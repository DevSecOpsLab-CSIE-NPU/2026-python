def bubble_sort(data: list) -> list:
    """泡沫排序（回傳全新已排序的 list）。"""
    if not isinstance(data, list):
        raise TypeError("Input must be a list")
    
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
    """快速排序（回傳全新已排序的 list，非原地排序）。"""
    if not isinstance(data, list):
        raise TypeError("Input must be a list")
        
    def _qs(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return _qs(left) + middle + _qs(right)
        
    return _qs(data)


def merge_sort(data: list) -> list:
    """合併排序（回傳全新已排序的 list）。"""
    if not isinstance(data, list):
        raise TypeError("Input must be a list")
        
    def _ms(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = _ms(arr[:mid])
        right = _ms(arr[mid:])
        return _merge(left, right)
        
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
        
    return _ms(data)
