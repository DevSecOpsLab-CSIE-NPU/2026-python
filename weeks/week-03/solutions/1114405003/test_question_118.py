import unittest

from question_118 import solve


class TestQuestion118(unittest.TestCase):
    def test_sample_case(self) -> None:
        self.assertEqual(
            solve(
                "5 3\n"
                "1 1 E\n"
                "RFRFRFRF\n"
                "3 2 N\n"
                "FRRFLLFFRRFLL\n"
                "0 3 W\n"
                "LLFFFLFLFL\n"
            ),
            "1 1 E\n3 3 N LOST\n2 3 S",
        )

    def test_scent_avoidance(self) -> None:
        self.assertEqual(
            solve(
                "1 1\n"
                "0 0 N\n"
                "FF\n"
                "0 0 N\n"
                "FF\n"
            ),
            "0 1 N LOST\n0 1 N",
        )


if __name__ == "__main__":
    unittest.main()