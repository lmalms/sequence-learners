from datetime import datetime, timedelta

import pandas as pd
from statsmodels.tsa.api import ExponentialSmoothing


class ExponentialSmoothingLearner:
    def __init__(self, horizon: int, **kwargs):
        self.horizon = horizon
        self.model_kwargs = kwargs

        # self.model = None
        # self.fitted_model = None

        # self._train_start: datetime | None = None
        # self._train_end: datetime | None = None

    def fit(self, y: pd.Series) -> None:
        self._train_start = y.index.min().to_pydatetime()
        self._train_end = y.index.max().to_pydatetime()

        self.model = ExponentialSmoothing(endog=y, **self.model_kwargs)
        self.fitted_model = self.model.fit()

    def predict(self) -> pd.Series:
        forecast_start = self._train_end + timedelta(days=1)
        forecast_end = forecast_start + timedelta(days=self.horizon)
        forecasts = self.fitted_model.predict(forecast_start, forecast_end)
        return forecasts
