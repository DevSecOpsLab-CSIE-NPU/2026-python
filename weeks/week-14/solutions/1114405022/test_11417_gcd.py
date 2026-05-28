"""
Unit tests for UVA 11417 — GCD

這個檔案提供：
- `gcd_sum(n)`：用暴力法計算 1..n 所有成對數字的 gcd 總和。
- `solve_from_string(s)`：把完整輸入字串轉成題目輸出格式，方便做 I/O 測試。

因為題目的 n 最大只有 500，所以暴力法非常適合拿來當單元測試的參考答案。
"""

import math
import unittest


def gcd_sum(n: int) -> int:
    """計算 sum(gcd(i, j)) for 1 <= i < j <= n。"""
    total = 0
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            total += math.gcd(i, j)
    return total


def solve_from_string(s: str) -> str:
    """模擬題目的標準輸入與標準輸出。"""
    out = []
    for line in s.strip().splitlines():
        line = line.strip()
        if not line:
            continue
        n = int(line)
        if n == 0:
            break
        out.append(str(gcd_sum(n)))
    return "\n".join(out) + ("\n" if out else "")


class TestGCD11417(unittest.TestCase):
    """針對 11417 的輸入輸出與邊界情況做測試。"""

    def test_sample_cases(self):
        """題目提供的範例。"""
        inp = """
        10
        100
        500
        0
        """
        expected = """67
13015
442011
"""
        self.assertEqual(solve_from_string(inp), expected)

    def test_smallest_valid_n(self):
        """N = 2 時只有一組 (1, 2)，gcd 為 1。"""
        self.assertEqual(gcd_sum(2), 1)

    def test_n_three(self):
        """N = 3 的情況可手算驗證。"""
        # gcd(1,2)=1, gcd(1,3)=1, gcd(2,3)=1
        self.assertEqual(gcd_sum(3), 3)

    def test_zero_termination(self):
        """輸入遇到 0 時要停止，不應再產生輸出。"""
        inp = """
        2
        0
        10
        """
        expected = "1\n"
        self.assertEqual(solve_from_string(inp), expected)

    def test_empty_input(self):
        """空輸入時回傳空字串。"""
        self.assertEqual(solve_from_string(""), "")


if __name__ == "__main__":
    # 直接執行此檔時，會自動跑所有 unittest。
    unittest.main()
