from datetime import datetime

import numpy as np
import pandas as pd
import ruptures as rpt


def get_changepoint_locations(
    location_df: pd.DataFrame,
    n_chpts: int,
) -> list[datetime]:
    location_df = location_df.copy()
    location_df = location_df.sort_values("date")

    model = rpt.Dynp(model="l2").fit(np.array(location_df["count"]))
    chpts_idx = model.predict(n_bkps=n_chpts)

    min_date, max_date = location_df["date"].min(), location_df["date"].max()
    chpts_dt = [location_df.iloc[idx]["date"].to_pydatetime() for idx in chpts_idx[:-1]]
    chpts_dt = [min_date.to_pydatetime()] + chpts_dt + [max_date.to_pydatetime()]

    return chpts_dt


def adjust_scale(
    cycle_counts: pd.DataFrame,
    chpts_by_location: dict[str, list[datetime]],
):
    for loc, chpts in chpts_by_location.items():
        loc_mask = cycle_counts["location"] == loc

        # Find the longest streak, this is the anchor
        chpt_streaks = list(zip(chpts, chpts[1:]))
        streak_lengths = [
            (loc_mask & cycle_counts["date"].between(s, e, inclusive="left")).sum()
            for (s, e) in chpt_streaks
        ]
        longest_streak = chpt_streaks[streak_lengths.index(max(streak_lengths))]

        # Calculate mean of longest streak
        ls_start, ls_end = longest_streak
        ls_mask = cycle_counts["date"].between(ls_start, ls_end, inclusive="left")
        ls_mean = cycle_counts[loc_mask & ls_mask]["count"].mean()

        # Scale every streak using anchor stats
        for streak_start, streak_end in chpt_streaks:
            streak_mask = cycle_counts["date"].between(
                streak_start, streak_end, inclusive="left"
            )
            streak_mean = cycle_counts[loc_mask & streak_mask]["count"].mean()
            loc_streak_counts = cycle_counts.loc[loc_mask & streak_mask, "count"]
            loc_streak_counts_adj = loc_streak_counts.div(streak_mean).mul(ls_mean)
            cycle_counts.loc[loc_mask & streak_mask, "count"] = loc_streak_counts_adj

    cycle_counts["count"] = cycle_counts["count"].astype(int)
    return cycle_counts
