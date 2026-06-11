import unittest
from timing import timeit


class TestTimeit(unittest.TestCase):

    def test_never_called_records_empty(self):
        @timeit
        def f():
            return 42

        self.assertIsNone(f.last_elapsed)
        self.assertEqual(f.records, [])

    def test_called_once_records_one(self):
        @timeit
        def f():
            return 42

        val = f()
        self.assertEqual(val, 42)
        self.assertEqual(len(f.records), 1)
        self.assertIsInstance(f.last_elapsed, float)
        self.assertEqual(f.last_elapsed, f.records[0])

    def test_return_value_preserved_none(self):
        @timeit
        def f():
            return None

        val = f()
        self.assertIsNone(val)

    def test_return_value_preserved_string(self):
        @timeit
        def f():
            return "hello"

        self.assertEqual(f(), "hello")

    def test_wraps_preserves_metadata(self):
        @timeit
        def f():
            """docstring"""
            return 1

        self.assertEqual(f.__name__, "f")
        self.assertEqual(f.__doc__, "docstring")


if __name__ == "__main__":
    unittest.main()
