
import importlib.util
from pathlib import Path

program_path = (
    Path(__file__).resolve().parents[1]
    / "codes"
    / "29_count_vowels.py"
)

spec = importlib.util.spec_from_file_location(
    "count_vowels", program_path
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_count_vowels():
    assert module.count_vowels("hello") == 2
    assert module.count_vowels("AEIOU") == 5
    assert module.count_vowels("Python") == 1
    assert module.count_vowels("xyz") == 0
