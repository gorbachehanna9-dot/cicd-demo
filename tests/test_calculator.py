import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.calculator import add, subtract, divide, multiply  # noqa: E402


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(10, 4) == 6


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)


def test_multiply():
    assert multiply(3, 4) == 12
