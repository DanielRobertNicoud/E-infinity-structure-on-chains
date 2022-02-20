from .permutation import Permutation

from typing import List, Union
from typeguard import check_type


class BarratEccles:
    """
    Basis elements of the Barrat-Eccles operad.

    Attributes:
        r               arity, equals to dimension of the permutations
        d               degree, given by the number of permutations
        permutations    the permutations composing the element
        is_zero         True if degenerate
    """

    def __init__(
            self, permutations: Union[List[Permutation], List[List[int]]]
            ):
        """
        Takes a list of permutations (either Permutation or lists passed to the
        Permutation constructor).
        """
        # transform to permutations if needed.
        try:
            check_type("permutations", permutations, List[List[int]])
            permutations = [Permutation(p) for p in permutations]
        except TypeError:
            pass
        self.permutations = permutations
        self.r = self.permutations[0].n
        self.d = len(self.permutations) - 1
        # check that all permutations have the same dimension
        for p in self.permutations:
            assert p.n == self.r, \
                "Not all permutations have the same dimension."
        # check if it is the zero element (degenerate)
        self.is_zero = False
        for i in range(self.d):
            if self.permutations[i] == self.permutations[i + 1]:
                self.is_zero = True
                break

    def __repr__(self):
        """
        Table representation.
        """
        return "\n".join([
            "| " + ", ".join([str(x + 1) for x in p.permutation])
            for p in self.permutations
            ])

    def __eq__(self, other):
        if self.is_zero != other.is_zero:
            return False
        if self.is_zero:
            return True
        return str(self) == str(other)

    def __rmul__(self, other: Permutation):
        permutations_out = [other * p for p in self.permutations]
        return BarratEccles(permutations_out)
