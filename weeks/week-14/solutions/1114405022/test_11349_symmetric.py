"""
Unit tests for UVA 11349 — Symmetric Matrix

這個檔案包含：
- `is_center_symmetric(matrix)`：判斷單一 n×n 矩陣是否符合題目定義的「對稱矩陣」。
- `solve_from_string(s)`：從一段多組測資的輸入字串產生對應的輸出字串（方便做 I/O 測試）。

所有函式都附上繁體中文註解，並用 unittest 撰寫多個測試案例，包含題目範例與邊界情境。
"""

import unittest
from typing import List


def is_center_symmetric(matrix: List[List[int]]) -> bool:
    """
    判斷給定的方陣是否為「中心點對稱」且所有元素非負。

    條件：
    1. 所有元素 >= 0
    2. 對任意 (i, j) 有 matrix[i][j] == matrix[n-1-i][n-1-j]

    使用 0-based index 實作。
    """
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            v = matrix[i][j]
            # 檢查非負
            if v < 0:
                return False
            # 檢查關於中心的對稱性
            if v != matrix[n - 1 - i][n - 1 - j]:
                return False
    return True


def solve_from_string(s: str) -> str:
    """
    解析整段輸入字串並回傳題目的輸出（每組一行）。

    這個輔助函式可讓我們在 unit test 中用範例輸入直接比對輸出結果。
    """
    lines = [line.strip() for line in s.strip().splitlines() if line.strip()]
    if not lines:
        return ""
    t = int(lines[0])
    out_lines = []
    idx = 1
    case_no = 1
    while case_no <= t and idx < len(lines):
        # 每組的第一行形如: N = n
        header = lines[idx]
        idx += 1
        # 解析 n
        if '=' in header:
            # 允許有空白，例如 'N = 3'
            parts = header.split('=')
            n = int(parts[1].strip())
        else:
            n = int(header)

        # 讀取 n 行矩陣
        mat = []
        for _ in range(n):
            row = list(map(int, lines[idx].split()))
            mat.append(row)
            idx += 1

        ok = is_center_symmetric(mat)
        if ok:
            out_lines.append(f"Test #{case_no}: Symmetric.")
        else:
            out_lines.append(f"Test #{case_no}: Non-symmetric.")
        case_no += 1

    return "\n".join(out_lines) + ("\n" if out_lines else "")


class TestSymmetric11349(unittest.TestCase):
    """多個單元測試案例，覆蓋範例與邊界情形。"""

    def test_sample_io(self):
        """測試題目說明中的範例 I/O。"""
        inp = """
        2
        N = 3
        5 1 3
        2 0 2
        3 1 5
        N = 3
        5 1 3
        2 0 2
        0 1 5
        """
        expected = "Test #1: Symmetric.\nTest #2: Non-symmetric.\n"
        self.assertEqual(solve_from_string(inp), expected)

    def test_single_element_positive(self):
        """n=1，非負數應為 symmetric。"""
        mat = [[42]]
        self.assertTrue(is_center_symmetric(mat))

    def test_single_element_negative(self):
        """n=1，但為負數應回傳 Non-symmetric。"""
        mat = [[-1]]
        self.assertFalse(is_center_symmetric(mat))

    def test_even_dimension(self):
        """n=2 的情況，檢查對稱配對是否正確。"""
        mat = [
            [1, 2],
            [2, 1],
        ]
        # 對於 n=2，中心對稱要求 M[0][0]==M[1][1] 以及 M[0][1]==M[1][0]
        self.assertTrue(is_center_symmetric(mat))

    def test_negative_element(self):
        """若有任何元素為負，整個矩陣即為 Non-symmetric。"""
        mat = [
            [1, -2, 1],
            [3, 0, 3],
            [1, -2, 1],
        ]
        self.assertFalse(is_center_symmetric(mat))

    def test_not_center_symmetric(self):
        """尺寸與非負都符合，但對稱條件不成立的情況。"""
        mat = [
            [5, 1, 3],
            [2, 0, 2],
            [3, 9, 5],  # 中央對稱位置 (3,1) 應為 1，但這裡為 9
        ]
        self.assertFalse(is_center_symmetric(mat))


if __name__ == "__main__":
    # 直接執行這個檔案會跑所有 unittest
    unittest.main()
