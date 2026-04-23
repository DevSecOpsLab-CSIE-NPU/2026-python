import unittest

# 假設您的解答將會寫在同一個資料夾下的 solution_10035.py 中
# 並且您的解答會提供一個 solve_carries(a, b) 函式：
# 接收兩個整數字串或整數 a 與 b，並回傳格式化後的結果字串 (包含單複數處理)。
from solution_10035 import solve_carries

class TestUVA10035(unittest.TestCase):
    
    def test_no_carry(self):
        """
        基礎測試：沒有任何進位發生的情況。
        預期輸出為 "No carry operation." (注意 No 開頭大寫與句號)
        """
        self.assertEqual(solve_carries(123, 456), "No carry operation.")
        self.assertEqual(solve_carries(0, 0), "No carry operation.")

    def test_one_carry(self):
        """
        單數進位測試：只有發生 1 次進位的情況。
        預期輸出為 "1 carry operation." (注意 operation 沒有 s)
        """
        # 5 + 5 = 10 (進位 1 次)，前面 5 + 4 + 1 = 10 不對，這裡換個明確的例子
        # 123 + 594 => 3+4=7, 2+9=11 (進位 1 次), 1+5+1=7。共 1 次進位。
        self.assertEqual(solve_carries(123, 594), "1 carry operation.")
        # 9 + 1 = 10 (進位 1 次)
        self.assertEqual(solve_carries(9, 1), "1 carry operation.")

    def test_multiple_carries(self):
        """
        複數進位測試：發生 2 次以上進位的情況。
        預期輸出為 "X carry operations." (注意 operations 有加 s)
        """
        # 555 + 555 => 3 次進位
        self.assertEqual(solve_carries(555, 555), "3 carry operations.")
        
    def test_different_lengths_and_chain_carry(self):
        """
        進階/邊界測試：兩個數字長度不同，且產生「連鎖進位」的情況。
        這是在寫迴圈對齊時最容易發生 IndexError 或漏算的地方。
        """
        # 9999 + 1 => 4 次進位 (連鎖進位)
        self.assertEqual(solve_carries(9999, 1), "4 carry operations.")
        # 1 + 999 => 3 次進位 (順序顛倒也要能正確處理)
        self.assertEqual(solve_carries(1, 999), "3 carry operations.")

if __name__ == '__main__':
    unittest.main()