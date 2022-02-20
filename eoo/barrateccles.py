from . permutation import Permutation

from typing import List, Union
from typeguard import check_type


class BarratEccles:
    """
    Basis elements of the Barrat-Eccles operad.

    Attributes:
        r   arity, equals to dimension of the permutations
        d   degree, given by the number of permutations
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
        self.d = len(permutations)
        # check that all permutations have the same dimension
        for p in self.permutations:
            assert p.n == self.r, \
                "Not all permutations have the same dimension."
