from datetime import datetime, timedelta

import pandas as pd
from prophet import Prophet


class ProphetSequenceLearner:

    def __init__(self, horizon: int, **kwargs):
        self.horizon = horizon
        self.model_kwargs = kwargs

        # self._train_start: datetime | None = None
        # self._train_end: datetime | None = None

    def fit(self, y: pd.Series) -> None:
        self._train_start = y.index.min().to_pydatetime()
        self._train_end = y.index.max().to_pydatetime()

        y_train = y.copy()
        y_train.name = "y"
        y_train.index.name = "ds"
        y_train = y_train.reset_index()

        self.model = Prophet(**self.model_kwargs).fit(y_train)

    def predict(self) -> pd.Series:
        forecast_start = self._train_end + timedelta(days=1)
        forecast_end = self._train_end + timedelta(days=self.horizon - 1)
        forecast_dates = pd.date_range(forecast_start, forecast_end, freq="D")

        y_hat = self.model.predict(pd.DataFrame({"ds": forecast_dates}))
        y_hat = (
            y_hat[["ds", "yhat"]]
            .rename(columns={"ds": "date", "yhat": "count"})
            .set_index("date")
            .squeeze()
        )

        return y_hat
