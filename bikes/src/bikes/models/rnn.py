import pandas as pd
import torch
import torch.nn as nn
from torch.optim import Adam
from torch.utils.data import DataLoader

from bikes.utils.preprocess import get_tensor_train_dataset


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
                print(f"Epoch [{epoch}/{n_epochs}], Loss: {loss.item():.4f}")
                print("------------------------------")
