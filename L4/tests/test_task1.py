import pytest
from tasks.task1 import generate_random_strings

def test_generate_random_strings():
    result = list(generate_random_strings(5, 10))
    assert len(result) == 5
    assert all(len(s) == 10 for s in result)
