import pytest
from working import convert, convert_time

def test_convert():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

def test_convert_error_hour():
    with pytest.raises(ValueError):
        convert("10 PM to 17 PM")

def test_convert_error_minutes():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")

def test_convert_error_no_to():
    with pytest.raises(ValueError):
        convert("9 AM 5 PM")