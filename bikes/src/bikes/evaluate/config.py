from dataclasses import dataclass
from datetime import datetime
from typing import Any

from bikes.models.ets import ExponentialSmoothingLearner
from bikes.models.prophet import ProphetSequenceLearner
from bikes.models.rnn import RNNSequenceLearner
from bikes.models.sarima import SARIMASequenceLearner
from bikes.models.theta import ThetaSequenceLearner

VALIDATION_PERIODS = [
    (datetime(2024, 8, 1), datetime(2024, 9, 1)),
    (datetime(2024, 9, 1), datetime(2024, 10, 1)),
    (datetime(2024, 10, 1), datetime(2024, 11, 1)),
    (datetime(2024, 11, 1), datetime(2024, 12, 1)),
    (datetime(2024, 12, 1), datetime(2025, 1, 1)),
]

TEST_PERIOD = datetime(2024, 10, 1), datetime(2025, 1, 1)

TEST_LOCATIONS = [
    "Dominion Road",
    "Upper Queen Street",
    "Grafton Road",
    "Orewa Path",
    "Lake Road",
    "Beach Road",
    "Mangere Bridge",
    "Westhaven Drive",
    "Grafton Gully",
    "Waterview Unitec",
    "Grafton Bridge",
    "Karangahape Road",
    "Nelson Street",
    "NW Cycleway TeAtatu",
    "Lightpath",
    "Quay Street - Spark Arena",
    "NW Cycleway Kingsland",
    "Tamaki Drive",
    "Quay Street Eco Display Classic",
]


@dataclass
class PipelineConfig:
    learner_class: Any
    learner_kwargs: dict[str, Any]
    transformer_class: Any = None
    transformer_kwargs: dict[str, Any] | None = None


LOCATION_MODEL_CONFIGS: dict[str, list[PipelineConfig]] = {
    "Nelson Street": [
        PipelineConfig(
            learner_class=ExponentialSmoothingLearner,
            learner_kwargs={
                "trend": "add",
                "damped_trend": True,
                "seasonal": "mul",
                "seasonal_periods": 7,
                "freq": "D",
            },
        ),
        PipelineConfig(
            learner_class=SARIMASequenceLearner,
            learner_kwargs={
                "order": (1, 1, 2),
                "seasonal_order": (1, 1, 1, 7),
                "freq": "D",
            },
        ),
        PipelineConfig(
            learner_class=ThetaSequenceLearner,
            learner_kwargs={},
        ),
        PipelineConfig(
            learner_class=ProphetSequenceLearner,
            learner_kwargs={},
        ),
    ],
}
