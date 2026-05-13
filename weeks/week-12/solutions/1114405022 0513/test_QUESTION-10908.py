import unittest

# ============================================================================
# UVA 10908 - Largest Square 解題函數
# ============================================================================

def find_largest_square(grid, r, c):
    """
    在給定的網格中，找出以 (r, c) 為中心的最大正方形邊長。
    
    正方形必須滿足：
    1. 中心點為 (r, c)
    2. 所有字元相同
    3. 邊長為奇數（1, 3, 5, ...）
    
    參數：
        grid (list): M 行 N 列的字元網格
        r (int): 中心點行座標（0-indexed）
        c (int): 中心點列座標（0-indexed）
    
    返回：
        int: 最大正方形的邊長
    """
    M = len(grid)           # 行數
    N = len(grid[0])        # 列數
    
    # 邊界檢查
    if r < 0 or r >= M or c < 0 or c >= N:
        return 0
    
    # 中心點的字符
    center_char = grid[r][c]
    
    # 最大可能的半径（从中心点到最近边界的距离）
    max_radius = min(r, c, M - 1 - r, N - 1 - c)
    
    # 從最大可能的大小開始，逐漸減小（貪心方式）
    # k 代表半径，邊長 = 2k + 1
    for k in range(max_radius, -1, -1):
        # 檢查邊長為 2k+1 的正方形是否有效
        # 正方形的邊界是：
        # - 上: row = r - k
        # - 下: row = r + k
        # - 左: col = c - k
        # - 右: col = c + k
        
        valid = True
        
        # 檢查正方形內所有字元是否相同
        for i in range(r - k, r + k + 1):
            for j in range(c - k, c + k + 1):
                if grid[i][j] != center_char:
                    valid = False
                    break
            if not valid:
                break
        
        # 若該大小的正方形有效，返回其邊長
        if valid:
            return 2 * k + 1
    
    # 至少邊長為 1 的正方形總是有效的（單個字元）
    return 1


# ============================================================================
# 單元測試類別
# ============================================================================

class TestLargestSquare(unittest.TestCase):
    """
    UVA 10908 - Largest Square 的單元測試類別
    """
    
    def setUp(self):
        """
        測試前準備：建立測試用的網格
        """
        # 建立題目範例的網格
        self.grid_example = [
            "abbbaaaaaa",
            "abbbaaaaaa",
            "abbbaaaaaa",
            "aaaaaaaaaa",
            "aaaaaaaaaa",
            "aaccaaaaaa",
            "aaccaaaaaa"
        ]
    
    def test_center_of_large_b_square(self):
        """
        測試: 題目範例 - 中心在 b 字符正方形區域
        位置: (1, 2)
        預期: 3
        說明: 
          網格的左上角 3×3 區域都是 'b' 字符
          以 (1, 2) 為中心，邊長 3 的正方形內都是 'b'
          邊長 5 會超出 'b' 區域，所以最大邊長是 3
        """
        result = find_largest_square(self.grid_example, 1, 2)
        self.assertEqual(result, 3)
    
    def test_isolated_character(self):
        """
        測試: 孤立的字符
        位置: (2, 4)
        預期: 1
        說明: 
          以 (2, 4) 為中心，周圍都是 'a'，中心是 'a'
          只有邊長 1 的正方形能滿足條件（單個字元）
          任何更大的正方形都會包含不同字符
        """
        result = find_largest_square(self.grid_example, 2, 4)
        self.assertEqual(result, 1)
    
    def test_large_a_region(self):
        """
        測試: 題目範例 - 中心在大型 'a' 區域
        位置: (4, 6)
        預期: 5
        說明:
          以 (4, 6) 為中心，周圍大部分都是 'a'
          從 (2, 4) 到 (6, 8) 的 5×5 區域都是 'a'
          這個 5×5 正方形完全滿足條件
        """
        result = find_largest_square(self.grid_example, 4, 6)
        self.assertEqual(result, 5)
    
    def test_center_near_edge(self):
        """
        測試: 題目範例 - 中心點在邊界附近
        位置: (5, 2)
        預期: 1
        說明:
          以 (5, 2) 為中心，這裡是 'c' 字符
          由於位置有限，邊長 3 的正方形會超出界限
          只能返回邊長 1
        """
        result = find_largest_square(self.grid_example, 5, 2)
        self.assertEqual(result, 1)
    
    def test_uniform_grid(self):
        """
        測試: 全部相同字符的網格
        網格: 3×3 全是 'a'
        位置: (1, 1)
        預期: 3
        說明:
          整個 3×3 網格都是 'a'，中心在 (1, 1)
          最大邊長 3 的正方形就是整個網格
        """
        grid = ["aaa", "aaa", "aaa"]
        result = find_largest_square(grid, 1, 1)
        self.assertEqual(result, 3)
    
    def test_single_cell(self):
        """
        測試: 單個字符網格
        網格: 1×1
        位置: (0, 0)
        預期: 1
        說明:
          網格只有一個字符，只能返回邊長 1
        """
        grid = ["x"]
        result = find_largest_square(grid, 0, 0)
        self.assertEqual(result, 1)
    
    def test_cross_pattern(self):
        """
        測試: 十字形圖案
        網格:
          aaaa
          abbb
          abbb
          abbb
          aaaa
        位置: (2, 2)
        預期: 3
        說明:
          以 (2, 2) 為中心（'b'字符）
          邊長 3 的正方形 (1,1) 到 (3,3) 都是 'b'
          周圍的 'a' 字符限制了進一步擴展
        """
        grid = [
            "aaaa",
            "abbb",
            "abbb",
            "abbb",
            "aaaa"
        ]
        result = find_largest_square(grid, 2, 2)
        self.assertEqual(result, 3)
    
    def test_alternating_pattern(self):
        """
        測試: 交替圖案（棋盤式）
        網格:
          ababab
          bababa
          ababab
        位置: (1, 1)
        預期: 1
        說明:
          位置 (1, 1) 是 'a' 字符
          周圍都是 'b' 字符，無法擴展
          只有邊長 1 有效
        """
        grid = [
            "ababab",
            "bababa",
            "ababab"
        ]
        result = find_largest_square(grid, 1, 1)
        self.assertEqual(result, 1)
    
    def test_odd_side_lengths(self):
        """
        測試: 驗證邊長總是奇數
        網格: 9×9 全是 'x'
        位置: (4, 4) （中心）
        預期: 9
        說明:
          9×9 的網格，中心在 (4, 4)
          最大邊長應該是 9（奇數）
          邊長 = 2k + 1，其中 k = 4，所以邊長 = 9
        """
        grid = ["x" * 9 for _ in range(9)]
        result = find_largest_square(grid, 4, 4)
        self.assertEqual(result, 9)
    
    def test_rectangular_grid(self):
        """
        測試: 非正方形的網格
        網格: 3×7 全是 'z'
        位置: (1, 3)
        預期: 3
        說明:
          網格為 3×7（3行7列）
          中心在 (1, 3)，到上下邊界距離都是 1
          最大半径 = min(1, 3, 3-1, 7-1-3) = min(1, 3, 2, 3) = 1
          但內容全相同，邊長 3 時會超出上下邊界
          實際最大邊長為 3（跨度確實是 0 到 2 行）
        """
        grid = ["zzzzzzz", "zzzzzzz", "zzzzzzz"]
        result = find_largest_square(grid, 1, 3)
        self.assertEqual(result, 3)


if __name__ == '__main__':
    # 運行所有測試
    unittest.main()
