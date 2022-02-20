import pytest

from eoo import BarratEccles


def test_constructor_barrateccles():
    p, q, r = [1, 2, 3, 4], [2, 1, 4, 3], [1, 4, 2, 3]
    t = [2, 1, 3]
    # composing with wrong dimensions
    try:
        BarratEccles([p, q, r, t])
        raise Exception("Constructed element with incompatible dimensions")
    except AssertionError:
        pass
    # correct element
    be = BarratEccles([p, q, r])
    assert be.r == 4, "Wrong arity"
    assert be.d == 2, "Wrong degree"


def test_degenerate():
    p, q, r = [1, 2, 3, 4], [2, 1, 4, 3], [1, 4, 2, 3]
    assert BarratEccles([p, q, q, r]).is_zero, "Degenerate != 0"
    assert not BarratEccles([p, q, r]).is_zero, "Non-degenerate == 0"


def test_repr():
    p, q, r = [1, 2, 3, 4], [2, 1, 4, 3], [1, 4, 2, 3]
    be = BarratEccles([p, q, r])
    s = (
        "| 1, 2, 3, 4\n"
        "| 2, 1, 4, 3\n"
        "| 1, 4, 2, 3\n"
        )
    assert str(be) == s


def test_equality():
    p, q, r = [1, 2, 3, 4], [2, 1, 4, 3], [1, 4, 2, 3]
    x = BarratEccles([p, q, r])
    y = BarratEccles([p, r, q])
    z = BarratEccles([p, q, q])
    assert x == x
    assert z == z
    assert x != y
    assert x != z
    assert y != z
