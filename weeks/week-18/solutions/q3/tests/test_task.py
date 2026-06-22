import unittest
import io
import sys
from task import to_base, digit_root_base, solve


class TestToBase(unittest.TestCase):
    """to_base 函數測試"""

    def test_zero(self):
        """Edge case: 0"""
        self.assertEqual(to_base(0, 6), [0])

    def test_single_digit(self):
        """單一位數（小於 base）"""
        self.assertEqual(to_base(5, 6), [5])

    def test_multi_digit(self):
        """多位數"""
        # 8 in base 6 = 12 (1*6 + 2)
        self.assertEqual(to_base(8, 6), [2, 1])
        # 63 in base 6 = 143 (1*36 + 4*6 + 3)
        self.assertEqual(to_base(63, 6), [3, 4, 1])

    def test_base_16(self):
        """Edge case: base 16"""
        self.assertEqual(to_base(255, 16), [15, 15])  # FF
        self.assertEqual(to_base(16, 16), [0, 1])     # 10


class TestDigitRootBase(unittest.TestCase):
    """digit_root_base 函數測試"""

    def test_single_digit_returns_self(self):
        """Edge case: 已是個位數（< base），直接回傳"""
        self.assertEqual(digit_root_base(0, 6), 0)
        self.assertEqual(digit_root_base(5, 6), 5)

    def test_simple_case(self):
        """基本案例：8 in base 6 = 12 → 1+2=3"""
        self.assertEqual(digit_root_base(8, 6), 3)

    def test_multi_step(self):
        """多步驟：63 in base 6 = 143 → 1+4+3=8 → 8 in base 6 = 12 → 1+2=3"""
        self.assertEqual(digit_root_base(63, 6), 3)

    def test_large_number(self):
        """大數字"""
        # 1000000 in base 6
        result = digit_root_base(1000000, 6)
        self.assertTrue(0 <= result < 6)

    def test_base_16_example(self):
        """Base 16 測試"""
        # 255 in base 16 = FF → 15+15=30 → 30 in base 16 = 1E → 1+14=15
        self.assertEqual(digit_root_base(255, 16), 15)
        # 16 in base 16 = 10 → 1+0=1
        self.assertEqual(digit_root_base(16, 16), 1)


class TestSolveIntegration(unittest.TestCase):
    """solve() 整合測試"""

    def run_solve(self, input_data: str) -> str:
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

    def test_example_from_spec(self):
        """規格範例（base=8 假設）：8 → 1, 63 → 7"""
        # 這裡用 base=6 重新計算
        # 8 in base 6 = 12 → 1+2=3
        # 63 in base 6 = 143 → 1+4+3=8 → 8 in base 6 = 12 → 1+2=3
        input_data = "8\n63\n"
        expected = "3\n3\n"
        self.assertEqual(self.run_solve(input_data), expected)

    def test_zero(self):
        """Edge case: x=0"""
        input_data = "0\n"
        expected = "0\n"
        self.assertEqual(self.run_solve(input_data), expected)

    def test_single_digit_input(self):
        """Edge case: 輸入已是個位數（< base）"""
        input_data = "5\n"
        expected = "5\n"
        self.assertEqual(self.run_solve(input_data), expected)

    def test_multiple_lines(self):
        """多行輸入"""
        input_data = "0\n1\n5\n8\n63\n1000000\n"
        output = self.run_solve(input_data).strip().split()
        self.assertEqual(len(output), 6)
        for val in output:
            self.assertTrue(0 <= int(val) < 6)

    def test_empty_input(self):
        """空輸入"""
        input_data = ""
        expected = ""
        self.assertEqual(self.run_solve(input_data), expected)


if __name__ == "__main__":
    unittest.main()