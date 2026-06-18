import unittest

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
            return "ok"

        self.assertEqual(sample.__name__, "sample")
        self.assertEqual(sample.__doc__, "sample doc")

    def test_repeat_records_and_average(self):
        @timeit(repeat=4)
        def work():
            return "done"

        self.assertEqual(work(), "done")
        self.assertEqual(len(work.records), 4)
        self.assertTrue(all(isinstance(item, float) for item in work.records))
        self.assertAlmostEqual(work.last_elapsed, sum(work.records) / 4)

    def test_repeat_below_one_raises_valueerror(self):
        with self.assertRaises(ValueError):
            timeit(repeat=0)


if __name__ == "__main__":
    unittest.main()
