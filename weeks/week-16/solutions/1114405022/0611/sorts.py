import random


def _validate_list(data):
    if not isinstance(data, list):
        raise TypeError(f"Expected list, got {type(data).__name__}")


def bubble_sort(data: list) -> list:
    _validate_list(data)
    result = data[:]
    n = len(result)
    for i in range(n):
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result


def quick_sort(data: list) -> list:
    _validate_list(data)
    if len(data) <= 1:
        return data[:]
    pivot = data[0]
    left = [x for x in data[1:] if x <= pivot]
    right = [x for x in data[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


def merge_sort(data: list) -> list:
    _validate_list(data)
    if len(data) <= 1:
        return data[:]
    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    return _merge(left, right)


def _merge(left: list, right: list) -> list:
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


def builtin_sort(data: list) -> list:
    _validate_list(data)
    return sorted(data)


def quick_sort_opt(data: list) -> list:
    _validate_list(data)
    if len(data) <= 1:
        return data[:]
    arr = data[:]
    _quick_sort_inplace(arr, 0, len(arr) - 1)
    return arr


def _quick_sort_inplace(arr, low, high):
    while low < high:
        if high - low < 20:
            _insertion_sort_range(arr, low, high)
            return
        pivot_idx = _partition(arr, low, high)
        if pivot_idx - low < high - pivot_idx:
            _quick_sort_inplace(arr, low, pivot_idx - 1)
            low = pivot_idx + 1
        else:
            _quick_sort_inplace(arr, pivot_idx + 1, high)
            high = pivot_idx - 1


def _partition(arr, low, high):
    pivot_idx = random.randint(low, high)
    arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def _insertion_sort_range(arr, low, high):
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key