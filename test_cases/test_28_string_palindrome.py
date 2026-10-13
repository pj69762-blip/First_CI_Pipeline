
import importlib

module = importlib.import_module("28_string_palindrome")
is_palindrome = module.is_palindrome


def test_palindrome_word():
    assert is_palindrome("madam") is True


def test_non_palindrome_word():
    assert is_palindrome("hello") is False


def test_palindrome_with_spaces():
    assert is_palindrome("nurses run") is True


def test_uppercase_palindrome():
    assert is_palindrome("Madam") is True


def test_empty_string():
    assert is_palindrome("") is True


def test_single_character():
    assert is_palindrome("a") is True
