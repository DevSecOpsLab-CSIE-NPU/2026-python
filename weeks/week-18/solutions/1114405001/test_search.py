"""
Test cases for binary search vs linear search
Task 1: Small array with target found (middle position)
Task 2: Large array with target found (performance comparison)
Task 3: Edge case - target not found
"""

import pytest
from search import linear_search, binary_search, SearchResult


class TestTask1SmallArrayTargetFound:
    """Task 1: 小規模陣列 - 目標存在（中間位置）
    目的：驗證基本搜尋邏輯正確性
    """
    
    def test_linear_search_small_array_middle(self):
        """Linear search 在小陣列中找到中間位置的目標"""
        arr = [1, 50, 101, 150, 200]
        result = linear_search(arr, 101)
        
        assert result.found is True
        assert result.index == 2
        assert result.comparisons >= 1
        assert result.comparisons <= len(arr)
    
    def test_binary_search_small_array_middle(self):
        """Binary search 在小陣列中找到中間位置的目標"""
        arr = [1, 50, 101, 150, 200]
        result = binary_search(arr, 101)
        
        assert result.found is True
        assert result.index == 2
        assert result.comparisons >= 1
        # Binary search 在 5 元素陣列應該最多 3 次比較（log2(5) ≈ 2.3）
        assert result.comparisons <= 3


class TestTask2LargeArrayTargetFound:
    """Task 2: 大規模陣列 - 目標存在（效能顯著差異）
    目的：驗證 binary search 的效能優勢
    """
    
    def test_linear_search_large_array(self):
        """Linear search 在大陣列中的性能"""
        arr = list(range(1, 10001))  # [1, 2, ..., 10000]
        result = linear_search(arr, 101)
        
        assert result.found is True
        assert result.index == 100  # 101 是第 101 個數
        # Linear search 在這個位置需要約 101 次比較
        assert result.comparisons >= 100
    
    def test_binary_search_large_array(self):
        """Binary search 在大陣列中的性能"""
        arr = list(range(1, 10001))  # [1, 2, ..., 10000]
        result = binary_search(arr, 101)
        
        assert result.found is True
        assert result.index == 100  # 101 是第 101 個數
        # Binary search 在 10000 元素應該最多 14 次比較（log2(10000) ≈ 13.3）
        assert result.comparisons <= 14
    
    def test_binary_search_much_faster_than_linear(self):
        """驗證 binary search 比 linear search 快很多"""
        arr = list(range(1, 10001))
        
        linear_result = linear_search(arr, 101)
        binary_result = binary_search(arr, 101)
        
        # Binary search 的比較次數應該遠少於 linear search
        assert binary_result.comparisons < linear_result.comparisons / 5


class TestTask3EdgeCaseNotFound:
    """Task 3: Edge Case - 目標不存在
    目的：驗證 NOT FOUND 邏輯正確性
    """
    
    def test_linear_search_not_found(self):
        """Linear search 找不到目標"""
        arr = [1, 50, 150, 200]  # 101 不在陣列中
        result = linear_search(arr, 101)
        
        assert result.found is False
        assert result.index == -1
        assert result.comparisons == len(arr)  # 必須檢查所有元素
    
    def test_binary_search_not_found(self):
        """Binary search 找不到目標"""
        arr = [1, 50, 150, 200]  # 101 不在陣列中
        result = binary_search(arr, 101)
        
        assert result.found is False
        assert result.index == -1
        assert result.comparisons <= len(arr)  # Binary search 比較次數少於陣列長度
    
    def test_target_not_in_range(self):
        """目標不在範圍內（太小和太大）"""
        arr = [101, 102, 103, 104, 105]
        
        # 搜尋太小的值
        result_small = binary_search(arr, 100)
        assert result_small.found is False
        assert result_small.index == -1
        
        # 搜尋太大的值
        result_large = binary_search(arr, 106)
        assert result_large.found is False
        assert result_large.index == -1


class TestEdgeCasesAdditional:
    """額外的 edge case 測試"""
    
    def test_single_element_array_found(self):
        """單元素陣列，目標存在"""
        arr = [101]
        
        linear_result = linear_search(arr, 101)
        binary_result = binary_search(arr, 101)
        
        assert linear_result.found is True
        assert linear_result.index == 0
        assert binary_result.found is True
        assert binary_result.index == 0
    
    def test_single_element_array_not_found(self):
        """單元素陣列，目標不存在"""
        arr = [100]
        
        linear_result = linear_search(arr, 101)
        binary_result = binary_search(arr, 101)
        
        assert linear_result.found is False
        assert linear_result.index == -1
        assert binary_result.found is False
        assert binary_result.index == -1
    
    def test_target_at_start(self):
        """目標在陣列起始"""
        arr = [101, 102, 103, 104, 105]
        
        linear_result = linear_search(arr, 101)
        binary_result = binary_search(arr, 101)
        
        assert linear_result.found is True
        assert linear_result.index == 0
        assert binary_result.found is True
        assert binary_result.index == 0
    
    def test_target_at_end(self):
        """目標在陣列末尾"""
        arr = [97, 98, 99, 100, 101]
        
        linear_result = linear_search(arr, 101)
        binary_result = binary_search(arr, 101)
        
        assert linear_result.found is True
        assert linear_result.index == 4
        assert binary_result.found is True
        assert binary_result.index == 4
