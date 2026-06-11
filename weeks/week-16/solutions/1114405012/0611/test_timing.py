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
        def sample():
            return "done"

        sample()
        sample()
        self.assertIsInstance(sample.last_elapsed, float)
        self.assertEqual(len(sample.records), 2)
        self.assertGreaterEqual(sample.last_elapsed, 0.0)

    def test_no_print_side_effect(self):
        @timeit
        def sample():
            return 1

        self.assertEqual(sample(), 1)


if __name__ == "__main__":
    unittest.main()
