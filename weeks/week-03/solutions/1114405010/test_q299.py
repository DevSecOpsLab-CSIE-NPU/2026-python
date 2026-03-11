"""q299_hand.py 的單元測試。"""

import unittest

import q299_hand as q299


class TestQ299(unittest.TestCase):
    def test_sample(self) -> None:
        sample_input = "\n".join(
            [
                "3",
                "3",
                "1 3 2",
                "4",
                "4 3 2 1",
                "2",
                "1 2",
            ]
        )
        expected = "\n".join(
            [
                "Optimal train swapping takes 1 swaps.",
                "Optimal train swapping takes 6 swaps.",
                "Optimal train swapping takes 0 swaps.",
            ]
        )
        self.assertEqual(q299.solve(sample_input), expected)


if __name__ == "__main__":
    unittest.main()
