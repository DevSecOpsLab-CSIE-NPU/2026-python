import unittest
import time


class TestTimeit(unittest.TestCase):

    def test_returns_original_result(self):
        """測試：回傳值不變"""
        from timing import timeit

        @timeit
        def add(a, b):
            return a + b

        result = add(1, 2)
        self.assertEqual(result, 3)

    def test_preserves_function_metadata(self):
        """測試：保留函式名稱和說明"""
        from timing import timeit

        @timeit
        def hello():
            """說嗨"""
            return "嗨"

        self.assertEqual(hello.__name__, "hello")
        self.assertEqual(hello.__doc__, "說嗨")

    def test_records_and_last_elapsed(self):
        """測試：records 有 repeat 次，last_elapsed 是平均"""
        from timing import timeit

        @timeit
        def sleep_a_bit():
            time.sleep(0.01)
            return "done"

        result = sleep_a_bit()

        self.assertEqual(result, "done")
        self.assertEqual(len(sleep_a_bit.records), 3)
        self.assertAlmostEqual(sleep_a_bit.last_elapsed,
                               sum(sleep_a_bit.records) / 3)

    def test_rejects_invalid_repeat(self):
        """測試：repeat < 1 要 raise ValueError"""
        from timing import timeit

        with self.assertRaises(ValueError):
            @timeit(repeat=0)
            def dummy():
                return 0


if __name__ == "__main__":
    unittest.main()
