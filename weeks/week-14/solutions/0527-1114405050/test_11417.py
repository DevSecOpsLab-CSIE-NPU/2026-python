import unittest
import math

# ==========================================
# 核心解題邏輯 (可移至獨立檔案例如 solution_11417.py)
# ==========================================
def calculate_gcd_sum(n: int) -> int:
    """
    計算給定 N 的 GCD 總和 G。
    根據題目公式：G = sum(gcd(i, j)) for 1 <= i < j <= n
    """
    total_gcd = 0
    # i 從 1 走到 n-1
    for i in range(1, n):
        # j 從 i+1 走到 n
        for j in range(i + 1, n + 1):
            # 累加 i 和 j 的最大公因數 (GCD)
            total_gcd += math.gcd(i, j)
            
    return total_gcd

# ==========================================
# 單元測試區塊
# ==========================================
class TestGCDSum(unittest.TestCase):
    
    def test_case_1(self):
        """測試 N = 10"""
        self.assertEqual(calculate_gcd_sum(10), 67, "N=10 時的輸出應為 67")

    def test_case_2(self):
        """測試 N = 100"""
        self.assertEqual(calculate_gcd_sum(100), 13015, "N=100 時的輸出應為 13015")
        
    def test_case_3(self):
        """測試 N = 500"""
        self.assertEqual(calculate_gcd_sum(500), 442011, "N=500 時的輸出應為 442011")

if __name__ == '__main__':
    unittest.main()