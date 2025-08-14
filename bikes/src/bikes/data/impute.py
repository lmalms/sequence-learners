import pandas as pd


def impute_missing_cycle_counts(cycle_counts: pd.DataFrame) -> pd.DataFrame:
    location_dfs = []
    for _, location_df in cycle_counts.groupby("location"):
        if location_df["count"].isna().any():

            # First interpolate
            location_df = location_df.sort_values("date")
            location_df["count"] = location_df["count"].interpolate(limit=1)

            # Fill remaining NaNs using weekday mean
            location_df["weekday"] = location_df["date"].dt.weekday
            weekday_mean = (
                location_df.groupby("weekday")[["count"]]
                .mean()
                .astype(int)
                .reset_index()
                .rename(columns={"count": "mean"})
            )
            location_df = location_df.merge(weekday_mean, on="weekday", how="left")
            location_df["count"] = location_df["count"].fillna(location_df["mean"])
            location_df = location_df.drop(columns=["weekday", "mean"])

        location_dfs.append(location_df)

    cycle_counts = pd.concat(location_dfs, axis=0, ignore_index=True)
    return cycle_counts
