import unittest

from question_299 import solve


class TestQuestion299(unittest.TestCase):
    def test_sample_case(self) -> None:
        self.assertEqual(
            solve("3\n3\n1 2 3\n4\n4 3 2 1\n0\n"),
            "Optimal train swapping takes 0 swaps.\nOptimal train swapping takes 6 swaps.\nOptimal train swapping takes 0 swaps.",
        )

    def test_single_case(self) -> None:
        self.assertEqual(solve("1\n5\n5 1 2 3 4\n"), "Optimal train swapping takes 4 swaps.")


if __name__ == "__main__":
    unittest.main()