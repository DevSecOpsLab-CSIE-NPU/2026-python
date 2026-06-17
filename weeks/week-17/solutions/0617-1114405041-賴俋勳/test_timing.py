import unittest
from timing import timeit


class TestTimeit(unittest.TestCase):
    def test_returns_original_result(self):
        @timeit
        def add(a, b):
            return a + b
        self.assertEqual(add(3, 5), 8)
        self.assertEqual(add(-1, 1), 0)

    def test_preserves_function_metadata(self):
        @timeit
        def sample_function():
            """docstring test"""
            pass
        self.assertEqual(sample_function.__name__, "sample_function")
        self.assertEqual(sample_function.__doc__, "docstring test")

    def test_records_each_repeat_and_average(self):
        @timeit
        def dummy():
            return 42
        result = dummy(repeat=5)
        self.assertEqual(result, 42)
        self.assertEqual(len(dummy.records), 5)
        self.assertGreater(dummy.last_elapsed, 0)
        expected_avg = sum(dummy.records) / len(dummy.records)
        self.assertAlmostEqual(dummy.last_elapsed, expected_avg)

    def test_repeat_one_records_single_value(self):
        @timeit
        def dummy():
            return 0
        dummy(repeat=1)
        self.assertEqual(len(dummy.records), 1)

    def test_rejects_invalid_repeat(self):
        @timeit
        def dummy():
            pass
        with self.assertRaises(ValueError):
            dummy(repeat=0)
        with self.assertRaises(ValueError):
            dummy(repeat=-3)


if __name__ == "__main__":
    unittest.main()
