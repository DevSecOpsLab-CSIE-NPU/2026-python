import unittest
from data_cleaning import data_cleaning


class TestDataCleaning(unittest.TestCase):
    """
    題目：資料清理 (Data Cleaning) - 30分
    
    輸入：多行資料，每行包含多個數字
    - 第一行是資料個數 n (0 ≤ n ≤ 10^9)
    - 後續行含有數字
    - 最後輸入 0 表示 EOF
    
    輸出：清理後的數列
    - 去掉重複資料
    - 數字間以空白分隔
    - 最後無任何符號
    """
    
    def test_basic_cleaning(self):
        """基本測試：簡單的資料清理"""
        # 樣本輸入中的第一組: D=2 的情況
        # 輸入: 8, [4 7 4 2 9 2 6 7], 3, [1 3 5], 0
        # 預期輸出: [2 4 6 7 9], [1 3 5]（去重後排序）
        input_data = [8, [4, 7, 4, 2, 9, 2, 6, 7], 3, [1, 3, 5], 0]
        result = data_cleaning(input_data)
        self.assertEqual(result, "2 4 6 7 9\n1 3 5")
    
    def test_empty_list(self):
        """邊界測試：空列表"""
        input_data = [0]  # 單個 0 代表 EOF，無資料組
        result = data_cleaning(input_data)
        self.assertEqual(result, "")
    
    def test_no_duplicates(self):
        """測試：沒有重複的資料"""
        input_data = [3, [1, 2, 3], 0]
        result = data_cleaning(input_data)
        self.assertEqual(result, "1 2 3")
    
    def test_all_duplicates(self):
        """測試：全部相同的資料"""
        input_data = [5, [2, 2, 2, 2, 2], 0]
        result = data_cleaning(input_data)
        self.assertEqual(result, "2")
    
    def test_single_element(self):
        """邊界測試：單個元素"""
        input_data = [1, [5], 0]
        result = data_cleaning(input_data)
        self.assertEqual(result, "5")


if __name__ == '__main__':
    unittest.main()
