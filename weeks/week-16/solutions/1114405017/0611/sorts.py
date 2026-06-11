from typing import List, Any


def bubble_sort(data: List[Any]) -> List[Any]:
    """回傳新 list，不修改傳入 list。簡單 Bubble (有提前停止)。"""
    a = list(data)
    n = len(a)
    if n <= 1:
        return a
    for i in range(n):
        swapped = False
        for j in range(0, n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a


def quick_sort(data: List[Any]) -> List[Any]:
    """純函式式 quick sort，回傳新 list，不修改輸入。"""
    if len(data) <= 1:
        return list(data)
    pivot = data[len(data) // 2]
    less = [x for x in data if x < pivot]
    equal = [x for x in data if x == pivot]
    greater = [x for x in data if x > pivot]
    return quick_sort(less) + equal + quick_sort(greater)


def merge_sort(data: List[Any]) -> List[Any]:
    """純函式式 merge sort，回傳新 list，不修改輸入。"""
    a = list(data)
    n = len(a)
    if n <= 1:
        return a
    mid = n // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    i = j = 0
    merged = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged
