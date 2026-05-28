"""
測試程式：UVA 11349 — Symmetric Matrix
用 subprocess 直接執行手打版 11349.py，驗證標準輸出是否正確
"""
import unittest
import subprocess
import sys
import os

# 手打版程式的路徑
SCRIPT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '11349.py')


def run(input_text):
    """執行手打版程式，傳入模擬標準輸入，回傳標準輸出（已去除首尾空白）"""
    result = subprocess.run(
        [sys.executable, SCRIPT],
        input=input_text,
        capture_output=True,
        text=True
    )
    return result.stdout.strip()


class TestSymmetricMatrix(unittest.TestCase):

    def test_example_from_problem(self):
        """題目範例：第1組對稱、第2組非對稱"""
        inp = (
            "2\n"
            "N = 3\n5 1 3\n2 0 2\n3 1 5\n"
            "N = 3\n5 1 3\n2 0 2\n0 1 5\n"
        )
        expected = "Test #1: Symmetric.\nTest #2: Non-symmetric."
        self.assertEqual(run(inp), expected)

    def test_negative_element(self):
        """含負數元素 → 非對稱"""
        inp = "1\nN = 2\n-1 0\n0 -1\n"
        self.assertEqual(run(inp), "Test #1: Non-symmetric.")

    def test_1x1_symmetric(self):
        """1×1 非負矩陣 → 對稱"""
        inp = "1\nN = 1\n42\n"
        self.assertEqual(run(inp), "Test #1: Symmetric.")

    def test_1x1_negative(self):
        """1×1 負數矩陣 → 非對稱"""
        inp = "1\nN = 1\n-5\n"
        self.assertEqual(run(inp), "Test #1: Non-symmetric.")

    def test_2x2_symmetric(self):
        """2×2 滿足中心對稱"""
        inp = "1\nN = 2\n1 2\n2 1\n"
        self.assertEqual(run(inp), "Test #1: Symmetric.")

    def test_2x2_non_symmetric(self):
        """2×2 不滿足中心對稱"""
        inp = "1\nN = 2\n1 2\n3 1\n"
        self.assertEqual(run(inp), "Test #1: Non-symmetric.")

    def test_all_zeros(self):
        """全零矩陣 → 對稱"""
        inp = "1\nN = 3\n0 0 0\n0 0 0\n0 0 0\n"
        self.assertEqual(run(inp), "Test #1: Symmetric.")

    def test_multiple_cases_numbering(self):
        """多組測試，輸出編號從 1 遞增"""
        inp = "3\nN = 1\n1\nN = 1\n2\nN = 1\n-1\n"
        expected = "Test #1: Symmetric.\nTest #2: Symmetric.\nTest #3: Non-symmetric."
        self.assertEqual(run(inp), expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
