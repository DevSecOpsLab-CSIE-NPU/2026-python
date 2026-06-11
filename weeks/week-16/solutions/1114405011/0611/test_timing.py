import io
import unittest
from contextlib import redirect_stdout

from timing import timeit


class TestTimeit(unittest.TestCase):
    def test_returns_original_result(self):
        @timeit
        def add(a, b):
            return a + b

        self.assertEqual(add(2, 5), 7)

    def test_preserves_function_metadata(self):
        @timeit
        def sample():
            """sample doc"""
            return 42

        self.assertEqual(sample.__name__, "sample")
        self.assertEqual(sample.__doc__, "sample doc")

    def test_records_elapsed_time(self):
        @timeit
        def work(n):
            total = 0
            for i in range(n):
                total += i
            return total

        before = len(work.records)
        work(1000)
        self.assertIsInstance(work.last_elapsed, float)
        self.assertGreaterEqual(work.last_elapsed, 0.0)
        self.assertEqual(len(work.records), before + 1)
        self.assertEqual(work.records[-1], work.last_elapsed)

    def test_records_accumulate_on_multiple_calls(self):
        @timeit
        def identity(x):
            return x

        identity(1)
        identity(2)
        identity(3)

        self.assertEqual(len(identity.records), 3)
        self.assertEqual(identity(4), 4)
        self.assertEqual(len(identity.records), 4)
        self.assertEqual(identity.records[-1], identity.last_elapsed)

    def test_decorator_does_not_print(self):
        @timeit
        def noop():
            return "ok"

        stream = io.StringIO()
        with redirect_stdout(stream):
            result = noop()

        self.assertEqual(result, "ok")
        self.assertEqual(stream.getvalue(), "")


if __name__ == "__main__":
    unittest.main()
