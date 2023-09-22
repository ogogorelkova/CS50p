from seasons import convert
import pytest

def test_convert():
    assert convert("2000-01-01") == "Twelve million, one hundred ninety-nine thousand, six hundred eighty"
    with pytest.raises(SystemExit):
        convert("2000-01")
    with pytest.raises(SystemExit):
        convert("2000-01-01-01")
    with pytest.raises(SystemExit):
        convert("January 1, 2001")
    with pytest.raises(SystemExit):
        convert("01-01-2000")
