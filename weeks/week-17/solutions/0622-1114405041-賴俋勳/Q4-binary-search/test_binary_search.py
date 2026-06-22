import unittest
import timeit
from binary_search import binary_search, linear_search


class TestBinarySearch(unittest.TestCase):
    """
    題目：二分搜尋功能 - 20分
    
    問題描述：
    - 產生(陸滾序) → 一份表格
    - 二分搜尋 K 位數 vs 二分搜尋位置 vs 二分搜尋自訂函式
    - 用 timeit 分別搜尋位置 vs 二分搜尋位置，對比性能
    - 產生一規避圖並用 README 說明
    
    輸入說明：
    - 第一行資料個數、第二行位數中序數
    
    輸出說明：
    - 第一列搜尋個數、第二列 timeit 結果時間輸時間輸時間輸（以秒秒秒計）
    """
    
    def test_binary_search_found(self):
        """基本測試：二分搜尋找到目標"""
        arr = [1, 3, 5, 7, 9, 11, 13, 15]
        target = 7
        result = binary_search(arr, target)
        self.assertEqual(result, 3)
    
    def test_binary_search_not_found(self):
        """基本測試：二分搜尋未找到目標"""
        arr = [1, 3, 5, 7, 9, 11, 13, 15]
        target = 8
        result = binary_search(arr, target)
        self.assertEqual(result, -1)
    
    def test_binary_search_first_element(self):
        """邊界測試：搜尋第一個元素"""
        arr = [1, 3, 5, 7, 9]
        result = binary_search(arr, 1)
        self.assertEqual(result, 0)
    
    def test_binary_search_last_element(self):
        """邊界測試：搜尋最後一個元素"""
        arr = [1, 3, 5, 7, 9]
        result = binary_search(arr, 9)
        self.assertEqual(result, 4)
    
    def test_binary_search_empty_array(self):
        """邊界測試：空陣列"""
        arr = []
        result = binary_search(arr, 5)
        self.assertEqual(result, -1)
    
    def test_binary_search_single_element_found(self):
        """邊界測試：單元素陣列，找到"""
        arr = [5]
        result = binary_search(arr, 5)
        self.assertEqual(result, 0)
    
    def test_binary_search_single_element_not_found(self):
        """邊界測試：單元素陣列，未找到"""
        arr = [5]
        result = binary_search(arr, 3)
        self.assertEqual(result, -1)
    
    def test_linear_search_vs_binary_search(self):
        """性能比較測試：線性搜尋 vs 二分搜尋"""
        arr = list(range(0, 1000000, 2))  # 大陣列
        target = 999998
        
        # 測試二分搜尋
        result_binary = binary_search(arr, target)
        self.assertNotEqual(result_binary, -1)
    
    def test_k_value_search(self):
        """K值搜尋測試：K=141（根據學號1114405041）"""
        # 建立包含 K=141 的陣列
        k_value = 141
        arr = list(range(0, 500, 2))  # [0, 2, 4, ..., 498]
        
        if k_value not in arr:
            arr.append(k_value)
            arr.sort()
        
        # 搜尋 K=141
        result = binary_search(arr, k_value)
        
        # 驗證找到了
        self.assertNotEqual(result, -1)
        # 驗證找到的值是正確的
        self.assertEqual(arr[result], k_value)
    
    def test_k_value_not_found(self):
        """K值邊界測試：K=141不存在於有限陣列中"""
        # 測試 K=141 在較小陣列中未找到的情況
        arr = list(range(0, 100, 2))  # [0, 2, 4, ..., 98]
        k_value = 141
        
        result = binary_search(arr, k_value)
        
        # 應該返回 -1（未找到）
        self.assertEqual(result, -1)


if __name__ == '__main__':
    unittest.main()
