import pytest

from eoo import Permutation


def test_permutation_constructor():
    # try constructing a wrong permutaiton
    permutation = [1, 3, 4, 1]
    try:
        permutation = Permutation(permutation)
        raise AssertionError("Incorrect permutation was allowed")
    except AssertionError:
        pass
    # construct correct permutation and test
    permutation = [1, 3, 4, 2]
    permutation = Permutation(permutation)
    assert permutation.n == 4, "Wrong permutation dimension"
    assert str(permutation) == "(1, 3, 4, 2)", "Wrong string representation"
