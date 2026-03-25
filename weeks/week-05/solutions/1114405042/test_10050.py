import unittest
import importlib.util
import sys

# 載入我們寫的標準版本解法
from q10050 import solve_hartals

# 動態載入帶有連字號 (-) 的檔案名稱 (q10050-easy.py)
# 這是一種比較進階的載入方式，解決了 Python 模組名稱不能有連字號的限制
spec = importlib.util.spec_from_file_location("q10050_easy", "q10050-easy.py")
q10050_easy_module = importlib.util.module_from_spec(spec)
sys.modules["q10050_easy"] = q10050_easy_module
spec.loader.exec_module(q10050_easy_module)
solve_hartals_easy = q10050_easy_module.solve_hartals_easy

class TestHartals(unittest.TestCase):
    """
    這是一個單元測試類別，用來驗證我們寫的 solve_hartals 程式是否正確。
    """
    
    def test_case_1(self):
        # 測試範例 1 (題目中的例子): N = 14, P = 3, parties = [3, 4, 8]
        # 預期輸出: 5 天
        # 解釋: 
        # 政黨 1 罷會: 3, 6, 9, 12
        # 政黨 2 罷會: 4, 8, 12
        # 政黨 3 罷會: 8
        # 合併後: 3, 4, 6, 8, 9, 12
        # 其中 6 (第 6 天) 是星期五，所以不計入損失的工作天
        # 實際損失: 3, 4, 8, 9, 12 (共 5 天)
        n_days = 14
        parties = [3, 4, 8]
        
        self.assertEqual(solve_hartals(n_days, parties), 5)
        self.assertEqual(solve_hartals_easy(n_days, parties), 5)

    def test_case_2(self):
        # 測試範例 2: N = 100, P = 4, parties = [12, 15, 25, 40]
        # 預期輸出: 15 天
        n_days = 100
        parties = [12, 15, 25, 40]
        
        self.assertEqual(solve_hartals(n_days, parties), 15)
        self.assertEqual(solve_hartals_easy(n_days, parties), 15)

    def test_case_3(self):
        # 測試範例 3: N = 7, P = 1, parties = [6]
        # 政黨罷會在第 6 天 (星期五)，因為是假日，預期損失的工作天為 0
        n_days = 7
        parties = [6]
        
        self.assertEqual(solve_hartals(n_days, parties), 0)
        self.assertEqual(solve_hartals_easy(n_days, parties), 0)

    def test_case_4(self):
        # 測試範例 4: N = 7, P = 1, parties = [7]
        # 題目說 h_i 永遠不會是 7 的倍數，所以這種情況不需要考慮
        # 但如果我們放一個合法天數例如 1 (每天罷會)
        # N = 7 (一週) 扣掉星期五(6)與星期六(7)
        # 預期損失: 5 天
        n_days = 7
        parties = [1]
        
        self.assertEqual(solve_hartals(n_days, parties), 5)
        self.assertEqual(solve_hartals_easy(n_days, parties), 5)

if __name__ == '__main__':
    # 執行測試
    unittest.main()
