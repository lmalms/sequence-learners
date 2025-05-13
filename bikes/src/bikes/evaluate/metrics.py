import numpy as np
import pandas as pd


def mase(y_train: pd.Series, y_true: pd.Series, y_hat: pd.Series, season: int = 1):
    """
    Mean Absolute Scaled Error
    """

    y_train = np.array(y_train)
    y_true = np.array(y_true)
    y_hat = np.array(y_hat)

    forecast_error = np.abs(y_true - y_hat)
    in_sample_error = np.abs(y_train[season:] - y_train[:-season])
    return np.mean(forecast_error) / np.mean(in_sample_error)
