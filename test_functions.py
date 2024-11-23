# test_functions.py
def test_celsius_to_fahrenheit():
    from main import celsius_to_fahrenheit
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert celsius_to_fahrenheit(-40) == -40
