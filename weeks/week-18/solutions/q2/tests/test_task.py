import unittest
import io
import sys
from contextlib import redirect_stdout, redirect_stderr
from task import encrypt_line, solve


class TestEncryptLine(unittest.TestCase):
    """encrypt_line 函數測試"""

    def test_normal_mixed_case(self):
        """一般情況：大小寫混合、含標點"""
        # shift=6: a->g, b->h, ..., z->f, A->G, Z->F
        self.assertEqual(encrypt_line("Hello, World!", 6), "Nkrru, Cuxrj!")
        self.assertEqual(encrypt_line("abc XYZ", 6), "ghi DEF")

    def test_wrap_around(self):
        """Edge case: 字母循環（z 往後位移回到開頭）"""
        # shift=6: z->f, Z->F
        self.assertEqual(encrypt_line("z", 6), "f")
        self.assertEqual(encrypt_line("Z", 6), "F")
        self.assertEqual(encrypt_line("xyz", 6), "def")
        self.assertEqual(encrypt_line("XYZ", 6), "DEF")

    def test_non_alphabetic_unchanged(self):
        """Edge case: 非英文字母（數字、空白、標點）保持不變"""
        self.assertEqual(encrypt_line("123!@#", 6), "123!@#")
        self.assertEqual(encrypt_line("a1b2c3", 6), "g1h2i3")
        self.assertEqual(encrypt_line("   ", 6), "   ")
        self.assertEqual(encrypt_line("", 6), "")

    def test_shift_zero(self):
        """Edge case: shift=0，字串不變"""
        self.assertEqual(encrypt_line("Hello", 0), "Hello")
        self.assertEqual(encrypt_line("abcXYZ", 0), "abcXYZ")

    def test_shift_26_equals_zero(self):
        """Edge case: shift=26 等同 shift=0"""
        self.assertEqual(encrypt_line("Hello", 26), "Hello")
        self.assertEqual(encrypt_line("xyz", 26), "xyz")

    def test_shift_negative(self):
        """Edge case: 負數位移（向左位移）"""
        # shift=-1 等同 shift=25
        self.assertEqual(encrypt_line("b", -1), "a")
        self.assertEqual(encrypt_line("a", -1), "z")


class TestSolveIntegration(unittest.TestCase):
    """solve() 整合測試"""

    def run_solve(self, input_data: str) -> str:
        """執行 solve() 並捕獲輸出"""
        stdin = sys.stdin
        stdout = sys.stdout
        sys.stdin = io.StringIO(input_data)
        sys.stdout = io.StringIO()
        try:
            solve()
            return sys.stdout.getvalue()
        finally:
            sys.stdin = stdin
            sys.stdout = stdout

    def test_single_line(self):
        """單行輸入"""
        input_data = "Hello"
        # shift=6: H->N, e->k, l->r, l->r, o->u
        expected = "Nkrru\n"
        self.assertEqual(self.run_solve(input_data), expected)

    def test_multiple_lines(self):
        """多行輸入"""
        input_data = "Hello\nWorld\n"
        expected = "Nkrru\nCuxrj\n"
        self.assertEqual(self.run_solve(input_data), expected)

    def test_empty_input(self):
        """空輸入"""
        input_data = ""
        expected = ""
        self.assertEqual(self.run_solve(input_data), expected)

    def test_with_numbers_and_punctuation(self):
        """含數字與標點"""
        input_data = "abc123!@#"
        # a->g, b->h, c->i, 123!@# 不變
        expected = "ghi123!@#\n"
        self.assertEqual(self.run_solve(input_data), expected)


if __name__ == "__main__":
    unittest.main()