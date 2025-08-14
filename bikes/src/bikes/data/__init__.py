import pandas as pd
from tqdm import tqdm

from .changepoints import adjust_scale
from .config import (
    BIKE_DATASET_LOAD_CONFIGS,
    LOCATION_CHANGEPOINTS,
    LOCATION_OUTLIERS,
    LOCATIONS_TO_EXCLUDE,
)
from .dataset import BikeDataset
from .impute import impute_missing_cycle_counts
from .outliers import drop_outliers
from .resample import resample_cycle_counts


def load_cycle_counts() -> pd.DataFrame:
    dfs: list[pd.DataFrame] = []
    for load_config in tqdm(BIKE_DATASET_LOAD_CONFIGS):
        try:
            ds = BikeDataset.load(load_config)
        except Exception as e:
            print("Could not load data for url: ", load_config.file_or_buffer)
            print("Reason: ", e)
            continue
        dfs.append(ds.data)

    cycle_counts = pd.concat(dfs, axis=0, ignore_index=True)

    # Drop locations
    to_exclude = cycle_counts["location"].isin(LOCATIONS_TO_EXCLUDE)
    cycle_counts = cycle_counts.loc[~to_exclude].copy()

    # Drop duplicate readings and missing readings
    cycle_counts = cycle_counts.drop_duplicates().dropna(subset=["count"])

    # Drop known outliers, resample to daily freq and fill missing values
    cycle_counts = drop_outliers(cycle_counts, LOCATION_OUTLIERS)
    cycle_counts = resample_cycle_counts(cycle_counts)
    cycle_counts = impute_missing_cycle_counts(cycle_counts)

    # Adjust scale between changepoints
    cycle_counts = adjust_scale(cycle_counts, LOCATION_CHANGEPOINTS)

    return cycle_counts
