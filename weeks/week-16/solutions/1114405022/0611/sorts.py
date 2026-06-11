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
    if len(data) < 20:
        return _insertion_sort(data[:])
    pivot = _median_of_three(data)
    left = [x for x in data if x < pivot]
    mid = [x for x in data if x == pivot]
    right = [x for x in data if x > pivot]
    return quick_sort_opt(left) + mid + quick_sort_opt(right)


def _insertion_sort(data: list) -> list:
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data


def _median_of_three(data: list) -> list:
    first, mid, last = data[0], data[len(data) // 2], data[-1]
    return sorted([first, mid, last])[1]
