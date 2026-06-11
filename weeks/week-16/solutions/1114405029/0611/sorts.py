"""Sorting algorithms for the 6/11 sorting lab."""


def bubble_sort(data: list) -> list:
    """Return a sorted copy of data using bubble sort."""
    result = data[:]
    n = len(result)

    for end in range(n - 1, 0, -1):
        for index in range(end):
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = result[index + 1], result[index]

    return result


def quick_sort(data: list) -> list:
    """Return a sorted copy of data using quick sort."""
    values = data[:]

    if len(values) <= 1:
        return values

    pivot = values[len(values) // 2]
    lower = []
    equal = []
    higher = []

    for value in values:
        if value < pivot:
            lower.append(value)
        elif value > pivot:
            higher.append(value)
        else:
            equal.append(value)

    return quick_sort(lower) + equal + quick_sort(higher)


def merge_sort(data: list) -> list:
    """Return a sorted copy of data using merge sort."""
    values = data[:]

    if len(values) <= 1:
        return values

    middle = len(values) // 2
    left = merge_sort(values[:middle])
    right = merge_sort(values[middle:])
    return _merge(left, right)


def _merge(left: list, right: list) -> list:
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged
