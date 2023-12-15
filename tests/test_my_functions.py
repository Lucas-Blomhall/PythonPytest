import pytest
import source.my_functions as my_functions


def test_add():
    result = my_functions.add(1, 4)
    assert result == 5


def test_divide():
    result = my_functions.divide(10, 5)
    assert result == 2


def test_divide_by_zero():
    # om vi skriver in "ZeroDivisionError" i parantesen så vi förväntar oss ett zero division error
    # men med vår funtion med ValueError så skickas det ValueError om vi har noll.
    with pytest.raises(ValueError):
        my_functions.divide(10, 0)
        assert True


def test_add_strings():
    result = my_functions.add("I like ", "Burgers")
    assert result == "I like Burgers"
