"""search.py - 線性搜尋與二分搜尋實作"""

from typing import Any


def linear_search(data: list, target: Any) -> int:
    """線性搜尋：逐一比對元素
    
    Args:
        data: 要搜尋的列表（不會被修改）
        target: 要尋找的目標值
        
    Returns:
        找到時回傳索引，找不到回傳 -1
    """
    for i, value in enumerate(data):
        if value == target:
            return i
    return -1


def binary_search(data: list, target: Any) -> int:
    """二分搜尋：前提 data 必須已排序
    
    Args:
        data: 已排序的列表（不會被修改）
        target: 要尋找的目標值
        
    Returns:
        找到時回傳索引，找不到回傳 -1
        
    Note:
        如果 data 未排序，行為未定義（可能回傳錯誤索引或 -1）。
        呼叫者有責任確保傳入已排序的資料。
    """
    left, right = 0, len(data) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1