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


def optimized_bubble_sort(data: list) -> list:
    """Return a sorted copy using bubble sort with a shrinking boundary."""
    result = data[:]
    end = len(result) - 1

    while end > 0:
        last_swap = 0
        for index in range(end):
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = result[index + 1], result[index]
                last_swap = index
        end = last_swap

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


def optimized_quick_sort(data: list) -> list:
    """Return a sorted copy using quick sort with median pivot and insertion sort."""
    values = data[:]
    return _optimized_quick(values)


def _optimized_quick(values: list) -> list:
    if len(values) <= 16:
        return _insertion_sort(values)

    first = values[0]
    middle = values[len(values) // 2]
    last = values[-1]
    pivot = _median_of_three(first, middle, last)
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

    return _optimized_quick(lower) + equal + _optimized_quick(higher)


def _median_of_three(first, second, third):
    if first > second:
        first, second = second, first
    if second > third:
        second, third = third, second
    if first > second:
        first, second = second, first
    return second


def _insertion_sort(data: list) -> list:
    result = data[:]

    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current

    return result


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
