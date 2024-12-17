from main import fon, fetch_weather_data_std
import pytest
import datetime
def test_fon():
    assert (fon(-21) == 'midnightblue')
    assert (fon(-15) == 'steelblue')
    assert (fon(-7) == 'powderblue')
    assert (fon(-2) == 'lightcyan')
    assert (fon(5) == 'moccasin')
    assert (fon(12) == 'burlywood')
    assert (fon(18) == 'goldenrod')
    assert (fon(22) == 'darkorange')
    assert (fon(30) == 'firebrick')


def test_fon_invalid_input():
    with pytest.raises(ValueError):
        fon("a")
    with pytest.raises(ValueError):
        fon(None)

def test_fetch_weather_data_std_1():
    result = fetch_weather_data_std("Москва", "2024-12-17", "2024-12-17", '1h')
    assert(result[0]['datetime'] == datetime.datetime(2024, 12, 17, 0, 0))

def test_fetch_weather_data_std_():
    result = fetch_weather_data_std("Москва", "2024-12-16", "2024-12-17", '1h')
    assert(result[1]['datetime'] != datetime.datetime(2024, 12, 17, 0, 0))

def test_fetch_weather_data_std_3():
    result = fetch_weather_data_std("Москва", "2024-12-16", "2024-12-17", '1h')
    assert(result[0]['resolvedAddress'] == 'Москва, Центральный федеральный округ, Россия')

def test_fetch_weather_data_std_4():
    result = fetch_weather_data_std("Москва", "2024-12-16", "2024-12-17", '1h')
    assert(result[0]['address'] == "Москва")