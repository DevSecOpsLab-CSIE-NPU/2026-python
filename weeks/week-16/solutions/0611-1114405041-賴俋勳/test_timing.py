import time
import unittest

from timing import timeit


class TestTimeit(unittest.TestCase):
    def test_return_value_and_records(self):
        @timeit
        def add(a, b):
            time.sleep(0.001)
            return a + b

        self.assertEqual(add(2, 3), 5)
        self.assertIsInstance(add.last_elapsed, float)
        self.assertEqual(len(add.records), 1)

    def test_records_accumulate(self):
        @timeit
        def ping():
            return "pong"

        ping()
        ping()
        self.assertEqual(len(ping.records), 2)

    def test_wraps_keeps_name_and_doc(self):
        @timeit
        def sample():
            "demo"
            return 1

        self.assertEqual(sample.__name__, "sample")
        self.assertEqual(sample.__doc__, "demo")


if __name__ == "__main__":
    unittest.main()
