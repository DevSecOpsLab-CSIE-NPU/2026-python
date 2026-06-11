import unittest
from sorts_fast import quick_sort_fast, builtin_sorted

SORTS = [quick_sort_fast, builtin_sorted]

TEST_CASES = [
    ([], []),
    ([1], [1]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ([3, 1, 2, 1, 3], [1, 1, 2, 3, 3]),
    ([-1, 3, -5, 0], [-5, -1, 0, 3]),
]


class TestSortsFast(unittest.TestCase):
    def test_correctness(self):
        for s in SORTS:
            for data, expected in TEST_CASES:
                with self.subTest(sort=s.__name__, data=data):
                    original = data.copy()
                    result = s(data)
                    self.assertEqual(result, expected)
                    self.assertEqual(data, original, f"{s.__name__} mutated input!")


if __name__ == "__main__":
    unittest.main()
