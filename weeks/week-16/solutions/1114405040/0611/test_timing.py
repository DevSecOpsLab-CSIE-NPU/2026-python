import io
import unittest
from contextlib import redirect_stdout

from timing import timeit


class TestTimeit(unittest.TestCase):
    def test_returns_original_result(self):
        @timeit
        def add(left, right):
            return left + right

        self.assertEqual(add(2, 5), 7)

    def test_preserves_function_metadata(self):
        @timeit
        def sample():
            """sample doc"""
            return "ok"

        self.assertEqual(sample.__name__, "sample")
        self.assertEqual(sample.__doc__, "sample doc")

    def test_records_elapsed_time(self):
        @timeit
        def sample():
            return "ok"

        buffer = io.StringIO()
        with redirect_stdout(buffer):
            sample()
            sample()

        self.assertEqual(buffer.getvalue(), "")
        self.assertIsInstance(sample.last_elapsed, float)
        self.assertEqual(len(sample.records), 2)
        self.assertTrue(all(value >= 0 for value in sample.records))


if __name__ == "__main__":
    unittest.main()
