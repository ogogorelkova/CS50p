from numb3rs import validate

def test_validate():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("1000.0.0.0") != True
    assert validate("0.1000.0.0") != True
    assert validate("0.0.1000.0") != True
    assert validate("0.0.0.1000") != True
    assert validate("1.1.1") !=True
    assert validate("1.1.1.1.1") !=True
    assert validate("cat") !=True
    assert validate("cat.dog") !=True
    assert validate("10.290.8.4 ") != True