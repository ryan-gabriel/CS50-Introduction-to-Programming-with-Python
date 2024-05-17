from fuel import convert, gauge
import pytest

def test_fuel():
    assert convert("3/4") == 75
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(10) == "10%"
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("100/50")

