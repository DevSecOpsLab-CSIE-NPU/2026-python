def bubble_sort(data: list) -> list:
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
    arr = list(data)
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return quick_sort(less) + equal + quick_sort(greater)


def quick_sort_fast(data: list) -> list:
    arr = list(data)
    if len(arr) <= 1:
        return arr

    _quick_sort_inplace(arr, 0, len(arr) - 1)
    return arr


def merge_sort(data: list) -> list:
    arr = list(data)
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)


def _merge(left: list, right: list) -> list:
    result = []
    i = 0
    j = 0

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


def _quick_sort_inplace(arr: list, lo: int, hi: int) -> None:
    while lo < hi:
        if hi - lo < 16:
            _insertion_sort_range(arr, lo, hi)
            return

        mid = (lo + hi) // 2
        pivot = sorted((arr[lo], arr[mid], arr[hi]))[1]
        i = lo
        j = hi
        while i <= j:
            while arr[i] < pivot:
                i += 1
            while arr[j] > pivot:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1

        if (j - lo) < (hi - i):
            if lo < j:
                _quick_sort_inplace(arr, lo, j)
            lo = i
        else:
            if i < hi:
                _quick_sort_inplace(arr, i, hi)
            hi = j


def _insertion_sort_range(arr: list, lo: int, hi: int) -> None:
    for i in range(lo + 1, hi + 1):
        value = arr[i]
        j = i - 1
        while j >= lo and arr[j] > value:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = value
