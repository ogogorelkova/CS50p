import pytest
from um import count


def test_punctuatiom():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("um....") == 1
    assert count("hey um yey") == 1

def test_Case():
    assert count("UM um Um") ==3

def test_begend():
    assert count("umami") ==0
    assert count("collossum") ==0