import unittest

# 導入解答程式
# from solution_10908 import solve_10908

class TestLargestSquare(unittest.TestCase):
    """
    測試 UVA 10908 - Largest Square
    測試在網格中找最大正方形邊長
    """
    
    def expand_from_center(self, grid, r, c):
        """
        從中心點 (r, c) 向外擴展，找最大正方形邊長
        返回最大邊長（必須為奇數）
        """
        M, N = len(grid), len(grid[0])
        center_char = grid[r][c]
        max_radius = 0
        
        # 嘗試擴大正方形半徑
        for radius in range(1, max(M, N)):
            # 檢查四個方向都有效
            top = r - radius
            bottom = r + radius
            left = c - radius
            right = c + radius
            
            if top < 0 or bottom >= M or left < 0 or right >= N:
                break
            
            # 檢查所有邊界點是否相同
            valid = True
            for i in range(top, bottom + 1):
                if grid[i][left] != center_char or grid[i][right] != center_char:
                    valid = False
                    break
            for j in range(left, right + 1):
                if grid[top][j] != center_char or grid[bottom][j] != center_char:
                    valid = False
                    break
            
            if valid:
                max_radius = radius
            else:
                break
        
        return 2 * max_radius + 1
    
    def test_single_character(self):
        """測試中心點只有一個字符的情況"""
        grid = [['a']]
        result = self.expand_from_center(grid, 0, 0)
        self.assertEqual(result, 1)
    
    def test_three_by_three(self):
        """測試 3x3 全相同的情況"""
        grid = [
            ['a', 'a', 'a'],
            ['a', 'a', 'a'],
            ['a', 'a', 'a']
        ]
        result = self.expand_from_center(grid, 1, 1)
        self.assertEqual(result, 3)
    
    def test_five_by_five(self):
        """測試 5x5 全相同的情況"""
        grid = [
            ['b', 'b', 'b', 'b', 'b'],
            ['b', 'b', 'b', 'b', 'b'],
            ['b', 'b', 'b', 'b', 'b'],
            ['b', 'b', 'b', 'b', 'b'],
            ['b', 'b', 'b', 'b', 'b']
        ]
        result = self.expand_from_center(grid, 2, 2)
        self.assertEqual(result, 5)
    
    def test_mixed_grid(self):
        """測試混合的網格，多個不同區域"""
        grid = [
            ['a', 'b', 'b', 'b', 'a'],
            ['a', 'b', 'b', 'b', 'a'],
            ['a', 'b', 'b', 'b', 'a'],
            ['a', 'a', 'a', 'a', 'a'],
            ['a', 'a', 'a', 'a', 'a']
        ]
        # 中心在 (1, 2) 的 'b'
        result = self.expand_from_center(grid, 1, 2)
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()
