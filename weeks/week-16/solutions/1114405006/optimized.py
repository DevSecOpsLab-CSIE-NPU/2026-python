def _insertion_sort(data, left, right):
    for i in range(left + 1, right + 1):
        key = data[i]
        j = i - 1
        while j >= left and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key


def _hoare_partition(data, left, right):
    mid = (left + right) // 2
    pivot = data[mid]
    data[mid], data[right] = data[right], data[mid]
    i, j = left, right - 1
    while True:
        while data[i] < pivot:
            i += 1
        while data[j] > pivot:
            j -= 1
        if i >= j:
            break
        data[i], data[j] = data[j], data[i]
        i += 1
        j -= 1
    data[i], data[right] = data[right], data[i]
    return i


def _hybrid_quick(data, left, right):
    if right - left < 32:
        _insertion_sort(data, left, right)
        return
    pivot_idx = _hoare_partition(data, left, right)
    _hybrid_quick(data, left, pivot_idx - 1)
    _hybrid_quick(data, pivot_idx + 1, right)


def optimized_sort(data: list) -> list:
    if not data:
        raise ValueError("empty list")
    result = data[:]
    _hybrid_quick(result, 0, len(result) - 1)
    return result
