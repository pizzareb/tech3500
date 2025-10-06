from app.addition import add


def test_addition():
    result = add(val1=4, val2=2)

    assert result == 6
