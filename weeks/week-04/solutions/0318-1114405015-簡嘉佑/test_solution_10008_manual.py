"""
UVA 10008 - Letter Frequency Count
Unit tests for solution_10008_manual.py (count_letters)
"""

from __future__ import annotations

import unittest
from pathlib import Path

from solution_10008_manual import count_letters


class TestLetterCount10008Manual(unittest.TestCase):

    def test_basic_count(self):
        """Single line, all distinct letters, same count -> alphabetical order."""
        result = count_letters(["abc"])
        self.assertEqual(result, [("A", 1), ("B", 1), ("C", 1)])

    def test_case_insensitive(self):
        """Lowercase and uppercase count as the same letter."""
        result = count_letters(["aAbBcC"])
        self.assertEqual(result, [("A", 2), ("B", 2), ("C", 2)])

    def test_sort_by_count_desc(self):
        """Letter with higher count comes first."""
        result = count_letters(["aaab"])
        self.assertEqual(result[0], ("A", 3))
        self.assertEqual(result[1], ("B", 1))

    def test_same_count_alpha_order(self):
        """When counts are equal, sort alphabetically ascending."""
        result = count_letters(["ba"])
        letters = [r[0] for r in result]
        self.assertLess(letters.index("A"), letters.index("B"))

    def test_ignore_non_alpha(self):
        """Digits, symbols, and spaces are not counted."""
        result = count_letters(["123 !@# abc"])
        self.assertEqual(result, [("A", 1), ("B", 1), ("C", 1)])

    def test_empty_lines(self):
        """No letters in input -> empty result."""
        result = count_letters(["", "   "])
        self.assertEqual(result, [])

    def test_single_letter_only(self):
        """Only one distinct letter appears."""
        result = count_letters(["ZZZZZ"])
        self.assertEqual(result, [("Z", 5)])

    def test_multi_line_accumulate(self):
        """Counts accumulate across multiple lines."""
        result = count_letters(["aaa", "bbb", "ab"])
        self.assertEqual(result, [("A", 4), ("B", 4)])

    def test_all_26_letters(self):
        """All 26 letters appear once; output in alphabetical order."""
        result = count_letters(["abcdefghijklmnopqrstuvwxyz"])
        self.assertEqual(len(result), 26)
        for i, (letter, cnt) in enumerate(result):
            self.assertEqual(letter, chr(ord("A") + i))
            self.assertEqual(cnt, 1)

    def test_sample_input(self):
        """Mixed-case multi-line input; most frequent letter is T."""
        lines = [
            "This is a test.",
            "Count the letters.",
        ]
        result = count_letters(lines)
        self.assertEqual(result[0][0], "T")
        self.assertGreaterEqual(result[0][1], 1)


def run_tests() -> bool:
    log_path = Path(__file__).resolve().parent / "test_solution_10008_manual.log"

    suite = unittest.TestLoader().loadTestsFromTestCase(TestLetterCount10008Manual)
    with log_path.open("w", encoding="utf-8") as log_file:
        runner = unittest.TextTestRunner(stream=log_file, verbosity=2)
        result = runner.run(suite)

        log_file.write("\n")
        log_file.write("=" * 60 + "\n")
        log_file.write(f"tests_run={result.testsRun}\n")
        log_file.write(f"failures={len(result.failures)}\n")
        log_file.write(f"errors={len(result.errors)}\n")
        log_file.write(f"success={result.wasSuccessful()}\n")

    print("Tests finished.")
    print(f"Log saved to: {log_path.name}")
    return result.wasSuccessful()


if __name__ == "__main__":
    ok = run_tests()
    raise SystemExit(0 if ok else 1)
