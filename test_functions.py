# test_functions.py
def test_celsius_to_fahrenheit():
    from main import celsius_to_fahrenheit
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert celsius_to_fahrenheit(-40) == -40

def test_fahrenheit_to_celsius():
    from main import fahrenheit_to_celsius
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(212) == 100
    assert fahrenheit_to_celsius(-40) == -40

def test_is_even():
    from main import is_even
    assert is_even(2) == True
    assert is_even(3) == False
    assert is_even(0) == True

