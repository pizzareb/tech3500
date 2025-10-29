import pytest


def divide(val1:int, val2:int) -> int:
    return val1 / val2

def test_divide_zero_exception():
    with pytest.raises(ZeroDivisionError):
        pass