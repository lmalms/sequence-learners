from datetime import datetime

import polars as pl


def interpolate_client_timeseries(
    uci_df: pl.DataFrame,
    client_name: str,
    start_ts: datetime,
    end_ts: datetime,
    interval: str = "15m",
) -> pl.DataFrame:
    """
    Filter a client timeseries to between start_ts and end_ts, and interpolate
    """

    # Get all non-zero observations between start_ts and end_ts
    client_df = uci_df.select(pl.col("timestamp"), pl.col(client_name)).filter(
        pl.col("timestamp").is_between(start_ts, end_ts, closed="both"),
        pl.col(client_name) > 0,
    )

    # Construct timeseries of expected timestamps between start_ts and end_ts
    expected_ts = pl.datetime_range(
        start=start_ts,
        end=end_ts,
        interval=interval,
        closed="both",
        eager=True,
    )

    # Merge and interpoalte
    client_df = (
        expected_ts.to_frame(name="timestamp")
        .join(client_df, on="timestamp", how="left")
        .select(pl.col("timestamp"), pl.col(client_name).interpolate())
    )

    # Merge back onto original uci_df
    uci_df = (
        uci_df.select(pl.all().exclude(client_name))
        .join(client_df, on="timestamp", how="left")
        .select(pl.all().exclude(client_name), pl.col(client_name).fill_null(0.0))
    )

    # Sort columns
    uci_df = uci_df.select(
        pl.col("timestamp"),
        *[pl.col(c) for c in sorted([c for c in uci_df.columns if c != "timestamp"])],
    )

    return uci_df
