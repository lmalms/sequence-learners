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
    (datetime(2017, 5, 10, 12), datetime(2017, 5, 12, 12)),
    (datetime(2017, 6, 8, 10), datetime(2017, 6, 10, 10)),
    (datetime(2017, 7, 14, 14), datetime(2017, 7, 16, 14)),
    (datetime(2017, 8, 15, 3), datetime(2017, 8, 17, 3)),
    (datetime(2017, 9, 21, 7), datetime(2017, 9, 23, 7)),
    (datetime(2017, 10, 23, 18), datetime(2017, 10, 25, 18)),
    (datetime(2017, 11, 7, 23), datetime(2017, 11, 9, 23)),
    (datetime(2017, 12, 19, 2), datetime(2017, 12, 21, 2)),
    (datetime(2018, 1, 28, 12), datetime(2018, 1, 30, 12)),
    (datetime(2018, 2, 14, 19), datetime(2018, 2, 16, 19)),
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
    "NI": [
        (datetime(2010, 3, 10, 12), datetime(2010, 3, 12, 12)),
        (datetime(2010, 4, 8, 10), datetime(2010, 4, 10, 10)),
        (datetime(2010, 5, 14, 14), datetime(2010, 5, 16, 14)),
        (datetime(2010, 6, 15, 3), datetime(2010, 6, 17, 3)),
        (datetime(2010, 7, 21, 7), datetime(2010, 7, 23, 7)),
        (datetime(2010, 8, 23, 18), datetime(2010, 8, 25, 18)),
        (datetime(2010, 9, 7, 23), datetime(2010, 9, 9, 23)),
        (datetime(2010, 10, 19, 2), datetime(2010, 10, 21, 2)),
        (datetime(2010, 11, 28, 12), datetime(2010, 11, 30, 12)),
        (datetime(2010, 12, 14, 19), datetime(2010, 12, 16, 19)),
    ],
    "PJME": DEFAULT_VALIDATION_WINDOWS,
    "PJMW": DEFAULT_VALIDATION_WINDOWS,
}
