from __future__ import annotations

import pathlib
import sys
import unittest


BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from task1_sequence_clean import dedupe_keep_order, solve  # noqa: E402


class TestTask1SequenceClean(unittest.TestCase):
    def test_sample_case(self) -> None:
        raw_input = "5 3 5 2 9 2 8 3 1\n"
        expected = (
            "dedupe: 5 3 2 9 8 1\n"
            "asc: 1 2 2 3 3 5 5 8 9\n"
            "desc: 9 8 5 5 3 3 2 2 1\n"
            "evens: 2 2 8"
        )
        self.assertEqual(solve(raw_input), expected)

    def test_empty_input(self) -> None:
        expected = "dedupe:\nasc:\ndesc:\nevens:"
        self.assertEqual(solve(""), expected)

    def test_dedupe_keeps_first_order(self) -> None:
        nums = [4, 1, 4, 2, 1, 3]
        self.assertEqual(dedupe_keep_order(nums), [4, 1, 2, 3])


if __name__ == "__main__":
    unittest.main()