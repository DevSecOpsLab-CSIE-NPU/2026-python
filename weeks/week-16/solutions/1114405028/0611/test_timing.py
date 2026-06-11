import io
import sys
import unittest

import timing


class TestTimeit(unittest.TestCase):
    def test_return_value_and_metadata(self):
        @timing.timeit
        def double(x):
            """Double a number"""
            return x * 2

        self.assertEqual(double(3), 6)
        self.assertEqual(double.__name__, 'double')
        self.assertIn('Double', double.__doc__)

    def test_last_elapsed_and_records(self):
        @timing.timeit
        def noop():
            return None

        noop()
        first = noop.last_elapsed
        self.assertIsInstance(first, float)
        noop()
        self.assertIsInstance(noop.records, list)
        self.assertEqual(len(noop.records), 2)

    def test_no_print_output(self):
        @timing.timeit
        def f():
            return 'ok'

        captured = io.StringIO()
        old_stdout = sys.stdout
        try:
            sys.stdout = captured
            f()
        finally:
            sys.stdout = old_stdout

        self.assertEqual(captured.getvalue(), '')


if __name__ == '__main__':
    unittest.main()
