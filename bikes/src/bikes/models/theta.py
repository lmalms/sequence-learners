from datetime import timedelta

import pandas as pd
from statsmodels.tsa.forecasting.theta import ThetaModel


class ThetaSequenceLearner:
    def __init__(self, horizon: int, **kwargs):
        self.horizon = horizon
        self.model_kwargs = kwargs

    def fit(self, y: pd.Series):
        self._train_start = y.index.min().to_pydatetime()
        self._train_end = y.index.max().to_pydatetime()

        self.model = ThetaModel(endog=y, **self.model_kwargs)
        self.fitted_model = self.model.fit()

    def predict(self) -> pd.Series:
        forecast_start = self._train_end + timedelta(days=1)
        forecast_end = forecast_start + timedelta(days=self.horizon - 1)
        forecast_dates = pd.date_range(forecast_start, forecast_end, freq="D")

        y_hat = self.fitted_model.forecast(steps=self.horizon)
        y_hat.index = forecast_dates

        return y_hat
