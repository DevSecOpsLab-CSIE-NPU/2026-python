import unittest
from timing import timeit


@timeit
def _sample_fn(x, y=0):
    "sample doc"
    return x + y


class TestTimeit(unittest.TestCase):
    def test_returns_original_result(self):
        res = _sample_fn(2, y=3)
        self.assertEqual(res, 5)

    def test_preserves_function_metadata(self):
        # name and docstring preserved by functools.wraps
        self.assertEqual(_sample_fn.__name__, "_sample_fn")
        self.assertIn("sample doc", (_sample_fn.__doc__ or ""))

    def test_records_elapsed_time(self):
        # ensure records list exists and last_elapsed is float
        # call multiple times
        _sample_fn.records.clear()
        _sample_fn(1, 2)
        first = _sample_fn.last_elapsed
        self.assertIsInstance(first, float)
        self.assertGreaterEqual(len(_sample_fn.records), 1)
        _sample_fn(3, 4)
        self.assertGreater(len(_sample_fn.records), 1)


if __name__ == "__main__":
    unittest.main()
