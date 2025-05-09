import pandas as pd

from .config import LOCATION_MAP, BikeDatasetLoadConfig


class BikeDataset:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    @staticmethod
    def _load_dataset(config: BikeDatasetLoadConfig):
        df = pd.read_excel(config.file_or_buffer, **config.load_kwargs)
        df = df.rename(columns={"Date": "date", "Date.1": "date", "Time": "date"})
        df = df.melt(id_vars="date", var_name="location", value_name="count")
        df = df.astype({"date": "datetime64[ns]", "location": str, "count": float})
        return df

    @staticmethod
    def _map_locations(df: pd.DataFrame) -> str:
        df["location"] = df["location"].apply(lambda loc: LOCATION_MAP.get(loc, loc))
        return df

    @staticmethod
    def _standardise_locations(df: pd.DataFrame) -> pd.DataFrame:
        df["location"] = df["location"].str.replace(r" Cyclists?", "", regex=True)
        df["location"] = df["location"].str.replace(r"\bDr\b", "Drive", regex=True)
        df["location"] = df["location"].str.replace(r"\bRd\b", "Road", regex=True)
        df["location"] = df["location"].str.replace(r"\bSt\b", "Street", regex=True)
        return df

    @classmethod
    def load(self, config: BikeDatasetLoadConfig) -> "BikeDataset":
        df = self._load_dataset(config)
        df = self._standardise_locations(df)
        df = self._map_locations(df)
        return BikeDataset(df)
