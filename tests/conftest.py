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
def test_sort_date() -> list:
    return [
        {"id": 1, "state": "EXECUTED", "date": "2018-10-14T00:00:00.000000", "amount": 150},
        {"id": 2, "state": "CANCELED", "date": "2018-10-12T08:00:00.000000", "amount": 200},
        {"id": 3, "state": "EXECUTED", "date": "2018-10-11T08:00:00.000000", "amount": 250},
        {"id": 4, "state": "CANCELED", "date": "2018-10-10T08:00:00.000000", "amount": 300},
    ]


@pytest.fixture()
def test_filter():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "руб", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "руб", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]


@pytest.fixture()
def description() -> str :
    return [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
    ]


@pytest.fixture()
def num_card() -> str:
    return [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]
