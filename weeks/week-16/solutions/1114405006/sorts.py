def bubble_sort(data: list) -> list:
    if not data:
        raise ValueError("empty list")
    result = data[:]
    n = len(result)
    for i in range(n):
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result


def _quick_sort(data: list) -> list:
    if len(data) <= 1:
        return data[:]
    pivot = data[0]
    left = [x for x in data[1:] if x <= pivot]
    right = [x for x in data[1:] if x > pivot]
    return _quick_sort(left) + [pivot] + _quick_sort(right)


def quick_sort(data: list) -> list:
    if not data:
        raise ValueError("empty list")
    return _quick_sort(data)


def _merge_sort(data: list) -> list:
    if len(data) <= 1:
        return data[:]
    mid = len(data) // 2
    left = _merge_sort(data[:mid])
    right = _merge_sort(data[mid:])
    i = j = 0
    result = []
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


def merge_sort(data: list) -> list:
    if not data:
        raise ValueError("empty list")
    return _merge_sort(data)
