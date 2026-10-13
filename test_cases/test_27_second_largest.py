
import importlib
import pytest

module = importlib.import_module("27_second_largest")
second_largest = module.second_largest


def test_normal_list():
    assert second_largest([10, 5, 8, 20, 15]) == 15


def test_duplicate_numbers():
    assert second_largest([10, 10, 8, 8, 5]) == 8


def test_negative_numbers():
    assert second_largest([-10, -5, -20, -2]) == -5


def test_two_distinct_numbers():
    assert second_largest([3, 7]) == 3


def test_all_same_numbers():
    with pytest.raises(ValueError):
        second_largest([5, 5, 5])


def test_empty_list():
    with pytest.raises(ValueError):
        second_largest([])
