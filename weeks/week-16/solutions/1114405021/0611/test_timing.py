import unittest

from timing import timeit


class TestTimeit(unittest.TestCase):
    def test_returns_original_result(self):
        @timeit
        def add(a, b):
            return a + b

        self.assertEqual(add(2, 3), 5)

    def test_preserves_function_metadata(self):
        @timeit
        def sample_function():
            """sample docstring"""

            return "ok"

        self.assertEqual(sample_function.__name__, "sample_function")
        self.assertEqual(sample_function.__doc__, "sample docstring")

    def test_records_elapsed_time(self):
        @timeit
        def slow_add(a, b):
            return a + b

        self.assertEqual(slow_add(1, 2), 3)
        self.assertEqual(slow_add(5, 7), 12)
        self.assertEqual(len(slow_add.records), 2)
        self.assertIsInstance(slow_add.last_elapsed, float)
        self.assertGreaterEqual(slow_add.last_elapsed, 0.0)
        self.assertGreaterEqual(slow_add.records[0], 0.0)
        self.assertGreaterEqual(slow_add.records[1], 0.0)


if __name__ == "__main__":
    unittest.main()