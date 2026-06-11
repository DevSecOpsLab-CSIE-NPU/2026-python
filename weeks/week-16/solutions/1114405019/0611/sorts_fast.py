"""排序演算法優化版（Stage 3）

三種優化策略：
  bubble_sort_fast — 早停（early termination）：某趟若無交換，已排序，立即結束
  quick_sort_fast  — 中間元素 pivot：避免已排序輸入退化成 O(n²)
  merge_sort_fast  — bottom-up 迭代合併排序：省去遞迴堆疊開銷
"""


def bubble_sort_fast(data: list) -> list:
    result = list(data)
    n = len(result)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break
    return result


def quick_sort_fast(data: list) -> list:
    result = list(data)
    _qs_fast(result, 0, len(result) - 1)
    return result


def _qs_fast(arr, low, high):
    if low < high:
        pi = _partition_mid(arr, low, high)
        _qs_fast(arr, low, pi - 1)
        _qs_fast(arr, pi + 1, high)


def _partition_mid(arr, low, high):
    # 中間元素當 pivot，避免已排序陣列的最壞情況
    mid = (low + high) // 2
    arr[mid], arr[high] = arr[high], arr[mid]
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def merge_sort_fast(data: list) -> list:
    result = list(data)
    n = len(result)
    width = 1
    while width < n:
        for i in range(0, n, 2 * width):
            mid = min(i + width, n)
            right = min(i + 2 * width, n)
            if mid < right:
                result[i:right] = _merge(result[i:mid], result[mid:right])
        width *= 2
    return result


def _merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
