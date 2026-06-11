import unittest
from timing import timeit


class TestTimeit(unittest.TestCase):
    def test_returns_original_result(self):
        """測試裝飾器不會改變被裝飾函式的回傳值"""
        @timeit
        def add(a, b):
            return a + b
        
        result = add(3, 4)
        self.assertEqual(result, 7)
        self.assertGreaterEqual(add.last_elapsed, 0.0)
        self.assertEqual(len(add.records), 1)

    def test_preserves_function_metadata(self):
        """測試裝飾器保留原函式的 __name__ 和 __doc__"""
        @timeit
        def sample_function(x):
            """This is a sample function docstring."""
            return x * 2
        
        self.assertEqual(sample_function.__name__, 'sample_function')
        self.assertEqual(sample_function.__doc__, 'This is a sample function docstring.')

    def test_records_elapsed_time(self):
        """測試裝飾器正確記錄執行時間"""
        @timeit
        def slow_function():
            import time
            time.sleep(0.01)
            return "done"
        
        result = slow_function()
        self.assertEqual(result, "done")
        self.assertGreater(slow_function.last_elapsed, 0.0)
        self.assertGreaterEqual(len(slow_function.records), 1)
        self.assertGreater(slow_function.records[0], 0.0)

    def test_multiple_calls_accumulate_records(self):
        """測試多次呼叫會累積記錄"""
        @timeit
        def quick():
            return 42
        
        quick()
        quick()
        quick()
        
        self.assertEqual(len(quick.records), 3)
        self.assertGreaterEqual(quick.records[0], 0.0)
        self.assertGreaterEqual(quick.records[1], 0.0)
        self.assertGreaterEqual(quick.records[2], 0.0)


if __name__ == "__main__":
    unittest.main()