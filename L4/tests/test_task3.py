import pytest
from tasks.task3 import map_cities

def test_map_cities():
    result = map_cities("New York Moscow Sydney London Paris")
    assert result == ['New York', 'Moscow', '-', 'London', 'Paris']
