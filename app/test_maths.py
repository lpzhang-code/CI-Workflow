from maths import *
import pytest


def test_add():
    assert add(1, 5) == 6
    assert not add(2, 7) == 4


def test_subtract():
    assert subtract(6, 4) == 2
    assert not subtract(5, 2) == 6


def test_multiply():
    assert multiply(4, 5) == 20
    assert not multiply(8, 7) == 50


def test_divide():
    assert divide(20, 2) == 10
    assert not divide(9, 3) == 2


def test_square():
    assert square(5) == 25
    assert not square(3) == 10
