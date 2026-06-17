_INSERTION_THRESHOLD = 16


def _insertion_sort(data: list, left: int, right: int) -> None:
    for i in range(left + 1, right + 1):
        key = data[i]
        j = i - 1
        while j >= left and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key


def bubble_sort_fast(data: list) -> list:
    result = data[:]
    n = len(result)
    left = 0
    right = n - 1
    while left < right:
        new_right = left
        for i in range(left, right):
            if result[i] > result[i + 1]:
                result[i], result[i + 1] = result[i + 1], result[i]
                new_right = i
        right = new_right
        if left >= right:
            break
        new_left = right
        for i in range(right, left, -1):
            if result[i - 1] > result[i]:
                result[i - 1], result[i] = result[i], result[i - 1]
                new_left = i
        left = new_left
    return result


def quick_sort_fast(data: list) -> list:
    result = data[:]
    _quick_sort_helper(result, 0, len(result) - 1)
    return result


def _quick_sort_helper(data: list, left: int, right: int) -> None:
    if right - left <= _INSERTION_THRESHOLD:
        _insertion_sort(data, left, right)
        return
    pivot = _median_of_three(data, left, right)
    i, j = left, right
    while i <= j:
        while data[i] < pivot:
            i += 1
        while data[j] > pivot:
            j -= 1
        if i <= j:
            data[i], data[j] = data[j], data[i]
            i += 1
            j -= 1
    if left < j:
        _quick_sort_helper(data, left, j)
    if i < right:
        _quick_sort_helper(data, i, right)


def _median_of_three(data: list, left: int, right: int):
    mid = (left + right) // 2
    a, b, c = data[left], data[mid], data[right]
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b
    data[left], data[mid], data[right] = a, b, c
    return b


def merge_sort_fast(data: list) -> list:
    if len(data) <= _INSERTION_THRESHOLD:
        result = data[:]
        _insertion_sort(result, 0, len(result) - 1)
        return result
    mid = len(data) // 2
    left = merge_sort_fast(data[:mid])
    right = merge_sort_fast(data[mid:])
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
