# -*- coding: utf-8 -*-
import unittest
import importlib

# 動態匯入數字命名的 Python 檔案
# 假設解題程式名為 10193.py，且裡面實作了 solve(a) 函式
try:
    # 改為載入簡單易記版 10193-easy.py
    sol = importlib.import_module("10193-easy")
    solve = sol.solve
except ImportError:
    # 如果找不到模組，將 solve 設為 None，並在測試中跳過
    solve = None

class TestUVA10193(unittest.TestCase):

    def setUp(self):
        """在每個測試開始前執行，確保解題函式已成功匯入"""
        if solve is None:
            self.skipTest("尚未找到 10193.py 或其解題函式 solve")

    def test_a_is_1(self):
        """基礎測試：a = 1"""
        # 根據公式 (b-a)(c-a) = a^2+1
        # (b-1)(c-1) = 1+1^2 = 2.
        # 2 的因數為 (1, 2)。
        # b-1=1, c-1=2 => b=2, c=3.
        # b+c 的最小值為 2+3=5。
        self.assertEqual(solve(1), 5)

    def test_a_is_2(self):
        """基礎測試：a = 2"""
        # (b-2)(c-2) = 1+2^2 = 5.
        # 5 的因數為 (1, 5)。
        # b-2=1, c-2=5 => b=3, c=7.
        # b+c 的最小值為 3+7=10。
        self.assertEqual(solve(2), 10)

    def test_composite_N(self):
        """進階測試：a=12, 此時 a^2+1 = 145 為合成數"""
        # (b-12)(c-12) = 145.
        # 145 的因數對有 (1, 145) 和 (5, 29)。因數和分別為 146 和 34。
        # 為了讓 b+c 最小，我們需要取最接近 sqrt(145) 的因數對 (5, 29)。
        # b-12=5, c-12=29 => b=17, c=41. b+c 的最小值為 17+41=58。
        self.assertEqual(solve(12), 58)

    def test_prime_N(self):
        """進階測試：a=20, 此時 a^2+1 = 401 為質數"""
        # (b-20)(c-20) = 401. 401 是質數，因數只有 (1, 401)。
        # b-20=1, c-20=401 => b=21, c=421. b+c 的最小值為 21+421=442。
        self.assertEqual(solve(20), 442)

    def test_large_a(self):
        """邊界測試：測試較大的 a 值，例如 a = 100"""
        # (b-100)(c-100) = 100^2+1 = 10001. 10001 = 73 * 137.
        # b-100=73, c-100=137 => b=173, c=237. b+c 的最小值為 173+237=410。
        self.assertEqual(solve(100), 410)

if __name__ == '__main__':
    unittest.main()