import pytest
from hw4 import count_simba, get_day_month_year, compute_distance, sum_general_int_list
from datetime import date
import pandas as pd
from geopy.distance import geodesic

def test_count_simba():
    strings = [
        "Simba and Nala are lions.",
        "I laugh in the face of danger.",
        "Hakuna matata",
        "Timon, Pumba and Simba are friends, but Simba could eat the other two."
    ]
    assert count_simba(strings) == 3

def test_get_day_month_year():
    dates_list = [date(2022, 10, 22), date(2023, 10, 23), date(2024, 10, 24)]
    result = get_day_month_year(dates_list)
    expected = pd.DataFrame({
        'day': [22, 23, 24],
        'month': [10, 10, 10],
        'year': [2022, 2023, 2024]
    })
    pd.testing.assert_frame_equal(result, expected) 

def test_compute_distance():
    coordinates = [((41.23, 23.5), (41.5, 23.4)), ((52.38, 20.1), (52.3, 17.8))]
    result = compute_distance(coordinates)
    expected = [
        geodesic((41.23, 23.5), (41.5, 23.4)).kilometers,
        geodesic((52.38, 20.1), (52.3, 17.8)).kilometers
    ]
    assert result == pytest.approx(expected) 

def test_sum_general_int_list():
    assert sum_general_int_list([1, 2, [3, 4], [[5]], 6]) == 21
    assert sum_general_int_list([1, [2, [3, 4]], 5]) == 15
    assert sum_general_int_list([0,0,[]]) == 0