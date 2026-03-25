import unittest
import importlib.util
import sys

# 載入我們寫的兩種版本的解法
from q10041 import solve_vito

# 動態載入帶有連字號 (-) 的檔案名稱 (q10041-easy.py)
spec = importlib.util.spec_from_file_location("q10041_easy", "q10041-easy.py")
q10041_easy_module = importlib.util.module_from_spec(spec)
sys.modules["q10041_easy"] = q10041_easy_module
spec.loader.exec_module(q10041_easy_module)
solve_vito_easy = q10041_easy_module.solve_vito_easy

class TestVitoFamily(unittest.TestCase):
    """
    這是一個單元測試類別，用來驗證我們寫的 solve_vito 程式是否正確。
    """
    
    def test_case_1(self):
        # 測試範例 1: 2 個親戚，門牌為 2, 4
        # 中位數為 4 (或 2)，距離總和為 |2-4| + |4-4| = 2
        data = [2, 2, 4] # 第一個數字 2 代表有兩個親戚
        
        # 測試標準版本
        self.assertEqual(solve_vito(data), 2)
        # 測試簡易版本
        self.assertEqual(solve_vito_easy(data), 2)

    def test_case_2(self):
        # 測試範例 2: 3 個親戚，門牌為 2, 4, 6
        # 中位數為 4，距離總和為 |2-4| + |4-4| + |6-4| = 2 + 0 + 2 = 4
        data = [3, 2, 4, 6]
        
        self.assertEqual(solve_vito(data), 4)
        self.assertEqual(solve_vito_easy(data), 4)

    def test_case_3(self):
        # 測試範例 3: 相同門牌號碼
        # 中位數為 3，距離總和為 |3-3| + |3-3| + |3-3| = 0
        data = [3, 3, 3, 3]
        
        self.assertEqual(solve_vito(data), 0)
        self.assertEqual(solve_vito_easy(data), 0)

    def test_case_4(self):
        # 測試範例 4: 門牌號碼沒有按照順序
        # 排序後為: 1, 3, 7, 10
        # 中位數為 7 (或 3)，距離總和為 |1-7| + |3-7| + |7-7| + |10-7| = 6 + 4 + 0 + 3 = 13
        data = [4, 7, 3, 1, 10]
        
        self.assertEqual(solve_vito(data), 13)
        self.assertEqual(solve_vito_easy(data), 13)

if __name__ == '__main__':
    # 執行測試
    unittest.main()
