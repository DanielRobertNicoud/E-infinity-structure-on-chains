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
    assert be.d == 3, "Wrong degree"
