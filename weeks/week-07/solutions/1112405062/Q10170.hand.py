import unittest
import math


def find_group_size(S: int, D: int) -> int:
    n = math.ceil((-(2 * S - 1) + math.sqrt((2 * S - 1) ** 2 + 8 * D)) / 2)
    return S + n - 1

if __name__ == "__main__":
    unittest.main()