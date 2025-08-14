import numpy as np
import pandas as pd


def mase(y_train: pd.Series, y_true: pd.Series, y_pred: pd.Series, season: int = 1):
    """
    Mean Absolute Scaled Error
    """

    y_train = np.array(y_train)
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    forecast_error = np.abs(y_true - y_pred)
    in_sample_error = np.abs(y_train[season:] - y_train[:-season])
    return np.mean(forecast_error) / np.mean(in_sample_error)


def mape(y_true: pd.Series, y_pred: pd.Series):
    """
    Mean Absolute Percentage Error
    """

    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true))
