import pytest
from tasks.task2 import arithmetic_sequence

def test_arithmetic_sequence():
    seq = arithmetic_sequence(-0.5, 0.1)
    result = [next(seq) for _ in range(5)]
    assert result == [-0.5, -0.4, -0.3, -0.2, -0.1]
