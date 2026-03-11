"""q100_hand.py 的單元測試。"""

import unittest

import q100_hand as q100


class TestQ100(unittest.TestCase):
    def test_sample(self) -> None:
        sample_input = "\n".join(
            [
                "1 10",
                "100 200",
                "201 210",
                "900 1000",
            ]
        )
        expected = "\n".join(
            [
                "1 10 20",
                "100 200 125",
                "201 210 89",
                "900 1000 174",
            ]
        )
        self.assertEqual(q100.solve(sample_input), expected)


if __name__ == "__main__":
    unittest.main()
