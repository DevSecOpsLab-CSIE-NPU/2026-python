"""
UVA 272 - TEX Quotes
Unit tests for solution_272_manual.py
"""

from __future__ import annotations

import unittest
from pathlib import Path

from solution_272_manual import convert_lines, convert_tex_quotes


class TestUVA272Manual(unittest.TestCase):

    def test_single_pair_in_one_line(self):
        """One quoted word should become ``word''."""
        out, state = convert_tex_quotes('"Hello"')
        self.assertEqual(out, "``Hello''")
        self.assertTrue(state)

    def test_sample_sentence(self):
        """Classic statement sample sentence."""
        src = '"To be or not to be," quoth the bard, "that is the question."'
        expected = "``To be or not to be,'' quoth the bard, ``that is the question.''"
        out, state = convert_tex_quotes(src)
        self.assertEqual(out, expected)
        self.assertTrue(state)

    def test_no_quotes(self):
        """Line without double quotes must remain unchanged."""
        src = "No quoted text here."
        out, state = convert_tex_quotes(src)
        self.assertEqual(out, src)
        self.assertTrue(state)

    def test_multiple_pairs_same_line(self):
        """Multiple quote pairs in one line should alternate correctly."""
        src = '"A" "B" "C"'
        out, state = convert_tex_quotes(src)
        self.assertEqual(out, "``A'' ``B'' ``C''")
        self.assertTrue(state)

    def test_consecutive_quotes_empty_content(self):
        """Two consecutive quotes represent an empty quoted string."""
        src = 'Before "" after'
        out, state = convert_tex_quotes(src)
        self.assertEqual(out, "Before ``'' after")
        self.assertTrue(state)

    def test_cross_line_state_continues(self):
        """Quote state must continue across lines in one input stream."""
        lines = [
            'He said, "Hello',
            'world" and left.',
        ]
        out = convert_lines(lines)
        self.assertEqual(out[0], "He said, ``Hello")
        self.assertEqual(out[1], "world'' and left.")

    def test_symbols_and_spaces_preserved(self):
        """Only double quote chars are replaced; others stay untouched."""
        src = 'x = 1, msg = "a+b=c?"  # ok!'
        out, state = convert_tex_quotes(src)
        self.assertEqual(out, "x = 1, msg = ``a+b=c?''  # ok!")
        self.assertTrue(state)

    def test_state_after_odd_quote_count_segment(self):
        """Odd number of quotes should flip the state."""
        out, state = convert_tex_quotes('"open only')
        self.assertEqual(out, "``open only")
        self.assertFalse(state)

    def test_resume_with_given_state(self):
        """When starting closed, first quote should be closing quotes.''"""
        out, state = convert_tex_quotes('close" then "open', is_open=False)
        self.assertEqual(out, "close'' then ``open")
        self.assertFalse(state)


def run_tests() -> bool:
    log_path = Path(__file__).resolve().parent / "test_solution_272_manual.log"

    suite = unittest.TestLoader().loadTestsFromTestCase(TestUVA272Manual)
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
