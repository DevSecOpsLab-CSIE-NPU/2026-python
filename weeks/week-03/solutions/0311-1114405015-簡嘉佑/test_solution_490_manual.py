"""
UVA 490 - Rotating Sentences (manual version) unit tests
"""

from __future__ import annotations

import unittest
from pathlib import Path

from solution_490_manual import out, rot


class TestUVA490Manual(unittest.TestCase):

    def test_two_lines_same_length(self):
        src = ["HELLO", "WORLD"]
        self.assertEqual(rot(src), ["WH", "OE", "RL", "LL", "DO"])

    def test_ragged_lines_need_padding(self):
        src = ["ABC", "DE"]
        self.assertEqual(rot(src), ["DA", "EB", " C"])

    def test_single_line(self):
        src = ["ABC"]
        self.assertEqual(rot(src), ["A", "B", "C"])

    def test_empty_input(self):
        self.assertEqual(rot([]), [])

    def test_lines_with_spaces(self):
        src = ["A B", "C D"]
        self.assertEqual(rot(src), ["CA", "  ", "DB"])

    def test_with_punctuation_and_digits(self):
        src = ["A1!", "b2?"]
        self.assertEqual(rot(src), ["bA", "21", "?!"])

    def test_three_lines_varied_lengths(self):
        src = ["12", "345", "6"]
        self.assertEqual(rot(src), ["631", " 42", " 5 "])

    def test_output_join_format(self):
        lines = ["AB", "CD", "EF"]
        rotated = rot(lines)
        self.assertEqual(out(rotated), "ECA\nFDB")

    def test_original_data_not_modified(self):
        src = ["AB", "C"]
        snapshot = src.copy()
        _ = rot(src)
        self.assertEqual(src, snapshot)


def run_tests() -> bool:
    log_path = Path(__file__).resolve().parent / "test_solution_490_manual.log"

    suite = unittest.TestLoader().loadTestsFromTestCase(TestUVA490Manual)
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
