import io
import unittest
from contextlib import redirect_stdout

from timing import timeit


class TestTimeit(unittest.TestCase):
    def test_returns_original_result_and_prints_nothing(self):
        def add(a, b):
            return a + b

        timed_add = timeit(add)

        output = io.StringIO()
        with redirect_stdout(output):
            result = timed_add(2, 5)

        self.assertEqual(result, 7)
        self.assertEqual(output.getvalue(), "")

    def test_preserves_function_metadata(self):
        def sample():
            """Original docstring."""
            return "ok"

        timed_sample = timeit(sample)

        self.assertEqual(timed_sample.__name__, "sample")
        self.assertEqual(timed_sample.__doc__, "Original docstring.")

    def test_repeat_one_records_average_elapsed_time(self):
        def sample():
            return "ok"

        timed_sample = timeit(sample, repeat=1)

        self.assertEqual(timed_sample.records, [])
        self.assertEqual(timed_sample(), "ok")

        self.assertEqual(len(timed_sample.records), 1)
        self.assertIsInstance(timed_sample.records[0], float)
        self.assertEqual(timed_sample.last_elapsed, timed_sample.records[-1])

    def test_multiple_calls_append_one_record_per_call(self):
        def sample():
            return "ok"

        timed_sample = timeit(sample, repeat=3)

        timed_sample()
        first_elapsed = timed_sample.last_elapsed
        timed_sample()

        self.assertEqual(len(timed_sample.records), 2)
        self.assertIsInstance(first_elapsed, float)
        self.assertEqual(timed_sample.last_elapsed, timed_sample.records[-1])

    def test_repeat_below_one_raises_valueerror(self):
        def sample():
            return "ok"

        with self.assertRaises(ValueError):
            timeit(sample, repeat=0)


if __name__ == "__main__":
    unittest.main()
