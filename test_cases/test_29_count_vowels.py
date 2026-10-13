
import importlib

module = importlib.import_module("29_count_vowels")
count_vowels = module.count_vowels


def test_normal_string():
    assert count_vowels("hello") == 2


def test_uppercase_string():
    assert count_vowels("AEIOU") == 5


def test_no_vowels():
    assert count_vowels("xyz") == 0


def test_empty_string():
    assert count_vowels("") == 0


def test_mixed_string():
    assert count_vowels("Python Programming") == 4
