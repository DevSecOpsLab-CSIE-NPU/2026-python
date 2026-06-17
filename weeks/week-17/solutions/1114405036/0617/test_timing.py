import unittest

from timing import timeit


class TestTimeit(unittest.TestCase):
    def test_returns_original_result(self):
        """規格 1:回傳值不變。"""

        @timeit
        def add(a, b):
            return a + b

        self.assertEqual(add(2, 3), 5)
        # 連續呼叫也要維持正確回傳值
        self.assertEqual(add(10, -4), 6)

    def test_preserves_function_metadata(self):
        """規格 2:functools.wraps 保留 __name__ / __doc__。"""

        @timeit
        def greet():
            """say hi"""
            return "hi"

        self.assertEqual(greet.__name__, "greet")
        self.assertEqual(greet.__doc__, "say hi")

    def test_records_each_repeat_and_average(self):
        """規格 3:每次呼叫實際跑 repeat 次,records 累積、last_elapsed 為平均。"""

        @timeit  # 預設 repeat=3
        def noop():
            return 42

        result = noop()
        self.assertEqual(result, 42)
        # 預設 repeat=3 → 本次 append 3 筆
        self.assertEqual(len(noop.records), 3)
        # 每筆都是非負 float 秒
        for elapsed in noop.records:
            self.assertIsInstance(elapsed, float)
            self.assertGreaterEqual(elapsed, 0.0)
        # last_elapsed = 本次 repeat 的平均
        expected_avg = sum(noop.records) / 3
        self.assertAlmostEqual(noop.last_elapsed, expected_avg)

        # 再呼叫一次:records 持續累積(3 + 3 = 6),last_elapsed 只反映本次平均
        noop()
        self.assertEqual(len(noop.records), 6)
        last_three = noop.records[-3:]
        self.assertAlmostEqual(noop.last_elapsed, sum(last_three) / 3)

    def test_repeat_one_runs_function_once_per_call(self):
        """edge case:repeat=1 時每次呼叫只跑一次,副作用不被多算。"""

        calls = []

        @timeit(repeat=1)
        def with_side_effect():
            calls.append(1)
            return len(calls)

        with_side_effect()
        self.assertEqual(len(calls), 1)
        self.assertEqual(len(with_side_effect.records), 1)
        with_side_effect()
        self.assertEqual(len(calls), 2)
        self.assertEqual(len(with_side_effect.records), 2)

    def test_default_repeat_runs_function_three_times(self):
        """edge case:預設 repeat=3 時,有副作用的函式會被跑 3 次。"""

        calls = []

        @timeit
        def with_side_effect():
            calls.append(1)
            return "done"

        with_side_effect()
        self.assertEqual(len(calls), 3)

    def test_rejects_invalid_repeat(self):
        """規格 5:repeat < 1 應 raise ValueError(不准 assert)。"""

        with self.assertRaises(ValueError):

            @timeit(repeat=0)
            def f():
                return 1

        with self.assertRaises(ValueError):

            @timeit(repeat=-3)
            def g():
                return 1


if __name__ == "__main__":
    unittest.main()