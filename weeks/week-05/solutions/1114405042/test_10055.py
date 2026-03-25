import unittest
import importlib.util
import sys

# 載入我們寫的標準版本解法
from q10055 import solve_functions

# 動態載入帶有連字號 (-) 的檔案名稱 (q10055-easy.py)
# 這是一種比較進階的載入方式，解決了 Python 模組名稱不能有連字號的限制
spec = importlib.util.spec_from_file_location("q10055_easy", "q10055-easy.py")
q10055_easy_module = importlib.util.module_from_spec(spec)
sys.modules["q10055_easy"] = q10055_easy_module
spec.loader.exec_module(q10055_easy_module)
solve_functions_easy = q10055_easy_module.solve_functions_easy

class TestMonotonicFunctions(unittest.TestCase):
    """
    這是一個單元測試類別，用來驗證我們寫的 solve_functions 程式是否正確。
    """
    
    def test_case_1(self):
        # 測試範例 1: N = 3
        # 初始狀態全為 0 (增函數)
        # 操作序列:
        # 1. 查詢 1~3 => 預期 0
        # 2. 修改 2 為減函數 (f2 從增變減)
        # 3. 查詢 1~3 => 預期 1 (只有 f2 是減)
        # 4. 修改 3 為減函數 (f3 從增變減)
        # 5. 查詢 1~3 => 預期 0 (f2 和 f3 都是減，負負得正)
        n = 3
        queries = [
            (2, 1, 3), # range [1, 3]
            (1, 2),    # toggle f2
            (2, 1, 3), # range [1, 3]
            (1, 3),    # toggle f3
            (2, 1, 3), # range [1, 3]
        ]
        
        expected = [0, 1, 0]
        self.assertEqual(solve_functions(n, queries), expected)
        self.assertEqual(solve_functions_easy(n, queries), expected)

    def test_case_2(self):
        # 測試範例 2: N = 5
        # 頻繁區間與單點查詢
        n = 5
        queries = [
            (1, 1),    # f1 變減
            (1, 3),    # f3 變減
            (1, 5),    # f5 變減
            (2, 1, 5), # 全區間 1~5 有三個減函數(1,3,5) => 奇數 => 減函數(1)
            (2, 2, 4), # 區間 2~4 只有 f3 是減函數 => 奇數 => 減函數(1)
            (1, 3),    # f3 變回增函數 (負負得正)
            (2, 2, 4), # 區間 2~4 變成全是增函數 => 預期 0
            (2, 1, 5), # 全區間得 f1, f5 是減函數 => 偶數 => 預期 0
        ]
        
        expected = [1, 1, 0, 0]
        self.assertEqual(solve_functions(n, queries), expected)
        self.assertEqual(solve_functions_easy(n, queries), expected)

if __name__ == '__main__':
    # 執行測試
    unittest.main()
