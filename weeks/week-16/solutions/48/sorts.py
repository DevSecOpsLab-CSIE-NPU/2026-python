def bubble_sort(data: list) -> list:
    result = data[:]
    n = len(result)
    for i in range(n):
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result


def quick_sort(data: list) -> list:
    if len(data) <= 1:
        return data[:]
    pivot = data[len(data) // 2]
    left = [x for x in data if x < pivot]
    middle = [x for x in data if x == pivot]
    right = [x for x in data if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def merge_sort(data: list) -> list:
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


def sorted_baseline(data: list) -> list:
    return sorted(data)


def quick_sort_fast(data: list) -> list:
    if len(data) <= 1:
        return data[:]
    result = data[:]
    _qsort_inplace(result, 0, len(result) - 1)
    return result


def _qsort_inplace(arr, low, high):
    while low < high:
        p = _partition(arr, low, high)
        if p - low < high - p:
            _qsort_inplace(arr, low, p - 1)
            low = p + 1
        else:
            _qsort_inplace(arr, p + 1, high)
            high = p - 1


def _partition(arr, low, high):
    pivot = arr[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]


def merge_sort_fast(data: list) -> list:
    result = data[:]
    n = len(result)
    step = 1
    while step < n:
        for left in range(0, n, step * 2):
            mid = left + step
            right = min(left + step * 2, n)
            if mid < right:
                _merge_inplace(result, left, mid, right)
        step *= 2
    return result


def _merge_inplace(arr, left, mid, right):
    left_part = arr[left:mid]
    right_part = arr[mid:right]
    i = j = 0
    k = left
    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1
    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1
    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1
