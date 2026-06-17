"""0617 任務一 — timeit 裝飾器測試"""

import unittest
from functools import wraps

# from timing import timeit  # 完成 timing.py 後解除註解


class TestTimeit(unittest.TestCase):
    def test_returns_original_result(self):
        """被裝飾函式的回傳值不變"""

        @timeit
        def add(a, b):
            return a + b

        self.assertEqual(add(3, 5), 8)
        self.assertEqual(add(-1, 1), 0)

    def test_preserves_function_metadata(self):
        """用 functools.wraps 保留 __name__ / __doc__"""

        @timeit
        def my_func():
            """docstring"""
            return 42

        self.assertEqual(my_func.__name__, "my_func")
        self.assertEqual(my_func.__doc__, "docstring")

    def test_records_each_repeat_and_average(self):
        """每次呼叫跑 repeat 次，f.records 記錄每次耗時，f.last_elapsed 為平均"""

        @timeit(repeat=3)
        def simple():
            return 1

        simple()
        self.assertEqual(len(simple.records), 3)
        self.assertIsInstance(simple.last_elapsed, float)
        self.assertAlmostEqual(simple.last_elapsed, sum(simple.records) / 3)

    def test_repeat_default_is_3(self):
        """預設 repeat=3"""

        @timeit
        def simple():
            return 1

        simple()
        self.assertEqual(len(simple.records), 3)

    def test_repeat_1_produces_single_record(self):
        """repeat=1 時 records 長度為 1"""

        @timeit(repeat=1)
        def simple():
            return 1

        simple()
        self.assertEqual(len(simple.records), 1)
        self.assertAlmostEqual(simple.last_elapsed, simple.records[0])

    def test_repeat_float_2_5_uses_int(self):
        """repeat=2.5 時以 int(2.5)=2 次執行"""

        @timeit(repeat=2.5)
        def simple():
            return 1

        simple()
        self.assertEqual(len(simple.records), 2)

    def test_rejects_invalid_repeat(self):
        """repeat < 1 → raise ValueError（不准 assert）"""
        for invalid in (0, -1, -100):
            with self.subTest(repeat=invalid):
                with self.assertRaises(ValueError):

                    @timeit(repeat=invalid)
                    def f():
                        pass

    def test_no_print_in_decorator(self):
        """裝飾器內不准 print"""
        import io
        import sys
        from unittest.mock import patch

        @timeit
        def f():
            return 1

        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            f()
        self.assertEqual(mock_stdout.getvalue(), "")


if __name__ == "__main__":
    unittest.main()
