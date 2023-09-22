from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("hello how are you") == 0
    assert value("HELLO") == 0

def test_H():
    assert value("hi") == 20
    assert value("hhello") == 20
    assert value("HI") == 20

def test_others():
    assert value("100") == 100
    assert value("") == 100
    assert value("!!!") == 100


