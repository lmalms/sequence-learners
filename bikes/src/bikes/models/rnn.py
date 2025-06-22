from datetime import timedelta

import pandas as pd
import torch
import torch.nn as nn
from loguru import logger
from torch.optim import Adam
from torch.utils.data import DataLoader

from bikes.preprocess.preprocess import get_tensor_train_dataset


class RNNSequenceLearner(nn.Module):
    def __init__(
        self,
        horizon: int,
        input_size: int = 1,
        hidden_size: int = 25,
        num_layers: int = 1,
    ):
        super().__init__()
        self.horizon = horizon
        self.rnn = nn.RNN(
            input_size=input_size,
            hidden_size=hidden_size,
            num_layers=num_layers,
            batch_first=True,
        )
        self.ho = nn.Linear(
            in_features=hidden_size,
            out_features=horizon,
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        out_, _ = self.rnn(x)
        return self.ho(out_)

    def fit(
        self,
        y: pd.Series,
        input_seq_length: int | None = None,
        n_epochs: int = 100,
        batch_size: int = 32,
        lr: float = 1e-03,
    ):
        self._train_start = y.index.min().to_pydatetime()
        self._train_end = y.index.max().to_pydatetime()

        # Prepare dataloader
        in_seq_length = input_seq_length or 3 * self.horizon
        ts = get_tensor_train_dataset(y, in_seq_length, self.horizon)
        dataloader = DataLoader(ts, batch_size=batch_size)

        # Define loss and optimizer
        loss_fn = nn.MSELoss()
        optimizer = Adam(self.parameters(), lr=lr)

        # Training loop
        self.train()
        for epoch in range(n_epochs):
            for X_train, y_train in dataloader:
                optimizer.zero_grad()
                y_hat = self(X_train)
                loss = loss_fn(y_train, y_hat)
                loss.backward()
                optimizer.step()

            if epoch % 10 == 0:
                logger.debug(f"Epoch [{epoch}/{n_epochs}], Loss: {loss.item():.4f}")

    def predict(
        self,
        y: pd.Series,
        input_seq_length: int | None = None,
    ) -> pd.Series:
        # RNNs requires some input features in order to make forecasts.
        in_seq_length = input_seq_length or 3 * self.horizon
        X_test_seq = y.iloc[-in_seq_length:].to_numpy()
        X_test = torch.tensor(X_test_seq, dtype=torch.float32).view(1, in_seq_length, 1)

        self.eval()
        with torch.no_grad():
            y_hat = self(X_test)

        # Get predictions for last input and construct series
        forecast_start = self._train_end + timedelta(days=1)
        forecast_end = forecast_start + timedelta(days=self.horizon - 1)
        y_hat_index = pd.date_range(forecast_start, forecast_end, freq="D")
        y_hat_data = y_hat[0, -1, :].numpy()
        y_hat = pd.Series(data=y_hat_data, index=y_hat_index)

        return y_hat
