import pytest

@pytest.fixture
def test_data():
    return [
        {"id": 921286598,
        "state": "EXECUTED",
        "date": "2018-03-09T23:57:37.537412",
        "operationAmount": {"amount": "25780.71",
                    "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Счет 26406253703545413262",
        "to": "Счет 20735820461482021315"},
        {"id": 207126257,
        "state": "EXECUTED",
        "date": "2019-07-15T11:47:40.496961",
        "operationAmount": {"amount": "92688.46",
                    "currency": {"name": "USD","code": "USD"}},
        "description": "Открытие вклада",
        "to": "Счет 35737585785074382265"},
        {"id": 957763565,
        "state": "EXECUTED",
        "date": "2021-01-05T00:52:30.108534",
        "operationAmount": {"amount": "87941.37",
                    "currency": {"name": "руб.","code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 46363668439560358409",
        "to": "Счет 18889008294666828266"},
        {"id": 667307132,
        "state": "EXECUTED",
        "date": "2019-07-13T18:51:29.313309",
        "operationAmount": {"amount": "97853.86",
                      "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод с карты на счет",
        "from": "Maestro 1308795367077170",
        "to": "Счет 96527012349577388612"}
    ]