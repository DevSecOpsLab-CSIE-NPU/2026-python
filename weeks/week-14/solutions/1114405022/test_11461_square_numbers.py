"""
Unit tests for UVA 11461 — Square Numbers

這個檔案包含：
- `count_squares(a, b)`：計算閉區間 [a, b] 中完全平方數的個數。
- `solve_from_string(s)`：模擬題目的輸入輸出格式，方便做 I/O 測試。

題目範圍只有到 100000，所以這裡用簡單、好懂的方式寫參考答案。
"""

import math
import unittest


def count_squares(a: int, b: int) -> int:
    """直接枚舉平方數，計算落在 [a, b] 的數量。"""
    total = 0
    root = 1
    while root * root <= b:
        square = root * root
        if a <= square <= b:
            total += 1
        root += 1
    return total


def solve_from_string(s: str) -> str:
    """把整段輸入字串轉成題目輸出，遇到 0 0 就停止。"""
    outputs = []
    for line in s.strip().splitlines():
        line = line.strip()
        if not line:
            continue
        a, b = map(int, line.split())
        if a == 0 and b == 0:
            break
        outputs.append(str(count_squares(a, b)))
    return "\n".join(outputs) + ("\n" if outputs else "")


class TestSquareNumbers11461(unittest.TestCase):
    """針對 11461 的範例與邊界情況測試。"""

    def test_sample_cases(self):
        """題目提供的範例輸入與輸出。"""
        inp = """
        1 4
        1 10
        1 100000
        0 0
        """
        expected = """2
3
316
"""
        self.assertEqual(solve_from_string(inp), expected)

    def test_single_square(self):
        """只有一個完全平方數時。"""
        self.assertEqual(count_squares(16, 16), 1)

    def test_no_square(self):
        """區間內沒有完全平方數時。"""
        self.assertEqual(count_squares(2, 3), 0)

    def test_range_with_multiple_squares(self):
        """檢查一般區間計算是否正確。"""
        # 4, 9, 16, 25, 36, 49, 64, 81, 100 共 9 個
        self.assertEqual(count_squares(4, 100), 9)

    def test_zero_termination(self):
        """遇到 0 0 之後應停止，不再產生輸出。"""
        inp = """
        1 1
        0 0
        4 4
        """
        expected = "1\n"
        self.assertEqual(solve_from_string(inp), expected)

    def test_empty_input(self):
        """空輸入時回傳空字串。"""
        self.assertEqual(solve_from_string(""), "")


if __name__ == "__main__":
    # 直接執行此檔會跑所有 unittest。
    unittest.main()
