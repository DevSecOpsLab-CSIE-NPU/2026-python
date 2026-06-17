import unittest

from timing import timeit


class TestTimeit(unittest.TestCase):
    def test_returns_original_result(self):
        call_counter = {"count": 0}

        @timeit(repeat=3)
        def add(a, b):
            call_counter["count"] += 1
            return a + b

        result = add(2, 5)

        self.assertEqual(result, 7)
        self.assertEqual(call_counter["count"], 3)

    def test_preserves_function_metadata(self):
        @timeit(repeat=1)
        def sample_func():
            """sample doc"""
            return "ok"

        self.assertEqual(sample_func.__name__, "sample_func")
        self.assertEqual(sample_func.__doc__, "sample doc")

    def test_records_each_repeat_and_average(self):
        @timeit(repeat=4)
        def work():
            total = 0
            for i in range(1000):
                total += i
            return total

        expected = sum(range(1000))
        result = work()

        self.assertEqual(result, expected)
        self.assertEqual(len(work.records), 4)
        self.assertTrue(all(isinstance(t, float) and t >= 0.0 for t in work.records))
        self.assertAlmostEqual(work.last_elapsed, sum(work.records) / 4)

    def test_repeat_one_still_records_once(self):
        @timeit(repeat=1)
        def identity(x):
            return x

        self.assertEqual(identity("A"), "A")
        self.assertEqual(len(identity.records), 1)
        self.assertIsInstance(identity.last_elapsed, float)

    def test_rejects_invalid_repeat(self):
        with self.assertRaises(ValueError):
            @timeit(repeat=0)
            def _bad():
                return 1


if __name__ == "__main__":
    unittest.main()
