import pytest
from app import generate_random_strings, arithmetic_sequence, map_cities

def test_generate_random_strings():
    result = list(generate_random_strings(5, 10))
    assert len(result) == 5
    assert all(len(s) == 10 for s in result)

def test_arithmetic_sequence():
    seq = arithmetic_sequence(-0.5, 0.1)
    result = [next(seq) for _ in range(5)]
    assert result == [-0.5, -0.4, -0.30000000000000004, -0.20000000000000004, -0.10000000000000003]

