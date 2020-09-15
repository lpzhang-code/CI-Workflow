import pytest

from maths import square, subtract


def test_square():
    assert square(2) == 4


def test_subtract():
    assert subtract(4, 1) == 3
