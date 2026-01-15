from datetime import datetime

PJM_SITE_NAMES = [
    "AEP",
    "COMED",
    "DAYTON",
    "DEOK",
    "DOM",
    "DUQ",
    "EKPC",
    "FE",
    "NI",
    "PJME",
    "PJMW",
]

DEFAULT_VALIDATION_WINDOWS = [
    (datetime(2017, 5, 10, 12), datetime(2017, 5, 12, 12)),  # [Wednesday, Friday]
    (datetime(2017, 6, 8, 10), datetime(2017, 6, 10, 10)),  # [Thursday, Saturday]
    (datetime(2017, 7, 14, 14), datetime(2017, 7, 16, 14)),  # [Friday, Sunday]
    (datetime(2017, 8, 12, 3), datetime(2017, 8, 14, 3)),  # [Saturday, Monday]
    (datetime(2017, 9, 24, 7), datetime(2017, 9, 26, 7)),  # [Sunday, Tuesday]
    (datetime(2017, 10, 23, 18), datetime(2017, 10, 25, 18)),  # [Monday, Wednesday]
    (datetime(2017, 11, 7, 23), datetime(2017, 11, 9, 23)),  # [Tuesday, Thursday]
    (datetime(2017, 12, 20, 2), datetime(2017, 12, 22, 2)),  # [Wednesday, Friday]
    (datetime(2018, 1, 25, 12), datetime(2018, 1, 27, 12)),  # [Thursday, Saturday]
    (datetime(2018, 2, 16, 19), datetime(2018, 2, 18, 19)),  # [Friday, Sunday]
]
VALIDATION_WINDOWS = {
    "AEP": DEFAULT_VALIDATION_WINDOWS,
    "COMED": DEFAULT_VALIDATION_WINDOWS,
    "DAYTON": DEFAULT_VALIDATION_WINDOWS,
    "DEOK": DEFAULT_VALIDATION_WINDOWS,
    "DOM": DEFAULT_VALIDATION_WINDOWS,
    "DUQ": DEFAULT_VALIDATION_WINDOWS,
    "EKPC": DEFAULT_VALIDATION_WINDOWS,
    "FE": DEFAULT_VALIDATION_WINDOWS,
    # fmt: off
    "NI": [
        (datetime(2010, 3, 10, 12), datetime(2010, 3, 12, 12)),  # [Wednesday, Friday]
        (datetime(2010, 4, 8, 10), datetime(2010, 4, 10, 10)),  # [Thursday, Saturday]
        (datetime(2010, 5, 7, 14), datetime(2010, 5, 9, 14)),  # [Friday, Sunday]
        (datetime(2010, 6, 12, 3), datetime(2010, 6, 14, 3)),  # [Saturday, Monday]
        (datetime(2010, 7, 18, 7), datetime(2010, 7, 20, 7)),  # [Sunday, Tuesday]
        (datetime(2010, 8, 23, 18), datetime(2010, 8, 25, 18)),  # [Monday, Wednesday]
        (datetime(2010, 9, 7, 23), datetime(2010, 9, 9, 23)),  # [Tuesday, Thursday]
        (datetime(2010, 10, 13, 2), datetime(2010, 10, 15, 2)),  # [Wednesday, Friday]
        (datetime(2010, 11, 18, 12), datetime(2010, 11, 20, 12)),  # [Thursday, Saturday]
        (datetime(2010, 12, 17, 19), datetime(2010, 12, 19, 19)),  # [Friday, Sunday]
    ],
    # fmt: on
    "PJME": DEFAULT_VALIDATION_WINDOWS,
    "PJMW": DEFAULT_VALIDATION_WINDOWS,
}
