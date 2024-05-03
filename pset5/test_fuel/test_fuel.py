import pytest
from fuel import convert
from fuel import gauge

def test_convert_integer():
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("2/4") == 50

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(75) == "75%"

def test_convert():
    with pytest.raises(ZeroDivisionError):
        convert("100/0")
    with pytest.raises(ValueError):
        convert("three/four")