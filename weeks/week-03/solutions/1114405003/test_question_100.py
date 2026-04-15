import unittest

from question_100 import solve


class TestQuestion100(unittest.TestCase):
    def test_sample_cases(self) -> None:
        self.assertEqual(
            solve("1 10\n100 200\n201 210\n900 1000\n"),
            "1 10 20\n100 200 125\n201 210 89\n900 1000 174",
        )

    def test_swapped_range(self) -> None:
        self.assertEqual(solve("10 1\n"), "10 1 20")


if __name__ == "__main__":
    unittest.main()