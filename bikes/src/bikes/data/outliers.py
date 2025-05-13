from datetime import datetime

import numpy as np
import pandas as pd


def get_outlier_df(location_df: pd.DataFrame, n_sigma: float = 3.0) -> pd.DataFrame:
    outlier_df = location_df.copy()

    # Compute mean and std by weekday
    outlier_df = outlier_df.assign(weekday=outlier_df["date"].dt.weekday)
    weekday_stats = (
        outlier_df.groupby("weekday")[["count"]]
        .agg(["mean", "std"])
        .droplevel(level=0, axis=1)
        .reset_index()
    )
    outlier_df = outlier_df.merge(weekday_stats, how="left", on="weekday")

    # Define upper and lower bounds
    outlier_df = outlier_df.assign(
        upper=outlier_df["mean"] + n_sigma * outlier_df["std"],
        lower=outlier_df["mean"] - n_sigma * outlier_df["std"],
    )
    above_upper = outlier_df["count"] > outlier_df["upper"]
    below_lower = outlier_df["count"] < outlier_df["lower"]
    is_outlier = above_upper | below_lower
    outlier_df = outlier_df.assign(is_outlier=is_outlier)

    return outlier_df


def drop_outliers(
    cycle_counts: pd.DataFrame,
    outliers_by_location: dict[str, list[datetime]],
):
    # Construct outlier filter
    to_drop = pd.Series(np.full((len(cycle_counts),), False), index=cycle_counts.index)
    for loc, dates in outliers_by_location.items():
        loc_mask = cycle_counts["location"] == loc
        date_mask = cycle_counts["date"].isin(dates)
        to_drop |= loc_mask & date_mask

    return cycle_counts.loc[~to_drop]
