from plates import is_valid

def test_2letter():
    assert is_valid("plate") == True
    assert is_valid("hi222") == True
    assert is_valid("h2222") != True
    assert is_valid("22222") != True
    assert is_valid("22hi") != True

def test_lengh():
    assert is_valid("h") != True
    assert is_valid("hi12345") != True

def test_endnumber():
    assert is_valid("hi22hi") != True
    assert is_valid("hi022") != True

def test_putctuation():
    assert is_valid("hello!") != True
    assert is_valid("hi hi") != True
    assert is_valid("hi.hi") != True



