from twttr import shorten

def test_shorten():
    assert shorten("hello") == "hll"

def test_cap():
    assert shorten("CAbBagE") == "CbBg"

def test_str():
    assert shorten("CS50!") == "CS50!"
