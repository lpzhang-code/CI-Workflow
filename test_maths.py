import pytest

from maths import square, subtract


def test_square():
    assert square(4) == 16


def test_subtract():
    assert subtract(100, 10) == 90
