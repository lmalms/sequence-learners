import pandas as pd


class SequenceLearnerPipeline:
    def __init__(self, learner, transformer):
        self.learner = learner
        self.transformer = transformer

    @property
    def is_fit(self) -> bool:
        if self.transformer is not None:
            return self.learner.is_fit and self.transformer.is_fit
        return self.learner.is_fit

    def fit(self, y: pd.Series, **kwargs):
        if self.transformer is not None:
            self.transformer.fit(y)
            y = self.transformer.transform(y)
        self.learner.fit(y)

    def predict(self, **kwargs) -> pd.Series:
        y_hat = self.learner.predict(**kwargs)
        if self.transformer is not None:
            y_hat = self.transformer.inverse_transform(y_hat)
        return y_hat
