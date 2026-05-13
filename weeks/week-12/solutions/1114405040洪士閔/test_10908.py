"""
題目 10908 - Largest Square 的 Unit Test 程式

本程式使用 Python 的 unittest 框架來測試 find_largest_square() 函數。
測試涵蓋正常情況、邊界情況和異常情況。

測試分類：
1. TestIsValidSquare - 檢驗正方形邊界和字元匹配
2. TestFindLargestSquare - 測試最大正方形尋找
3. TestSolveLargestSquare - 整合測試
4. TestEdgeCases - 邊界情況測試
"""

import unittest
from q10908_solution import is_valid_square, find_largest_square, solve_largest_square


class TestIsValidSquare(unittest.TestCase):
    """
    測試 is_valid_square 函數的單元測試類別。
    驗證正方形的邊界檢查和字元相同性檢查。
    """
    
    def test_single_cell_valid(self):
        """
        測試邊長為 1 的正方形（單個格子）。
        輸入：grid = [['a']], 查詢點 (0, 0), 邊長 1
        預期：True（單個格子總是有效的）
        """
        grid = [['a']]
        self.assertTrue(is_valid_square(grid, 0, 0, 1))
    
    def test_3x3_square_all_same(self):
        """
        測試邊長為 3 的正方形，所有字元相同。
        輸入：3x3 網格全為 'a'，中心 (1, 1)，邊長 3
        預期：True（所有字元相同）
        """
        grid = [['a', 'a', 'a'],
                ['a', 'a', 'a'],
                ['a', 'a', 'a']]
        self.assertTrue(is_valid_square(grid, 1, 1, 3))
    
    def test_boundary_out_of_bounds_top(self):
        """
        測試超出邊界的情況（頂部）。
        輸入：3x3 網格，查詢點 (0, 1)，邊長 3
        預期：False（超出邊界）
        """
        grid = [['a', 'a', 'a'],
                ['a', 'a', 'a'],
                ['a', 'a', 'a']]
        self.assertFalse(is_valid_square(grid, 0, 1, 3))
    
    def test_3x3_square_with_different_char(self):
        """
        測試邊長為 3 的正方形，有不同的字元。
        輸入：3x3 網格，中心為 'a' 但位置 (2,1) 為 'b'
        預期：False（存在不同的字元）
        """
        grid = [['a', 'a', 'a'],
                ['a', 'a', 'a'],
                ['a', 'b', 'a']]
        self.assertFalse(is_valid_square(grid, 1, 1, 3))
    
    def test_5x5_square_center(self):
        """
        測試邊長為 5 的正方形，中心在 (2, 2)。
        輸入：5x5 網格全為 'x'
        預期：True（所有字元相同）
        """
        grid = [['x', 'x', 'x', 'x', 'x'],
                ['x', 'x', 'x', 'x', 'x'],
                ['x', 'x', 'x', 'x', 'x'],
                ['x', 'x', 'x', 'x', 'x'],
                ['x', 'x', 'x', 'x', 'x']]
        self.assertTrue(is_valid_square(grid, 2, 2, 5))


class TestFindLargestSquare(unittest.TestCase):
    """
    測試 find_largest_square 函數的單元測試類別。
    驗證找到最大正方形的邊長。
    """
    
    def test_single_cell_grid(self):
        """
        測試最簡單的情況：1x1 網格。
        輸入：grid = [['a']], 查詢點 (0, 0)
        預期：邊長 = 1
        """
        grid = [['a']]
        result = find_largest_square(grid, 0, 0)
        self.assertEqual(result, 1)
    
    def test_uniform_3x3_grid(self):
        """
        測試 3x3 均勻網格（所有字元相同）。
        輸入：3x3 全 'a' 網格，查詢中心點 (1, 1)
        預期：邊長 = 3
        """
        grid = [['a', 'a', 'a'],
                ['a', 'a', 'a'],
                ['a', 'a', 'a']]
        result = find_largest_square(grid, 1, 1)
        self.assertEqual(result, 3)
    
    def test_uniform_5x5_grid(self):
        """
        測試 5x5 均勻網格（所有字元相同）。
        輸入：5x5 全 'b' 網格，查詢中心點 (2, 2)
        預期：邊長 = 5
        """
        grid = [['b'] * 5 for _ in range(5)]
        result = find_largest_square(grid, 2, 2)
        self.assertEqual(result, 5)
    
    def test_corner_position(self):
        """
        測試角落位置的查詢。
        輸入：3x3 網格，查詢左上角 (0, 0)
        預期：邊長 = 1（角落只能有邊長為 1 的正方形）
        """
        grid = [['c', 'c', 'c'],
                ['c', 'c', 'c'],
                ['c', 'c', 'c']]
        result = find_largest_square(grid, 0, 0)
        self.assertEqual(result, 1)
    
    def test_edge_position(self):
        """
        測試邊界位置（非角落）的查詢。
        輸入：5x5 網格，查詢上邊中心 (0, 2)
        預期：邊長 = 1
        """
        grid = [['d'] * 5 for _ in range(5)]
        result = find_largest_square(grid, 0, 2)
        self.assertEqual(result, 1)
    
    def test_different_chars_mixed(self):
        """
        測試混合不同字元的網格。
        輸入：
        a b a
        b a b
        a b a
        查詢中心點 (1, 1)，中心是 'a'，周圍都是 'b'
        預期：邊長 = 1
        """
        grid = [['a', 'b', 'a'],
                ['b', 'a', 'b'],
                ['a', 'b', 'a']]
        result = find_largest_square(grid, 1, 1)
        self.assertEqual(result, 1)
    
    def test_square_with_boundary(self):
        """
        測試正方形受邊界限制的情況。
        輸入：7x7 全 'a' 網格，查詢點 (1, 1)
        預期：邊長 = 3（由於距離邊界限制）
        """
        grid = [['a'] * 7 for _ in range(7)]
        result = find_largest_square(grid, 1, 1)
        self.assertEqual(result, 3)
    
    def test_large_uniform_grid(self):
        """
        測試較大的均勻網格。
        輸入：11x11 全 'z' 網格，查詢中心點 (5, 5)
        預期：邊長 = 11
        """
        grid = [['z'] * 11 for _ in range(11)]
        result = find_largest_square(grid, 5, 5)
        self.assertEqual(result, 11)


class TestSolveLargestSquare(unittest.TestCase):
    """
    測試 solve_largest_square 函數的整合測試類別。
    驗證完整的問題解決流程。
    """
    
    def test_sample_case_from_problem(self):
        """
        測試題目提供的範例。
        給定：
        7x10 網格，4 個查詢
        網格內容：
        abbbaaaaaa
        abbbaaaaaa
        abbbaaaaaa
        aaaaaaaaaa
        aaaaaaaaaa
        aaccaaaaaa
        aaccaaaaaa
        
        查詢和預期結果：
        (1, 2) -> 3
        (2, 4) -> 1
        (4, 6) -> 5
        (5, 2) -> 1
        """
        grid = [
            'abbbaaaaaa',
            'abbbaaaaaa',
            'abbbaaaaaa',
            'aaaaaaaaaa',
            'aaaaaaaaaa',
            'aaccaaaaaa',
            'aaccaaaaaa'
        ]
        
        queries = [(1, 2), (2, 4), (4, 6), (5, 2)]
        results = solve_largest_square(7, 10, 4, grid, queries)
        
        # 驗證每個查詢的結果
        self.assertEqual(results[0], 3, "查詢 1：(1, 2) 應返回 3")
        self.assertEqual(results[1], 1, "查詢 2：(2, 4) 應返回 1")
        self.assertEqual(results[2], 5, "查詢 3：(4, 6) 應返回 5")
        self.assertEqual(results[3], 1, "查詢 4：(5, 2) 應返回 1")
    
    def test_simple_single_query(self):
        """
        測試簡單情況：單個查詢。
        輸入：3x3 均勻網格，單個查詢在中心
        預期：[3]
        """
        grid = [['x', 'x', 'x'],
                ['x', 'x', 'x'],
                ['x', 'x', 'x']]
        queries = [(1, 1)]
        results = solve_largest_square(3, 3, 1, grid, queries)
        self.assertEqual(results, [3])
    
    def test_multiple_queries(self):
        """
        測試多個查詢。
        輸入：5x5 均勻網格，三個不同位置的查詢
        預期結果：中心最大，邊界最小
        """
        grid = [['m'] * 5 for _ in range(5)]
        queries = [(2, 2), (0, 0), (2, 4)]
        results = solve_largest_square(5, 5, 3, grid, queries)
        
        self.assertEqual(results[0], 5, "中心查詢應返回 5")
        self.assertEqual(results[1], 1, "角落查詢應返回 1")
        self.assertEqual(results[2], 1, "邊界查詢應返回 1")
    
    def test_empty_result_list(self):
        """
        測試沒有查詢的情況。
        輸入：3x3 網格，但沒有查詢
        預期：空列表
        """
        grid = [['a'] * 3 for _ in range(3)]
        queries = []
        results = solve_largest_square(3, 3, 0, grid, queries)
        self.assertEqual(results, [])


class TestEdgeCases(unittest.TestCase):
    """
    邊界情況和特殊情況的測試類別。
    """
    
    def test_rectangular_grid_non_square(self):
        """
        測試非正方形的矩形網格（M ≠ N）。
        輸入：4x6 網格，查詢點 (2, 3)
        預期：應正確處理不同的行列數
        """
        grid = [['p'] * 6 for _ in range(4)]
        result = find_largest_square(grid, 2, 3)
        # 距離最小邊界 = min(2, 3, 1, 2) = 1
        # 最大邊長 = 2*1 + 1 = 3
        self.assertEqual(result, 3)
    
    def test_single_row_grid(self):
        """
        測試只有一行的網格。
        輸入：1x5 網格，查詢中心點 (0, 2)
        預期：邊長 = 1
        """
        grid = [['q', 'q', 'q', 'q', 'q']]
        result = find_largest_square(grid, 0, 2)
        self.assertEqual(result, 1)
    
    def test_single_column_grid(self):
        """
        測試只有一列的網格。
        輸入：5x1 網格，查詢中心點 (2, 0)
        預期：邊長 = 1
        """
        grid = [['r'], ['r'], ['r'], ['r'], ['r']]
        result = find_largest_square(grid, 2, 0)
        self.assertEqual(result, 1)
    
    def test_different_characters_in_rows(self):
        """
        測試具有不同字元的行。
        輸入：
        aaa
        aba
        aaa
        查詢中心 (1, 1)，中心是 'b'
        預期：邊長 = 1
        """
        grid = [['a', 'a', 'a'],
                ['a', 'b', 'a'],
                ['a', 'a', 'a']]
        result = find_largest_square(grid, 1, 1)
        self.assertEqual(result, 1)
    
    def test_large_area_same_character(self):
        """
        測試大面積相同字元的情況。
        輸入：10x10 全 's' 網格，查詢中心 (5, 5)
        預期：邊長 = 9（受邊界限制）
        說明：位置 (5, 5) 距離上/左邊界為 5，距離下/右邊界為 4
              最小距離為 4，所以最大邊長 = 2*4+1 = 9
        """
        grid = [['s'] * 10 for _ in range(10)]
        result = find_largest_square(grid, 5, 5)
        self.assertEqual(result, 9)


class TestSpecialCases(unittest.TestCase):
    """
    測試特殊和複雜的情況。
    """
    
    def test_checkerboard_pattern(self):
        """
        測試棋盤式圖案。
        輸入：4x4 棋盤式網格
        ababab...
        bababa...
        查詢中心點
        預期：邊長 = 1
        """
        grid = [['a' if (i + j) % 2 == 0 else 'b' for j in range(4)] for i in range(4)]
        result = find_largest_square(grid, 1, 1)
        self.assertEqual(result, 1)
    
    def test_cross_pattern(self):
        """
        測試十字圖案。
        輸入：5x5 網格，中心十字為 'x'，其他為 'o'
        預期：邊長 = 1
        """
        grid = [['o', 'o', 'x', 'o', 'o'],
                ['o', 'o', 'x', 'o', 'o'],
                ['x', 'x', 'x', 'x', 'x'],
                ['o', 'o', 'x', 'o', 'o'],
                ['o', 'o', 'x', 'o', 'o']]
        result = find_largest_square(grid, 2, 2)
        self.assertEqual(result, 1)
    
    def test_concentric_squares(self):
        """
        測試同心正方形圖案。
        輸入：7x7 網格，由同心正方形組成
        預期：中心查詢應返回邊長 = 1
        """
        grid = [['a'] * 7 for _ in range(7)]
        # 設定內部邊界
        for i in range(2, 5):
            for j in range(2, 5):
                grid[i][j] = 'b'
        
        result = find_largest_square(grid, 3, 3)
        self.assertEqual(result, 3)


def run_tests():
    """
    運行所有測試並顯示詳細結果。
    """
    # 建立測試套件
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # 加入所有測試類別
    suite.addTests(loader.loadTestsFromTestCase(TestIsValidSquare))
    suite.addTests(loader.loadTestsFromTestCase(TestFindLargestSquare))
    suite.addTests(loader.loadTestsFromTestCase(TestSolveLargestSquare))
    suite.addTests(loader.loadTestsFromTestCase(TestEdgeCases))
    suite.addTests(loader.loadTestsFromTestCase(TestSpecialCases))
    
    # 運行測試
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # 返回測試結果
    return result


if __name__ == '__main__':
    # 運行所有測試，使用 verbosity=2 詳細顯示結果
    unittest.main(verbosity=2)
