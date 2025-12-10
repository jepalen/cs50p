import pytest
from calculator import expo


def main():
    test_positive_square()


def test_positive_square():

    assert expo(2, 2) == 4
    assert expo(3, 2) == 9


def test_negative_square():

    assert expo(-2, 2) == 4
    assert expo(-3, 2) == 9


def test_zero():
    assert expo(0, 2) == 0


def test_str():
    with pytest.raises(TypeError):
        expo("cat", 2)

if __name__ == "__main__":
    main()
