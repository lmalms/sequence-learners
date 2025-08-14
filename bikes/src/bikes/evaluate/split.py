import pandas as pd

from .config import TEST_PERIOD


def train_test_split(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    test_start_idx, test_end_idx = df.index.get_indexer(TEST_PERIOD)
    train_df = df.iloc[:test_start_idx].copy()
    test_df = df.iloc[test_start_idx:test_end_idx].copy()
    return train_df, test_df
