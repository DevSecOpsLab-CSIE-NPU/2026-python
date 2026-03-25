import unittest
import importlib.util
import sys

# 載入我們寫的標準版本解法
from q10056 import solve_probability

# 動態載入帶有連字號 (-) 的檔案名稱 (q10056-easy.py)
# 這是一種比較進階的載入方式，解決了 Python 模組名稱不能有連字號的限制
spec = importlib.util.spec_from_file_location("q10056_easy", "q10056-easy.py")
q10056_easy_module = importlib.util.module_from_spec(spec)
sys.modules["q10056_easy"] = q10056_easy_module
spec.loader.exec_module(q10056_easy_module)
solve_probability_easy = q10056_easy_module.solve_probability_easy

class TestProbability(unittest.TestCase):
    """
    這是一個單元測試類別，用來驗證我們寫的 solve_probability 程式是否正確。
    我們將結果使用 round(..., 4) 四捨五入到小數點後四位進行比較。
    """
    
    def test_case_1(self):
        # 測試範例 1: N = 2, p = 0.166666, I = 1
        # 預期輸出: 0.5455 (UVA 標準測資)
        n, p, i = 2, 0.166666, 1
        expected = 0.5455
        
        self.assertAlmostEqual(round(solve_probability(n, p, i), 4), expected)
        self.assertAlmostEqual(round(solve_probability_easy(n, p, i), 4), expected)

    def test_case_2(self):
        # 測試範例 2: N = 2, p = 0.166666, I = 2
        # 預期輸出: 0.4545 (UVA 標準測資)
        n, p, i = 2, 0.166666, 2
        expected = 0.4545
        
        self.assertAlmostEqual(round(solve_probability(n, p, i), 4), expected)
        self.assertAlmostEqual(round(solve_probability_easy(n, p, i), 4), expected)

    def test_case_3(self):
        # 測試範例 3: N = 2, p = 0, I = 1
        # 當 p=0，任何人都不可能贏，預期機率為 0.0000
        n, p, i = 2, 0.0, 1
        expected = 0.0000
        
        self.assertEqual(solve_probability(n, p, i), expected)
        self.assertEqual(solve_probability_easy(n, p, i), expected)

    def test_case_4(self):
        # 測試範例 4: N = 3, p = 1.0, I = 1
        # 當 p=1，第一個人每次都一定贏，所以他的獲勝機率為 1.0000
        # 而其他人都是 0
        n, p, i = 3, 1.0, 1
        expected = 1.0000
        
        self.assertAlmostEqual(round(solve_probability(n, p, i), 4), expected)
        self.assertAlmostEqual(round(solve_probability_easy(n, p, i), 4), expected)

if __name__ == '__main__':
    # 執行測試
    unittest.main()
