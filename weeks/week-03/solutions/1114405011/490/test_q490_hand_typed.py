"""
test_q490_hand_typed.py — 測試 q490-Hand-typed.py
"""
import importlib.util
import pathlib
import unittest

# 動態載入含連字號的檔名
_path = pathlib.Path(__file__).parent / "q490-Hand-typed.py"
_spec = importlib.util.spec_from_file_location("q490_hand_typed", _path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)

solve = _mod.solve


class TestSolve(unittest.TestCase):
    def test_basic_hello_world(self):
        self.assertEqual(solve("HELLO\nWORLD"), "WH\nOE\nRL\nLL\nDO")

    def test_single_row(self):
        self.assertEqual(solve("ABC"), "A\nB\nC")

    def test_single_column(self):
        self.assertEqual(solve("A\nB\nC"), "CBA")

    def test_empty_input(self):
        self.assertEqual(solve(""), "")

    def test_single_char(self):
        self.assertEqual(solve("Z"), "Z")

    def test_with_trailing_newline(self):
        self.assertEqual(solve("HELLO\nWORLD\n"), "WH\nOE\nRL\nLL\nDO")

    def test_unequal_rows(self):
        self.assertEqual(solve("AB\nCDE\nF"), "FCA\n DB\n E ")

    def test_numbers_only(self):
        self.assertEqual(solve("123\n456"), "41\n52\n63")

    def test_punctuation(self):
        self.assertEqual(solve("A!\nB."), "BA\n.!")

    def test_spaces_preserved(self):
        self.assertEqual(solve("A B\nC D"), "CA\n  \nDB")

    def test_output_line_count(self):
        lines = solve("HELLO\nWORLD\nPY").splitlines()
        self.assertEqual(len(lines), 5)

    def test_mixed_case(self):
        self.assertEqual(solve("aA\nbB"), "ba\nBA")

    def test_only_spaces_line(self):
        self.assertEqual(solve("   \nA"), "A \n  \n  ")


if __name__ == "__main__":
    unittest.main()
