from datetime import datetime

import polars as pl


def drop_client_timeseries(uci_df: pl.DataFrame, client_name: str) -> pl.DataFrame:
    return uci_df.select(pl.all().exclude(client_name))


def filter_client_timeseries(
    uci_df: pl.DataFrame,
    client_name: str,
    start_ts: datetime,
    end_ts: datetime,
) -> pl.DataFrame:

    client_df = uci_df.select(pl.col("timestamp"), pl.col(client_name)).filter(
        pl.col("timestamp").is_between(start_ts, end_ts, closed="both")
    )

    # Merge back onto main df
    uci_df = (
        uci_df.select(pl.all().exclude(client_name))
        .join(client_df, on="timestamp", how="left")
        .select(pl.all().exclude(client_name), pl.col(client_name).fill_null(0.0))
    )

    # Sort columns
    uci_df = uci_df.select(
        pl.col("timestamp"),
        *[pl.col(c) for c in sorted([c for c in uci_df.columns if c != "timestamp"])]
    )

    return uci_df
