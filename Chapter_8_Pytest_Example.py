import pytest

@pytest.mark.parametrize("num", [0, 1, 2, 3, 4, 5])
def test_num(num):
    assert num % 2 == 0