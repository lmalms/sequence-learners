from pathlib import Path

import pandas as pd

from .config import LOCATION_MODEL_CONFIGS, VALIDATION_PERIODS, ModelConfig


def get_model_forecasts(df: pd.DataFrame, model_config: ModelConfig) -> pd.DataFrame:

    all_forecast_dfs = []

    for fold_idx, (val_start, val_end) in enumerate(VALIDATION_PERIODS):
        train_df = df.loc[df["date"] < val_start]
        train_df = train_df.set_index("date").sort_index()

        val_df = df.loc[(df["date"] >= val_start) & (df["date"] < val_end)]
        val_df = val_df.set_index("date").sort_index()

        horizon = (val_end - val_start).days

        # Fit model and make predictions
        model = model_config.model_class(
            horizon=horizon,
            **model_config.model_init_kwargs,
        )
        model.fit(train_df.loc[:, "count"])
        y_hat_df = (
            model.predict()
            .to_frame(name="forecast")
            .assign(model=model.__class__.__name__, fold_idx=fold_idx)
        )

        # Merge ground truth and forecasts
        forecast_df = pd.merge(
            left=val_df.rename(columns={"count": "actual"}),
            right=y_hat_df,
            left_index=True,
            right_index=True,
        )

        # Reset index to make date column rather than index
        forecast_df = forecast_df.reset_index()
        all_forecast_dfs.append(forecast_df)

    return pd.concat(all_forecast_dfs, axis=0, ignore_index=True)


def run_evaluation(cycle_counts_df: pd.DataFrame, forecast_dir: Path):

    forecast_dir.mkdir(parents=True, exist_ok=True)

    for location, models in LOCATION_MODEL_CONFIGS.items():
        location_mask = cycle_counts_df["location"] == location
        location_df = cycle_counts_df.loc[location_mask].copy()
        location_df = location_df.sort_values(by="date")

        # Compute forecasts
        all_model_forecasts = []
        for model in models:
            forecast_df = get_model_forecasts(location_df, model)
            all_model_forecasts.append(forecast_df)

        all_forecasts_df = pd.concat(all_model_forecasts, axis=0, ignore_index=True)
        forecast_path = forecast_dir / f"{location}.parquet"
        all_forecasts_df.to_parquet(forecast_path)
