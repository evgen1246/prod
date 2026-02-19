import pytest


@pytest.fixture()
def test_data() -> list:
    return [
        {"id": 1, "state": "EXECUTED", "date": "2018-10-14T00:00:00.000000", "amount": 150},
        {"id": 2, "state": "CANCELED", "date": "2018-10-12T08:00:00.000000", "amount": 200},
        {"id": 3, "state": "EXECUTED", "date": "2018-10-11T08:00:00.000000", "amount": 250},
        {"id": 4, "state": "CANCELED", "date": "2018-10-10T08:00:00.000000", "amount": 300},
    ]


@pytest.fixture()
def test_sort_date():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2018-10-14T00:00:00.000000", "amount": 150},
        {"id": 2, "state": "CANCELED", "date": "2018-10-12T08:00:00.000000", "amount": 200},
        {"id": 3, "state": "EXECUTED", "date": "2018-10-11T08:00:00.000000", "amount": 250},
        {"id": 4, "state": "CANCELED", "date": "2018-10-10T08:00:00.000000", "amount": 300},
    ]
