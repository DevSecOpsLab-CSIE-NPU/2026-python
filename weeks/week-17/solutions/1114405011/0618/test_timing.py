"""Stage 1 - timeit decorator tests."""

import unittest
from unittest.mock import patch

from timing import timeit


def sample(value):
    """sample docstring"""
    return value + 1


class TestTimeit(unittest.TestCase):
    def test_returns_original_result(self):
        with patch("timing.perf_counter", side_effect=[0, 1, 1, 3, 3, 6]), patch(
            "builtins.print"
        ) as mock_print:
            decorated = timeit()(sample)
            result = decorated(41)

        self.assertEqual(result, 42)
        self.assertEqual(decorated.records, [1, 2, 3])
        self.assertAlmostEqual(decorated.last_elapsed, 2.0)
        mock_print.assert_not_called()

    def test_preserves_function_metadata(self):
        decorated = timeit(repeat=1)(sample)

        self.assertEqual(decorated.__name__, sample.__name__)
        self.assertEqual(decorated.__doc__, sample.__doc__)

    def test_repeat_records_and_average(self):
        with patch("timing.perf_counter", side_effect=[10, 11, 11, 14, 14, 20]):
            decorated = timeit()(sample)
            decorated(0)

        self.assertEqual(decorated.records, [1, 3, 6])
        self.assertAlmostEqual(decorated.last_elapsed, 10 / 3)

    def test_repeat_below_one_raises_valueerror(self):
        with self.assertRaises(ValueError):
            timeit(repeat=0)


if __name__ == "__main__":
    unittest.main()