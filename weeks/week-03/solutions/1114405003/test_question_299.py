"""
題目 299：火車車廂置換的單元測試程式

這個程式測試計算最少相鄰車廂交換次數的演算法
核心概念：最少交換次數 = 逆序對(Inversion)個數

逆序對：在排列中，若i < j但arr[i] > arr[j]，則(i,j)構成一個逆序對
"""

import unittest
from typing import List


# ============================================================================
# 火車車廂置換類別
# ============================================================================

class TrainSwapper:
    """
    火車車廂置換求解器
    
    使用合併排序的方式計算逆序對個數
    時間複雜度：O(n log n)
    空間複雜度：O(n)
    """
    
    def count_inversions_merge_sort(self, arr: List[int]) -> int:
        """
        使用合併排序計算逆序對個數（最佳方法）
        
        原理：
        - 合併排序過程中，當右邊子陣列的元素小於左邊子陣列的元素時
          該元素與左邊剩餘的所有元素都構成逆序對
        
        Args:
            arr: 火車車廂的排列
            
        Returns:
            逆序對的個數
        """
        if len(arr) <= 1:
            return 0
        
        # 建立工作用的複本
        temp_arr = arr[:]
        
        # 呼叫遞迴函式進行合併排序並計數
        return self._merge_sort_count(temp_arr, 0, len(temp_arr) - 1)
    
    def _merge_sort_count(self, arr: List[int], left: int, right: int) -> int:
        """
        遞迴的合併排序計數函式
        
        Args:
            arr: 陣列
            left: 左邊界索引
            right: 右邊界索引
            
        Returns:
            該範圍內的逆序對個數
        """
        if left >= right:
            return 0
        
        # 計算中點
        mid = (left + right) // 2
        
        # 分別計算左邊和右邊的逆序對
        inversion_count = 0
        inversion_count += self._merge_sort_count(arr, left, mid)
        inversion_count += self._merge_sort_count(arr, mid + 1, right)
        
        # 合併並計算交叉的逆序對
        inversion_count += self._merge_count(arr, left, mid, right)
        
        return inversion_count
    
    def _merge_count(self, arr: List[int], left: int, mid: int, right: int) -> int:
        """
        合併兩個已排序的子陣列，並計算產生的逆序對
        
        當從右邊子陣列取出一個元素時，如果它小於左邊仍未取出的元素
        則該元素與左邊剩餘的所有元素都構成逆序對
        
        Args:
            arr: 陣列
            left: 左子陣列的開始索引
            mid: 左子陣列的結束索引
            right: 右子陣列的結束索引
            
        Returns:
            此次合併產生的逆序對個數
        """
        # 建立左右兩個臨時陣列的複本
        left_arr = arr[left:mid + 1]
        right_arr = arr[mid + 1:right + 1]
        
        i = j = 0
        k = left
        inversion_count = 0
        
        # 合併兩個子陣列
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] <= right_arr[j]:
                # 左邊元素較小，直接放入
                arr[k] = left_arr[i]
                i += 1
            else:
                # 右邊元素較小，且小於左邊剩餘所有元素
                # 加上左邊剩餘元素的個數
                arr[k] = right_arr[j]
                inversion_count += len(left_arr) - i
                j += 1
            k += 1
        
        # 複製剩餘元素
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
        
        return inversion_count
    
    def count_inversions_simple(self, arr: List[int]) -> int:
        """
        計算逆序對個數（簡單但低效的方法）
        
        直接比較所有配對，O(n²)時間複雜度
        適合小規模數據或理解演算法概念
        
        Args:
            arr: 火車車廂的排列
            
        Returns:
            逆序對的個數
        """
        count = 0
        n = len(arr)
        
        # 檢查所有配對
        for i in range(n):
            for j in range(i + 1, n):
                if arr[i] > arr[j]:
                    count += 1
        
        return count
    
    def solve(self, train_order: List[int]) -> int:
        """
        求解火車車廂置換問題
        
        Args:
            train_order: 火車當前的車廂順序
            
        Returns:
            最少交換次數
        """
        # 使用高效的合併排序方法
        return self.count_inversions_merge_sort(train_order)


# ============================================================================
# 單元測試類別
# ============================================================================

class TestTrainSwapperBasics(unittest.TestCase):
    """測試基本的逆序對計數功能"""
    
    def setUp(self):
        """每個測試前的準備工作"""
        self.swapper = TrainSwapper()
    
    def test_already_sorted(self):
        """測試已排序的序列應該0次交換"""
        train = [1, 2, 3, 4, 5]
        self.assertEqual(self.swapper.solve(train), 0)
    
    def test_reverse_sorted(self):
        """測試完全反序的序列"""
        # [5, 4, 3, 2, 1] 有 10 個逆序對
        # C(5,2) = 10
        train = [5, 4, 3, 2, 1]
        self.assertEqual(self.swapper.solve(train), 10)
    
    def test_single_element(self):
        """測試單一元素"""
        train = [1]
        self.assertEqual(self.swapper.solve(train), 0)
    
    def test_two_elements_sorted(self):
        """測試兩個元素已排序"""
        train = [1, 2]
        self.assertEqual(self.swapper.solve(train), 0)
    
    def test_two_elements_reversed(self):
        """測試兩個元素反序"""
        train = [2, 1]
        self.assertEqual(self.swapper.solve(train), 1)
    
    def test_three_elements(self):
        """測試三個元素"""
        # [3, 2, 1] 有 3 個逆序對：(3,2), (3,1), (2,1)
        train = [3, 2, 1]
        self.assertEqual(self.swapper.solve(train), 3)
    
    def test_partial_inversion(self):
        """測試部分逆序的序列"""
        # [2, 1, 3] 有 1 個逆序對：(2,1)
        train = [2, 1, 3]
        self.assertEqual(self.swapper.solve(train), 1)


class TestTrainSwapperExamples(unittest.TestCase):
    """測試官方範例"""
    
    def setUp(self):
        self.swapper = TrainSwapper()
    
    def test_example_1(self):
        """測試簡單範例"""
        # [1, 2, 3] 已排序
        train = [1, 2, 3]
        self.assertEqual(self.swapper.solve(train), 0)
    
    def test_example_2(self):
        """測試範例：[4, 3, 2, 1]"""
        # 4 個元素完全反序
        # 逆序對數：C(4,2) = 6
        # (4,3), (4,2), (4,1), (3,2), (3,1), (2,1)
        train = [4, 3, 2, 1]
        self.assertEqual(self.swapper.solve(train), 6)
    
    def test_example_3(self):
        """測試範例：[2, 4, 1, 3]"""
        train = [2, 4, 1, 3]
        # 逆序對：(2,1), (4,1), (4,3) = 3 對
        self.assertEqual(self.swapper.solve(train), 3)


class TestTrainSwapperLargerCases(unittest.TestCase):
    """測試較大規模的案例"""
    
    def setUp(self):
        self.swapper = TrainSwapper()
    
    def test_five_elements_reverse(self):
        """測試5個元素反序"""
        train = [5, 4, 3, 2, 1]
        # C(5,2) = 10
        self.assertEqual(self.swapper.solve(train), 10)
    
    def test_five_elements_mixed(self):
        """測試5個元素混合"""
        train = [3, 1, 4, 2, 5]
        # 逆序對：(3,1), (3,2), (4,2) = 3 對
        self.assertEqual(self.swapper.solve(train), 3)
    
    def test_longer_sequence(self):
        """測試較長序列"""
        train = [6, 5, 4, 3, 2, 1]
        # 完全反序：C(6,2) = 15
        self.assertEqual(self.swapper.solve(train), 15)


class TestInversionCountingMethods(unittest.TestCase):
    """比較兩種計數方法"""
    
    def setUp(self):
        self.swapper = TrainSwapper()
    
    def test_simple_vs_efficient_method_1(self):
        """比較兩種方法在範例1"""
        train = [3, 1, 2]
        simple = self.swapper.count_inversions_simple(train)
        efficient = self.swapper.count_inversions_merge_sort(train)
        self.assertEqual(simple, efficient)
    
    def test_simple_vs_efficient_method_2(self):
        """比較兩種方法在範例2"""
        train = [4, 2, 3, 1, 5]
        simple = self.swapper.count_inversions_simple(train)
        efficient = self.swapper.count_inversions_merge_sort(train)
        self.assertEqual(simple, efficient)
    
    def test_simple_vs_efficient_reverse(self):
        """比較兩種方法在反序序列"""
        train = [7, 6, 5, 4, 3, 2, 1]
        simple = self.swapper.count_inversions_simple(train)
        efficient = self.swapper.count_inversions_merge_sort(train)
        self.assertEqual(simple, efficient)


class TestEdgeCases(unittest.TestCase):
    """測試邊界情況"""
    
    def setUp(self):
        self.swapper = TrainSwapper()
    
    def test_empty_array(self):
        """測試空陣列"""
        train = []
        self.assertEqual(self.swapper.solve(train), 0)
    
    def test_single_inversion(self):
        """測試只有一個逆序對"""
        train = [1, 3, 2, 4]
        self.assertEqual(self.swapper.solve(train), 1)
    
    def test_alternating_pattern(self):
        """測試交替模式"""
        train = [2, 1, 4, 3, 6, 5]
        # 每對都是逆序的，共3對
        self.assertEqual(self.swapper.solve(train), 3)


class TestRealWorldScenarios(unittest.TestCase):
    """測試實際情景"""
    
    def setUp(self):
        self.swapper = TrainSwapper()
    
    def test_scenario_1_locomotive_at_end(self):
        """場景1：機車在最後"""
        train = [2, 3, 4, 5, 1]
        # (2,1), (3,1), (4,1), (5,1) = 4 對
        self.assertEqual(self.swapper.solve(train), 4)
    
    def test_scenario_2_locomotive_at_start(self):
        """場景2：機車在最前"""
        train = [1, 5, 4, 3, 2]
        # (5,4), (5,3), (5,2), (4,3), (4,2), (3,2) = 6 對
        self.assertEqual(self.swapper.solve(train), 6)
    
    def test_scenario_3_mostly_correct(self):
        """場景3：大多已排列正確，只有小部分亂序"""
        train = [1, 2, 4, 3, 5]
        # (4,3) = 1 對
        self.assertEqual(self.swapper.solve(train), 1)


class TestOutputFormat(unittest.TestCase):
    """測試輸出格式"""
    
    def test_output_format(self):
        """測試輸出格式是否正確"""
        swapper = TrainSwapper()
        train = [2, 1, 3]
        swaps = swapper.solve(train)
        output = f"Optimal train swapping takes {swaps} swaps."
        self.assertEqual(output, "Optimal train swapping takes 1 swaps.")
    
    def test_output_zero_swaps(self):
        """測試0次交換的輸出"""
        swapper = TrainSwapper()
        train = [1, 2, 3]
        swaps = swapper.solve(train)
        output = f"Optimal train swapping takes {swaps} swaps."
        self.assertEqual(output, "Optimal train swapping takes 0 swaps.")


# ============================================================================
# 主程式入口
# ============================================================================

if __name__ == '__main__':
    # 執行所有單元測試
    unittest.main(verbosity=2)
