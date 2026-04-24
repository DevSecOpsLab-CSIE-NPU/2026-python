import unittest

# 假設您的解答將會寫在同一個資料夾下的 solution_10071.py 中
# 並且您的解答會提供一個 count_solutions(s_set) 函式：
# - s_set: 包含 N 個整數的集合 S (list of ints)
# 回傳滿足 a+b+c+d+e = f 的六元組總數 (int)。
from solution_10071 import count_solutions

class TestUVA10071(unittest.TestCase):
    
    def test_no_solution(self):
        """
        基礎測試：集合中只有一個非零數字，無法構成等式。
        a+b+c+d+e = f -> 1+1+1+1+1 = 5, 但 f 只能是 1。
        """
        self.assertEqual(count_solutions([1]), 0)

    def test_zero_only(self):
        """
        邊界測試：集合中只有 0。
        只有 0+0+0+0+0 = 0 這一種組合，所以答案是 1。
        """
        self.assertEqual(count_solutions([0]), 1)

    def test_simple_case(self):
        """
        基礎測試：包含 0 和 1 的簡單情況。
        透過手動計算，a,b,c,d,e,f 均來自 {0, 1} 時，
        滿足 a+b+c+d+e = f 的組合共有 6 組。
        """
        self.assertEqual(count_solutions([0, 1]), 6)

    def test_symmetric_case(self):
        """
        進階測試：包含正負數與零的對稱情況。
        S = {-1, 0, 1}
        透過 meet-in-the-middle 演算法手動推導，
        sums(a+b+c) 的頻率分佈與 sums(f-d-e) 的頻率分佈相同，
        總組合數為 1*1 + 3*3 + 6*6 + 7*7 + 6*6 + 3*3 + 1*1 = 141。
        """
        self.assertEqual(count_solutions([-1, 0, 1]), 141)

if __name__ == '__main__':
    unittest.main()