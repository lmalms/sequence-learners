from dataclasses import dataclass
from datetime import datetime
from typing import Any

from bikes.models.ets import ExponentialSmoothingLearner
from bikes.models.prophet import ProphetSequenceLearner
from bikes.models.sarima import SARIMASequenceLearner
from bikes.models.theta import ThetaSequenceLearner

VALIDATION_PERIODS = [
    (datetime(2024, 8, 1), datetime(2024, 9, 1)),
    (datetime(2024, 9, 1), datetime(2024, 10, 1)),
    (datetime(2024, 10, 1), datetime(2024, 11, 1)),
    (datetime(2024, 11, 1), datetime(2024, 12, 1)),
    (datetime(2024, 12, 1), datetime(2025, 1, 1)),
]


@dataclass
class ModelConfig:
    model_class: Any
    model_init_kwargs: dict[str, Any]


LOCATION_MODEL_CONFIGS: dict[str, list[ModelConfig]] = {
    "Nelson Street": [
        ModelConfig(
            model_class=ExponentialSmoothingLearner,
            model_init_kwargs={
                "trend": "add",
                "damped_trend": True,
                "seasonal": "mul",
                "seasonal_periods": 7,
                "freq": "D",
            },
        ),
        ModelConfig(
            model_class=SARIMASequenceLearner,
            model_init_kwargs={
                "order": (1, 1, 2),
                "seasonal_order": (1, 1, 1, 7),
                "freq": "D",
            },
        ),
        ModelConfig(
            model_class=ThetaSequenceLearner,
            model_init_kwargs={},
        ),
        ModelConfig(
            model_class=ProphetSequenceLearner,
            model_init_kwargs={},
        ),
    ],
}
