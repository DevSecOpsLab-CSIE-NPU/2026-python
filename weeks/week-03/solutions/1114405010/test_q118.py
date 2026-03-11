"""q118_hand.py 的單元測試。"""

import unittest

import q118_hand as q118


class TestQ118(unittest.TestCase):
    def test_sample(self) -> None:
        sample_input = "\n".join(
            [
                "5 3",
                "1 1 E",
                "RFRFRFRF",
                "3 2 N",
                "FRRFLLFFRRFLL",
                "0 3 W",
                "LLFFFLFLFL",
            ]
        )
        expected = "\n".join(
            [
                "1 1 E",
                "3 3 N LOST",
                "2 3 S",
            ]
        )
        self.assertEqual(q118.solve(sample_input), expected)


if __name__ == "__main__":
    unittest.main()
