
import importlib
import pytest

module = importlib.import_module("30_factorial")
factorial = module.factorial


def test_factorial_of_zero():
    assert factorial(0) == 1


def test_factorial_of_one():
    assert factorial(1) == 1


def test_factorial_of_five():
    assert factorial(5) == 120


def test_factorial_of_six():
    assert factorial(6) == 720


def test_negative_number():
    with pytest.raises(ValueError):
        factorial(-1)