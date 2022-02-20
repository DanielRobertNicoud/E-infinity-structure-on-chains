from typing import List


class Permutation:
    """
    Represents a single permutation.

    A permutation sigma is given as [sigma(1), ..., sigma(n)]. Internally it
    is represented shifting everything by 1 (ie starts at 0 not at 1).
    """

    def __init__(self, permutation: List[int]):
        self.n = len(permutation)
        # shift by 1
        self.permutation = [x - 1 for x in permutation]
        # check it is a well defined permutation
        assert set(self.permutation) == set(range(self.n)), \
            "Invalid permutation"
        return

    def __repr__(self) -> str:
        return "(" + ", ".join([str(x + 1) for x in self.permutation]) + ")"

    def __mul__(self, other):
        """
        Composition of permutations.
        """
        # check the two permutations have same dimension
        assert self.n == other.n, "Trying to compose permutations of " \
            "different dimension"
        composite = [self.permutation[x] + 1 for x in other.permutation]
        return Permutation(composite)


if __name__ == "__main__":
    p = Permutation([2, 3, 1])
    q = Permutation([3, 2, 1])
    print(p * q)
