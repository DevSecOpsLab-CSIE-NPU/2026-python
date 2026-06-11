def bubble_sort(data: list) -> list:
    result = list(data)
    n = len(result)
    for i in range(n):
        for j in range(n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result


def quick_sort(data: list) -> list:
    result = list(data)
    _qs(result, 0, len(result) - 1)
    return result


def _qs(arr, low, high):
    if low < high:
        pi = _partition(arr, low, high)
        _qs(arr, low, pi - 1)
        _qs(arr, pi + 1, high)


def _partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def merge_sort(data: list) -> list:
    if len(data) <= 1:
        return list(data)
    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
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
