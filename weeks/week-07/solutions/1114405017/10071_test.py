import unittest
from io import StringIO
import sys

# 這裡封裝原本的邏輯，方便測試調用
def get_count_of_sextuplets(n, s):
    sum_counts = {}
    # 計算 a + b + c
    for a in s:
        for b in s:
            for c in s:
                lhs = a + b + c
                sum_counts[lhs] = sum_counts.get(lhs, 0) + 1
                    
    ans = 0
    # 計算 f - e - d
    for f in s:
        for d in s:
            for e in s:
                rhs = f - d - e
                if rhs in sum_counts:
                    ans += sum_counts[rhs]
    return ans

class TestUVA10071(unittest.TestCase):

    def test_example_case(self):
        """測試題目範例：N=2, S={1, 2}"""
        n = 2
        s = [1, 2]
        # 預期輸出為 20
        # (例如: 1+1+1+1+1=5 不可能, 但 1+1+1+1+2=6 在集合中沒有 6)
        # 這裡會包含如 1+1+1+1+1=5(X), 實質上是符合 a+b+c+d+e=f 的組合
        self.assertEqual(get_count_of_sextuplets(n, s), 20)

    def test_single_element_zero(self):
        """測試只有一個元素且為 0 的情況：0+0+0+0+0=0"""
        n = 1
        s = [0]
        # 只有一種可能：(0,0,0,0,0,0)
        self.assertEqual(get_count_of_sextuplets(n, s), 1)

    def test_negative_numbers(self):
        """測試包含負數的情況"""
        n = 2
        s = [-1, 1]
        # 這裡會有許多抵消的情況
        # 例如: -1 + 1 + -1 + 1 + 1 = 1
        result = get_count_of_sextuplets(n, s)
        self.assertGreater(result, 0)
        print(f"\n負數測試結果 (S={s}): {result}")

    def test_large_numbers(self):
        """測試數值較大時是否正確（不影響邏輯但確認溢位問題，Python 自動處理大數）"""
        n = 2
        s = [30000, -30000]
        result = get_count_of_sextuplets(n, s)
        # 結果應該與 [-1, 1] 相同，因為結構是一樣的
        self.assertEqual(result, get_count_of_sextuplets(2, [-1, 1]))

if __name__ == "__main__":
    unittest.main()