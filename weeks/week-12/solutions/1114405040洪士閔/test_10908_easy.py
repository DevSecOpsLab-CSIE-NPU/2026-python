"""
題目 10908 - Largest Square（簡易版本的單元測試）

測試 q10908_solution_easy.py 中的函數
"""

import unittest
from q10908_solution_easy import is_valid, find_square


class TestIsValidSimple(unittest.TestCase):
    """
    測試 is_valid() 函數的有效性
    """
    
    def test_single_cell(self):
        """
        測試最小的情況：1×1 網格，邊長 1
        預期：True（單個格子總是有效的）
        """
        grid = [['a']]
        self.assertTrue(is_valid(grid, 0, 0, 1))
    
    def test_uniform_3x3(self):
        """
        測試 3×3 均勻網格，邊長 3
        預期：True（所有字元都相同）
        """
        grid = [['a', 'a', 'a'],
                ['a', 'a', 'a'],
                ['a', 'a', 'a']]
        self.assertTrue(is_valid(grid, 1, 1, 3))
    
    def test_uniform_5x5(self):
        """
        測試 5×5 均勻網格，邊長 5
        預期：True（所有字元都相同）
        """
        grid = [['x'] * 5 for _ in range(5)]
        self.assertTrue(is_valid(grid, 2, 2, 5))
    
    def test_out_of_bounds(self):
        """
        測試超出邊界的情況：3×3 網格，邊長 3，中心在 (0, 1)
        預期：False（上邊界會超出）
        """
        grid = [['a', 'a', 'a'],
                ['a', 'a', 'a'],
                ['a', 'a', 'a']]
        self.assertFalse(is_valid(grid, 0, 1, 3))
    
    def test_different_characters(self):
        """
        測試包含不同字元的 3×3 網格，邊長 3
        預期：False（位置 (2, 1) 是 'b'，不同於中心 'a'）
        """
        grid = [['a', 'a', 'a'],
                ['a', 'a', 'a'],
                ['a', 'b', 'a']]
        self.assertFalse(is_valid(grid, 1, 1, 3))


class TestFindSquareSimple(unittest.TestCase):
    """
    測試 find_square() 函數的邊長尋找
    """
    
    def test_single_cell_grid(self):
        """
        測試最小的情況：1×1 網格
        預期：邊長 1
        """
        grid = [['a']]
        result = find_square(grid, 0, 0)
        self.assertEqual(result, 1)
    
    def test_uniform_3x3_grid(self):
        """
        測試 3×3 均勻網格，中心在 (1, 1)
        預期：邊長 3（整個網格都相同）
        """
        grid = [['a', 'a', 'a'],
                ['a', 'a', 'a'],
                ['a', 'a', 'a']]
        result = find_square(grid, 1, 1)
        self.assertEqual(result, 3)
    
    def test_uniform_5x5_grid(self):
        """
        測試 5×5 均勻網格，中心在 (2, 2)
        預期：邊長 5（整個網格都相同）
        """
        grid = [['b'] * 5 for _ in range(5)]
        result = find_square(grid, 2, 2)
        self.assertEqual(result, 5)
    
    def test_corner_position(self):
        """
        測試角落位置：3×3 網格，查詢左上角 (0, 0)
        預期：邊長 1（無法向上或左擴展）
        """
        grid = [['a', 'a', 'a'],
                ['a', 'a', 'a'],
                ['a', 'a', 'a']]
        result = find_square(grid, 0, 0)
        self.assertEqual(result, 1)
    
    def test_mixed_characters(self):
        """
        測試混合字元：棋盤式網格
        預期：邊長 1（任何邊長 > 1 都會包含不同字元）
        """
        grid = [['a', 'b', 'a'],
                ['b', 'a', 'b'],
                ['a', 'b', 'a']]
        result = find_square(grid, 1, 1)
        self.assertEqual(result, 1)
    
    def test_rectangular_grid(self):
        """
        測試矩形網格（非正方形）：4×6 網格
        預期：邊長 3（min(2, 1, 3, 2) = 1 -> 邊長 = 2×1+1 = 3）
        說明：中心 (2, 3) 到下邊界距離最小為 1
        """
        grid = [['x'] * 6 for _ in range(4)]
        result = find_square(grid, 2, 3)
        self.assertEqual(result, 3)


class TestSampleCaseSimple(unittest.TestCase):
    """
    測試題目提供的範例
    """
    
    def test_official_example(self):
        """
        題目官方範例：7×10 網格，4 個查詢
        
        網格內容：
        abbbaaaaaa
        abbbaaaaaa
        abbbaaaaaa
        aaaaaaaaaa
        aaaaaaaaaa
        aaccaaaaaa
        aaccaaaaaa
        
        查詢：
        (1, 2) -> 3（以 'b' 為中心的 3×3）
        (2, 4) -> 1（'a' 周圍被 'a' 包圍但距離有限）
        (4, 6) -> 5（大面積的 'a'）
        (5, 2) -> 1（'c' 的位置很受限）
        """
        grid = [
            list("abbbaaaaaa"),
            list("abbbaaaaaa"),
            list("abbbaaaaaa"),
            list("aaaaaaaaaa"),
            list("aaaaaaaaaa"),
            list("aaccaaaaaa"),
            list("aaccaaaaaa")
        ]
        
        # 測試查詢 1
        result1 = find_square(grid, 1, 2)
        self.assertEqual(result1, 3, f"查詢 1 應該返回 3，但得到 {result1}")
        
        # 測試查詢 2
        result2 = find_square(grid, 2, 4)
        self.assertEqual(result2, 1, f"查詢 2 應該返回 1，但得到 {result2}")
        
        # 測試查詢 3
        result3 = find_square(grid, 4, 6)
        self.assertEqual(result3, 5, f"查詢 3 應該返回 5，但得到 {result3}")
        
        # 測試查詢 4
        result4 = find_square(grid, 5, 2)
        self.assertEqual(result4, 1, f"查詢 4 應該返回 1，但得到 {result4}")


class TestEdgeCasesSimple(unittest.TestCase):
    """
    測試邊界和特殊情況
    """
    
    def test_single_row(self):
        """
        測試只有一行的網格
        預期：邊長 1（無法向上或下擴展）
        """
        grid = [list("aaaaa")]
        result = find_square(grid, 0, 2)
        self.assertEqual(result, 1)
    
    def test_single_column(self):
        """
        測試只有一列的網格
        預期：邊長 1（無法向左或右擴展）
        """
        grid = [[c] for c in "aaaaa"]
        result = find_square(grid, 2, 0)
        self.assertEqual(result, 1)
    
    def test_uniform_non_square(self):
        """
        測試非正方形的矩形（4×6），全部相同字元
        預期：邊長 7（min(2, 1, 3, 2) = 1 -> 2×1+1 = 3）
        """
        grid = [['a'] * 6 for _ in range(4)]
        result = find_square(grid, 2, 3)
        self.assertEqual(result, 3)
    
    def test_larger_uniform_area(self):
        """
        測試 7×7 均勻網格
        預期：邊長 7
        """
        grid = [['c'] * 7 for _ in range(7)]
        result = find_square(grid, 3, 3)
        self.assertEqual(result, 7)


class TestPatternSimple(unittest.TestCase):
    """
    測試特殊圖案
    """
    
    def test_cross_pattern(self):
        """
        測試十字圖案：中心為 'x'，其他為 'o'
        
        o x o
        x x x
        o x o
        
        查詢中心 (1, 1)
        預期：邊長 1（十字無法形成完整正方形）
        """
        grid = [['o', 'x', 'o'],
                ['x', 'x', 'x'],
                ['o', 'x', 'o']]
        result = find_square(grid, 1, 1)
        self.assertEqual(result, 1)
    
    def test_concentric_pattern(self):
        """
        測試同心正方形：中心為 'a'，周圍是 'b'
        
        bbbbbb
        baaaab
        baaaab
        baaaab
        baaaab
        bbbbbb
        
        查詢中心 (3, 3)（'a' 區域的中心）
        預期：邊長 3（3×3 的 'a' 區域）
        """
        grid = [['b'] * 6,
                ['b', 'a', 'a', 'a', 'a', 'b'],
                ['b', 'a', 'a', 'a', 'a', 'b'],
                ['b', 'a', 'a', 'a', 'a', 'b'],
                ['b', 'a', 'a', 'a', 'a', 'b'],
                ['b'] * 6]
        result = find_square(grid, 3, 3)
        self.assertEqual(result, 3)


if __name__ == '__main__':
    # 運行所有測試
    unittest.main(verbosity=2)
