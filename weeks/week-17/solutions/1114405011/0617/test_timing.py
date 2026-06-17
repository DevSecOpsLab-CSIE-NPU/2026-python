import unittest

from timing import timeit


class TestTimeit(unittest.TestCase):
    def test_returns_original_result(self):
        calls = []

        @timeit(repeat=1)
        def add(a, b):
            calls.append((a, b))
            return a + b

        result = add(2, 5)

        self.assertEqual(result, 7)
        self.assertEqual(len(calls), 1)

    def test_preserves_function_metadata(self):
        @timeit(repeat=1)
        def greet(name):
            """Return greeting text."""

            return f"Hello, {name}"

        self.assertEqual(greet.__name__, "greet")
        self.assertEqual(greet.__doc__, "Return greeting text.")

    def test_records_each_repeat_and_average(self):
        calls = []

        @timeit(repeat=3)
        def work():
            calls.append("x")
            return "ok"

        self.assertEqual(work(), "ok")
        self.assertEqual(len(calls), 3)
        self.assertEqual(len(work.records), 3)
        first_avg = sum(work.records[-3:]) / 3
        self.assertAlmostEqual(work.last_elapsed, first_avg, places=10)

        self.assertEqual(work(), "ok")
        self.assertEqual(len(calls), 6)
        self.assertEqual(len(work.records), 6)
        second_avg = sum(work.records[-3:]) / 3
        self.assertAlmostEqual(work.last_elapsed, second_avg, places=10)

    def test_rejects_invalid_repeat(self):
        with self.assertRaises(ValueError):

            @timeit(repeat=0)
            def sample():
                return 1


if __name__ == "__main__":
    unittest.main()
