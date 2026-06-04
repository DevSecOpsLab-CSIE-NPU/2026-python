import unittest

from gcd import sum_of_gcd


class TestSumOfGcd(unittest.TestCase):
    def test_required_cases(self):
        """課堂要求的三個案例：n=2、n=10、n=1(edge)"""
        cases = [
            (2, 1),
            (10, 67),
            (1, 0),
        ]
        for n, expected in cases:
            with self.subTest(n=n):
                self.assertEqual(sum_of_gcd(n), expected)

    def test_n_equals_3(self):
        """補一個小範圍案例，確認基本計算正確"""
        self.assertEqual(sum_of_gcd(3), 3)


if __name__ == "__main__":
    unittest.main()
