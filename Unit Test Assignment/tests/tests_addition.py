from app.addition import add


def tests_addition():
    result = add(val1=4, val2=2)

    assert result == 6
