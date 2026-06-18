# -*- coding: utf-8 -*-
def bubble_sort(data: list) -> list:
    """氣泡排序：回傳新串列，具備提早結束優化"""
    arr = list(data)
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def quick_sort(data: list) -> list:
    """快速排序：回傳新串列，使用隨機 Pivot 避免最差情況"""
    if len(data) <= 1:
        return list(data)
    import random
    pivot = random.choice(data)
    left = [x for x in data if x < pivot]
    middle = [x for x in data if x == pivot]
    right = [x for x in data if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(data: list) -> list:
    """合併排序：典型的 O(n log n) 穩定排序"""
    if len(data) <= 1:
        return list(data)
    
    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    return merge(left, right)

def builtin_sort_baseline(data: list) -> list:
    """內建排序對照組 (Timsort)"""
    return sorted(data)

