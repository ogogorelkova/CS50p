import pytest
from working import convert


def test_convert():
    # Test normal case
    assert convert("09:05 PM to 02:15 AM") == "21:05 to 02:15"

    # Test border case with different hours
    assert convert("11:59 PM to 12:01 AM") == "23:59 to 00:01"

    # Test border case with same hours
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"

def test_valueError():
    with pytest.raises(ValueError):
        convert("09:65 AM to 10:30 AM")

def test_valueError2():
    with pytest.raises(ValueError):
        convert("09:00 AM - 10:30 AM")
