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
        return self.fitted_model.forecast(steps=self.horizon)
