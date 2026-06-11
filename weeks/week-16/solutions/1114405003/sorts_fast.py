INSERTION_CUTOFF = 16


def _insertion_sort(data, left, right):
    for i in range(left + 1, right + 1):
        key = data[i]
        j = i - 1
        while j >= left and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key


def _median_of_three(data, left, right):
    mid = (left + right) // 2
    if data[left] > data[mid]:
        data[left], data[mid] = data[mid], data[left]
    if data[left] > data[right]:
        data[left], data[right] = data[right], data[left]
    if data[mid] > data[right]:
        data[mid], data[right] = data[right], data[mid]
    data[mid], data[right - 1] = data[right - 1], data[mid]
    return data[right - 1]


def _quick_sort_fast_inplace(data, left, right):
    if right - left + 1 <= INSERTION_CUTOFF:
        _insertion_sort(data, left, right)
        return
    pivot = _median_of_three(data, left, right)
    i, j = left, right - 1
    while True:
        i += 1
        while data[i] < pivot:
            i += 1
        j -= 1
        while data[j] > pivot:
            j -= 1
        if i >= j:
            break
        data[i], data[j] = data[j], data[i]
    data[i], data[right - 1] = data[right - 1], data[i]
    _quick_sort_fast_inplace(data, left, i - 1)
    _quick_sort_fast_inplace(data, i + 1, right)


def quick_sort_fast(data: list) -> list:
    result = data.copy()
    if len(result) <= 1:
        return result
    _quick_sort_fast_inplace(result, 0, len(result) - 1)
    return result


def builtin_sorted(data: list) -> list:
    return sorted(data)
