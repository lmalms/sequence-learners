import pandas as pd


def resample_cycle_counts(cycle_counts: pd.DataFrame, freq: str = "D"):
    location_dfs = []
    for loc, location_df in cycle_counts.groupby("location"):
        location_df = (
            location_df.set_index("date")
            .resample(freq)
            .asfreq()
            .reset_index(names="date")
        )
        location_df["location"] = location_df["location"].fillna(value=loc)
        location_dfs.append(location_df)

    cycle_counts = pd.concat(location_dfs, axis=0, ignore_index=True)
    return cycle_counts
