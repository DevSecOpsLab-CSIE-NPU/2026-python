import unittest
from timing import timeit


class TestTimeit(unittest.TestCase):
    def test_return_value_is_preserved(self):
        @timeit(repeat=3)
        def add(a, b):
            return a + b

        result = add(2, 3)

        self.assertEqual(result, 5)

    def test_records_length_matches_repeat(self):
        calls = []

        @timeit(repeat=3)
        def record_call():
            calls.append("called")
            return "ok"

        result = record_call()

        self.assertEqual(result, "ok")
        self.assertEqual(len(calls), 3)
        self.assertEqual(len(record_call.records), 3)

    def test_last_elapsed_exists_and_is_average_time(self):
        @timeit(repeat=2)
        def simple():
            return "done"

        simple()

        self.assertTrue(hasattr(simple, "last_elapsed"))
        self.assertIsInstance(simple.last_elapsed, float)
        self.assertGreaterEqual(simple.last_elapsed, 0)

    def test_repeat_less_than_one_raises_value_error(self):
        with self.assertRaises(ValueError):
            @timeit(repeat=0)
            def bad_function():
                return "bad"

    def test_wraps_preserves_function_metadata(self):
        @timeit(repeat=1)
        def sample_function():
            """sample docstring"""
            return "ok"

        self.assertEqual(sample_function.__name__, "sample_function")
        self.assertEqual(sample_function.__doc__, "sample docstring")


if __name__ == "__main__":
    unittest.main()