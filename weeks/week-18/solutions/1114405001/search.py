"""
Binary Search vs Linear Search Implementation
K = 101
"""

from dataclasses import dataclass
from typing import List


@dataclass
class SearchResult:
    """搜尋結果資料類"""
    found: bool
    index: int
    comparisons: int


def linear_search(arr: List[int], target: int) -> SearchResult:
    """
    線性搜尋 - O(n) 時間複雜度
    逐一檢查陣列中的每個元素
    
    Args:
        arr: 升序整數陣列
        target: 搜尋目標值
    
    Returns:
        SearchResult: 搜尋結果（是否找到、索引、比較次數）
    """
    comparisons = 0
    
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return SearchResult(found=True, index=i, comparisons=comparisons)
    
    return SearchResult(found=False, index=-1, comparisons=comparisons)


def binary_search(arr: List[int], target: int) -> SearchResult:
    """
    二分搜尋 - O(log n) 時間複雜度
    在升序陣列中進行分治搜尋
    
    Args:
        arr: 升序整數陣列
        target: 搜尋目標值
    
    Returns:
        SearchResult: 搜尋結果（是否找到、索引、比較次數）
    """
    left = 0
    right = len(arr) - 1
    comparisons = 0
    
    while left <= right:
        comparisons += 1
        mid = (left + right) // 2
        mid_value = arr[mid]
        
        if mid_value == target:
            return SearchResult(found=True, index=mid, comparisons=comparisons)
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return SearchResult(found=False, index=-1, comparisons=comparisons)


def format_output(result: SearchResult) -> str:
    """
    格式化搜尋結果輸出
    
    Args:
        result: SearchResult 物件
    
    Returns:
        格式化的字符串 "FOUND idx cmp=X" 或 "NOT FOUND -1 cmp=X"
    """
    if result.found:
        return f"FOUND {result.index} cmp={result.comparisons}"
    else:
        return f"NOT FOUND -1 cmp={result.comparisons}"
