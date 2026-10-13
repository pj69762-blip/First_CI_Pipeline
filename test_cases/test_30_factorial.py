
import importlib.util
from pathlib import Path
import pytest

program_path = (
    Path(__file__).resolve().parents[1]
    / "codes"
    / "30_factorial.py"
)

spec = importlib.util.spec_from_file_location(
    "factorial", program_path
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_factorial():
    assert module.factorial(0) == 1
    assert module.factorial(1) == 1
    assert module.factorial(5) == 120
    assert module.factorial(6) == 720


def test_negative_factorial():
    with pytest.raises(ValueError):
        module.factorial(-1)
        