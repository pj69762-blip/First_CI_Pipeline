
import importlib

module = importlib.import_module("27_rotate_list")
rotate_list = module.rotate_list


def test_rotate_once():
    assert rotate_list([1, 2, 3, 4, 5], 1) == [5, 1, 2, 3, 4]


def test_rotate_two_positions():
    assert rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]


def test_rotate_by_length():
    assert rotate_list([1, 2, 3], 3) == [1, 2, 3]


def test_empty_list():
    assert rotate_list([], 2) == []


def test_zero_rotation():
    assert rotate_list([1, 2, 3], 0) == [1, 2, 3]
