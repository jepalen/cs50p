import pytest
from distances import convert_to_m


def main():
    test_positive()


def test_positive():
    assert convert_to_m(1) == 149597870691.7


def test_str():
    with pytest.raises(TypeError):
        convert_to_m("cat")


def test_float_coversion():
    assert convert_to_m(0.001) == pytest.approx(149597870.691, abs=1e-2)


if __name__ == "__main__":
    main()
