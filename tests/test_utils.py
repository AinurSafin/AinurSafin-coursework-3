import pytest

from utils import get_data, get_last_data, get_formatted_data, get_filtered_data


def test_get_data():
    url = "https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1678905381256&signature=pynRU5kI_bfyDxJ-L_gtwOUyE_IRIfH7i6ata9xG6vs&downloadName=operations.json"
    assert get_data(url) is not None
    url = "https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5ef/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-"
    data, info = get_data(url)
    assert data is None
    assert info == "WARNING: Статус ответа 400"
    url = "https://fil.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1678905381256&signature=pynRU5kI_bfyDxJ-L_gtwOUyE_IRIfH7i6ata9xG6vs&downloadName=operations.json"
    data, info = get_data(url)
    assert data is None
    assert info == "ERROR: requests.exceptions.ConnectionError"


def test_get_filtered_data(test_data):
    assert len(get_filtered_data(test_data)) == 4
    assert len(get_filtered_data(test_data, filtered_empty_from=True)) == 3

def test_get_last_data(test_data):
    data = get_last_data(test_data, count_last_values=2)
    assert data[0]['date'] == '2021-01-05T00:52:30.108534'
    assert len(data) == 2


def test_get_formatted_data(test_data):
    data = get_formatted_data(test_data[:1])
    assert data == ['09.03.2018 Перевод организации\nСчет 2640 62** **** 3262 -> Счет **1315\n25780.71 руб.\n']
    data = get_formatted_data(test_data[1:2])
    assert data == ['15.07.2019 Открытие вклада\n[СКРЫТО]  -> Счет **2265\n92688.46 USD\n']
