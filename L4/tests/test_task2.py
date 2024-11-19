import pytest
from tasks.task2 import arithmetic_sequence

def test_arithmetic_sequence():
    seq = arithmetic_sequence(-0.5, 0.1)
    result = [next(seq) for _ in range(5)]
    assert result == [-0.5, -0.4, -0.30000000000000004, -0.20000000000000004, -0.10000000000000003]
