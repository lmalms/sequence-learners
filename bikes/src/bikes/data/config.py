from datetime import datetime
from typing import Annotated, Any

from pydantic import BaseModel, Field


class BikeDatasetLoadConfig(BaseModel):
    file_or_buffer: Annotated[str, Field(pattern=r"\.xlsx$")]
    load_kwargs: Annotated[dict[str, Any], Field(default_factory=dict)]


BIKE_DATASET_LOAD_CONFIGS = [
    BikeDatasetLoadConfig(
        file_or_buffer="https://at.govt.nz/media/1991027/auckland-trasnport-cycle-counts-jan-dec-2022.xlsx",
        load_kwargs={},
    ),
    BikeDatasetLoadConfig(
        file_or_buffer="https://at.govt.nz/media/1991376/auckland-transport-january-2023-cycle-counts.xlsx",
        load_kwargs={},
    ),
    BikeDatasetLoadConfig(
        file_or_buffer="https://at.govt.nz/media/1991377/auckland-transport-february-2023-cycle-counts.xlsx",
        load_kwargs={},
    ),
    BikeDatasetLoadConfig(
        file_or_buffer="https://at.govt.nz/media/1991436/auckland-transport-march-2023-cycle-counts.xlsx",
        load_kwargs={"na_values": "Pending"},
    ),
    BikeDatasetLoadConfig(
        file_or_buffer="https://at.govt.nz/media/1992545/april-2023-cycle-counts.xlsx",
        load_kwargs={},
    ),
    BikeDatasetLoadConfig(
        file_or_buffer="https://at.govt.nz/media/1992547/may-2023-cycle-counts.xlsx",
        load_kwargs={},
    ),
    BikeDatasetLoadConfig(
        file_or_buffer="https://at.govt.nz/media/1992546/june-2023-cycle-counts.xlsx",
        load_kwargs={},
    ),
    BikeDatasetLoadConfig(
        file_or_buffer="https://at.govt.nz/media/xs5lybun/at-daily-cycle-data-july-2023.xlsx",
        load_kwargs={"header": 2},
    ),
    BikeDatasetLoadConfig(
        file_or_buffer="https://at.govt.nz/media/t3zlbdn4/at-daily-cycle-data-august-2023.xlsx",
        load_kwargs={"header": 2},
    ),
    BikeDatasetLoadConfig(
        file_or_buffer="https://at.govt.nz/media/53rj40ji/at-daily-cycle-data-september-2023.xlsx",
        load_kwargs={"header": 2},
    ),
    BikeDatasetLoadConfig(
        file_or_buffer="https://at.govt.nz/media/hl0jbsrl/at-daily-cycle-data-october-2023.xlsx",
        load_kwargs={"header": 2},
    ),
    BikeDatasetLoadConfig(
        file_or_buffer="https://at.govt.nz/media/ty4js45t/at-daily-cycle-counts-november-2023.xlsx",
        load_kwargs={"header": 2},
    ),
    BikeDatasetLoadConfig(
        file_or_buffer="https://at.govt.nz/media/1tvdgsgo/at-daily-cycle-counts-december-2023.xlsx",
        load_kwargs={"header": 2},
    ),
    BikeDatasetLoadConfig(
        file_or_buffer="https://at.govt.nz/media/bb4h3wd3/at-daily-cycle-counts-january-2024.xlsx",
        load_kwargs={"header": 2},
    ),
    BikeDatasetLoadConfig(
        file_or_buffer="https://at.govt.nz/media/xlcaru0v/at-daily-cycle-counts-feb-2024.xlsx",
        load_kwargs={"header": 2},
    ),
    BikeDatasetLoadConfig(
        file_or_buffer="https://at.govt.nz/media/4g3hzpp5/at-daily-cycle-counts-march-2024.xlsx",
        load_kwargs={"header": 2},
    ),
    BikeDatasetLoadConfig(
        file_or_buffer="https://at.govt.nz/media/htvezqdn/at-daily-cycle-counts-april-2024.xlsx",
        load_kwargs={"header": 2},
    ),
    BikeDatasetLoadConfig(
        file_or_buffer="https://at.govt.nz/media/ue5cygl0/at-daily-cycle-counts-may-2024.xlsx",
        load_kwargs={"header": 2},
    ),
    BikeDatasetLoadConfig(
        file_or_buffer="https://at.govt.nz/media/3icd2jug/at-daily-cycle-counts-june-2024.xlsx",
        load_kwargs={"header": 2},
    ),
    BikeDatasetLoadConfig(
        file_or_buffer="https://at.govt.nz/media/jbdd1rox/cycle-counts-july-2024.xlsx",
        load_kwargs={"header": 2, "na_values": "z"},
    ),
    BikeDatasetLoadConfig(
        file_or_buffer="https://at.govt.nz/media/bvadzmqg/cycle-counts-august-2024.xlsx",
        load_kwargs={"usecols": "G:CG"},
    ),
    BikeDatasetLoadConfig(
        file_or_buffer="https://at.govt.nz/media/lpsfdwbe/auckland-transport-cycle-counts-september-2024.xlsx",
        load_kwargs={"usecols": "G:CG"},
    ),
    BikeDatasetLoadConfig(
        file_or_buffer="https://at.govt.nz/media/ohbhvmrl/auckland-transport-cycle-movements-october-2024.xlsx",
        load_kwargs={"header": 2},
    ),
    BikeDatasetLoadConfig(
        file_or_buffer="https://at.govt.nz/media/chelni1f/auckland-transport-cycle-movements-data-november-2024.xlsx",
        load_kwargs={"header": 2},
    ),
    BikeDatasetLoadConfig(
        file_or_buffer="https://at.govt.nz/media/zdumuud2/auckland-transport-cycle-movements-december-2024.xlsx",
        load_kwargs={"header": 2},
    ),
]


LOCATION_MAP = {
    "GI TO TAMAKI DR SECTION-1": "GI to Tamaki Drive Section-1",
    "Great North Road NB Towards CBD": "Great North Road",
    "Great South Road Manukau": "Great South Road",
    "Highbrook Pathway": "Highbrook Drive",
    "Lake Road Total New": "Lake Road",
    "Leigh Road Shared Path": "Leigh Road",
    "Mangere Foot Bridge": "Mangere Bridge",
    "Ocean View Road": "Oceanview Road",
    "Rathgar Road": "Rathger Road",
    "Remuera Road": "Remurua Road",
    "SH18 Upper Harbour Drive": "Upper Harbour",
    "SH20A Shared Path": "SH20A",
    "SW Shared Path": "SW SH20",
    "Symonds Street Total": "Symonds Street",
    "Tamaki Drive - Parnell": "Tamaki Drive",
    "TeAtatu Peninsula Shared Path": "TeAtatu Peninsula",
    "TeWero Bridge Bike Counter": "TeWero Bridge",
    "Ti Rakau - Opposite Bunnings": "Ti Rakau",
    "Ti Rakau opposite 92": "Ti Rakau",
    "Twin Streams Shared Path": "Twin Streams",
    "Upper Harbour Shared Path": "Upper Harbour",
    "Waterview Unitec Shared Path": "Waterview Unitec",
}

LOCATIONS_TO_EXCLUDE = [
    "Ngapipi Road SUP",
    "Meadowbank SUP",
    "Rankin Ave Shared Path",
    "Ti Rakau",
    "Ti Rakau Reserve",
    "Ti Rakau Riverhills",
    "TeWero Bridge",
]

LOCATION_OUTLIERS = {
    "Albany Highway": [
        datetime(2024, 10, 12),
        datetime(2024, 10, 21),
    ],
    "Archibald Park": [
        datetime(2023, 4, 12),
        datetime(2024, 3, 1),
        datetime(2024, 3, 9),
        datetime(2024, 9, 28),
    ],
    "GI to Tamaki Drive Section-1": [
        datetime(2022, 5, 28),
        datetime(2022, 6, 4),
    ],
    "Lake Road": [
        datetime(2024, 9, 2),
    ],
    "Mangere Safe Routes": [
        datetime(2022, 10, 15),
        datetime(2022, 12, 2),
        datetime(2024, 9, 24),
    ],
    "NW Cycleway TeAtatu": [
        datetime(2022, 5, 7),
    ],
    "Sandringham Road": [
        datetime(2024, 2, 19),
        datetime(2024, 2, 20),
        datetime(2024, 2, 21),
        datetime(2024, 2, 22),
        datetime(2024, 2, 23),
    ],
    "SH20A": [
        datetime(2022, 3, 2),
        datetime(2024, 2, 22),
    ],
    "SW SH20": [
        datetime(2024, 2, 2),
        datetime(2024, 2, 3),
        datetime(2024, 3, 27),
        datetime(2024, 4, 11),
        datetime(2024, 4, 12),
        datetime(2024, 4, 13),
    ],
}
