
import importlib

module = importlib.import_module("29_is_armstrong")
is_armstrong = module.is_armstrong


def test_three_digit_armstrong():
    assert is_armstrong(153) is True


def test_single_digit_number():
    assert is_armstrong(7) is True


def test_non_armstrong_number():
    assert is_armstrong(123) is False


def test_negative_number():
    assert is_armstrong(-153) is False


def test_zero():
    assert is_armstrong(0) is True
