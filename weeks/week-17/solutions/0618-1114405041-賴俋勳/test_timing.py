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
        def sample():
            """test doc"""
            pass
        self.assertEqual(sample.__name__, "sample")
        self.assertEqual(sample.__doc__, "test doc")

    def test_repeat_records_and_average(self):
        @timeit
        def dummy():
            return 42
        result = dummy(repeat=5)
        self.assertEqual(result, 42)
        self.assertEqual(len(dummy.records), 5)
        self.assertGreater(dummy.last_elapsed, 0)
        expected = sum(dummy.records) / len(dummy.records)
        self.assertAlmostEqual(dummy.last_elapsed, expected)

    def test_repeat_below_one_raises_valueerror(self):
        @timeit
        def dummy():
            pass
        with self.assertRaises(ValueError):
            dummy(repeat=0)
        with self.assertRaises(ValueError):
            dummy(repeat=-3)


if __name__ == "__main__":
    unittest.main()
