import unittest
from io import StringIO
import sys

def simulate_logic(n, queries):
    """
    模擬邏輯的輔助函式，用於測試驗證
    """
    bit = [0] * (n + 1)
    def update(i, v):
        while i <= n:
            bit[i] ^= v
            i += i & (-i)
    def query(i):
        res = 0
        while i > 0:
            res ^= bit[i]
            i -= i & (-i)
        return res
    
    results = []
    for q in queries:
        if q[0] == 1:
            update(q[1], 1)
        else:
            res = query(q[2]) ^ query(q[1]-1)
            results.append(res)
    return results

class TestFunctionMonotonicity(unittest.TestCase):
    
    def test_basic_composition(self):
        """測試基本的複合邏輯 (增增=增, 增減=減, 減減=增)"""
        # N=3, Q=3
        # 1. 查詢 (1,3) -> 0^0^0 = 0
        # 2. 修改 f2 變減 -> (0,1,0)
        # 3. 查詢 (1,3) -> 0^1^0 = 1
        # 4. 修改 f3 變減 -> (0,1,1)
        # 5. 查詢 (1,3) -> 0^1^1 = 0
        queries = [(2, 1, 3), (1, 2), (2, 1, 3), (1, 3), (2, 1, 3)]
        expected = [0, 1, 0]
        self.assertEqual(simulate_logic(3, queries), expected)

    def test_single_function(self):
        """測試單一函數的反轉"""
        queries = [(2, 1, 1), (1, 1), (2, 1, 1)]
        expected = [0, 1]
        self.assertEqual(simulate_logic(1, queries), expected)

    def test_range_xor(self):
        """測試區間 XOR 是否正確"""
        # 函數狀態：[增, 減, 減, 增, 減] -> [0, 1, 1, 0, 1]
        queries = [
            (1, 2), (1, 3), (1, 5), # 設定狀態
            (2, 2, 3), # 1^1 = 0
            (2, 1, 5), # 0^1^1^0^1 = 1
            (2, 3, 5)  # 1^0^1 = 0
        ]
        expected = [0, 1, 0]
        self.assertEqual(simulate_logic(5, queries), expected)

if __name__ == '__main__':
    unittest.main()