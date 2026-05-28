"""r03_profile.py 的單元測試。"""

import unittest

import r03_profile as r03


class TestR03Profile(unittest.TestCase):
    """驗證 timed、timeit、cProfile 三種測量方式。"""

    def test_sum_of_squares(self):
        value, elapsed = r03.sum_of_squares(10)
        self.assertEqual(value, sum(i * i for i in range(10)))
        self.assertGreaterEqual(elapsed, 0.0)

    def test_bench_timeit(self):
        result = r03.bench_timeit(n=1000, number=20)
        self.assertIn("genexp", result)
        self.assertIn("map_lambda", result)
        self.assertGreaterEqual(result["genexp"], 0.0)
        self.assertGreaterEqual(result["map_lambda"], 0.0)

    def test_bench_cprofile(self):
        text = r03.bench_cprofile(limit=500, top_n=3)
        self.assertIn("function calls", text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
