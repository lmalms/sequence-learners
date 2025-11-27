import polars as pl


def get_min_max_timestamps_by_client(uci_df: pl.DataFrame) -> pl.DataFrame:
    min_max_ts = (
        uci_df.unpivot(
            on=[c for c in uci_df.columns if c != "timestamp"],
            index="timestamp",
            variable_name="client",
        )
        .filter(pl.col("value") > 0)
        .group_by("client", maintain_order=True)
        .agg(
            min_timestamp=pl.col("timestamp").min(),
            max_timestamp=pl.col("timestamp").max(),
        )
    )
    return min_max_ts
