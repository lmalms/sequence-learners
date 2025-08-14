import numpy as np
import pandas as pd
import torch
from torch.utils.data import TensorDataset


class StandardScaler:
    def __init__(self):
        self.mean_: float | None = None
        self.scale_: float | None = None

    @property
    def is_fit(self) -> bool:
        return self.mean_ is not None and self.scale_ is not None

    def fit_transform(self, y: pd.Series) -> pd.Series:
        self.mean_ = y.mean()
        self.scale_ = y.std()
        return self.transform(y)

    def transform(self, y: pd.Series) -> pd.Series:
        assert self.is_fit
        return (y - self.mean_) / self.scale_

    def inverse_transform(self, y: pd.Series) -> pd.Series:
        assert self.is_fit
        return y * self.scale_ + self.mean_


class MeanScaler:
    def __init__(self):
        self.mean_: float | None = None

    @property
    def is_fit(self) -> bool:
        return self.mean_ is not None

    def fit_transform(self, y: pd.Series) -> pd.Series:
        self.mean_ = 1 + y.mean()
        return self.transform(y)

    def transform(self, y: pd.Series) -> pd.Series:
        assert self.is_fit
        return y / self.mean_

    def inverse_transform(self, y: pd.Series) -> pd.Series:
        assert self.is_fit
        return y * self.mean_


def get_tensor_train_dataset(
    y: pd.Series,
    in_seq_length: int,
    out_seq_length: int,
) -> TensorDataset:

    features, labels = [], []

    last_ts_idx = len(y) - in_seq_length
    last_ts_idx -= out_seq_length if out_seq_length > 1 else 0
    for i in range(last_ts_idx):
        # Get the features
        feat_start, feat_end = i, i + in_seq_length
        feat_seq = y.iloc[feat_start:feat_end]
        features.append(feat_seq.values)

        # Get the labels
        # Get an output sequence for each value of the input sequence
        for j in range(in_seq_length):
            label_start = i + j + 1
            label_end = i + j + out_seq_length + 1
            label_seq = y.iloc[label_start:label_end]
            labels.append(label_seq.values)

    # Turn into tensors
    feature_ts = torch.tensor(np.array(features), dtype=torch.float)
    feature_ts = feature_ts.view(-1, in_seq_length, 1)

    label_ts = torch.tensor(np.array(labels), dtype=torch.float32)
    label_ts = label_ts.view(-1, in_seq_length, out_seq_length)

    return TensorDataset(feature_ts, label_ts)
