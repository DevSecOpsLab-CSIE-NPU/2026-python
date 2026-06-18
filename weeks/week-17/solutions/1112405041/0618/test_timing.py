import unittest
from timing import timeit


class TestTimeit(unittest.TestCase):

    def test_returns_original_result(self):
        @timeit
        def add(a, b):
            return a + b
        self.assertEqual(add(1, 2), 3)

    def test_preserves_function_metadata(self):
        @timeit
        def hello():
            """說嗨"""
            return "嗨"
        self.assertEqual(hello.__name__, "hello")
        self.assertEqual(hello.__doc__, "說嗨")

    def test_repeat_records_and_average(self):
        @timeit
        def do_nothing():
            return 42
        result = do_nothing()
        self.assertEqual(result, 42)
        self.assertEqual(len(do_nothing.records), 3)
        self.assertAlmostEqual(do_nothing.last_elapsed,
                               sum(do_nothing.records) / 3)

    def test_repeat_below_one_raises_valueerror(self):
        with self.assertRaises(ValueError):
            @timeit(repeat=0)
            def dummy():
                return 0


if __name__ == "__main__":
    unittest.main()
