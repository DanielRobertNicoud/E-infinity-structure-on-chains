import pytest

from eoo import Permutation


def test_permutation_constructor():
    # try constructing a wrong permutaiton
    permutation = [1, 3, 4, 1]
    try:
        permutation = Permutation(permutation)
        raise Exception("Incorrect permutation was allowed")
    except AssertionError:
        pass
    # construct correct permutation and test
    permutation = [1, 3, 4, 2]
    permutation = Permutation(permutation)
    assert permutation.n == 4, "Wrong permutation dimension"
    assert str(permutation) == "(1, 3, 4, 2)", "Wrong string representation"


def test_composite():
    p = Permutation([2, 3, 1])
    q = Permutation([3, 2, 1])
    r = Permutation([1, 2, 3, 4])
    # try composing wrong dimensions
    try:
        p * r
        raise Exception("Composed wrong dimension permutations")
    except AssertionError:
        pass
    # compose correct dimensions
    c = p * q
    assert c.n == 3, "Wrong dimension"
    assert str(c) == "(1, 3, 2)"
