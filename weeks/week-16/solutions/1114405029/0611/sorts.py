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
    """Return a sorted copy using in-place quick sort on a copy."""
    result = data[:]
    _quick_sort_in_place(result, 0, len(result) - 1)
    return result


def _quick_sort_in_place(values: list, low: int, high: int) -> None:
    while low < high:
        if high - low <= 24:
            _insertion_sort_range(values, low, high)
            return

        pivot_index = _median_index(values, low, (low + high) // 2, high)
        values[pivot_index], values[high] = values[high], values[pivot_index]
        pivot = values[high]
        store_index = low

        for index in range(low, high):
            if values[index] < pivot:
                values[store_index], values[index] = values[index], values[store_index]
                store_index += 1

        values[store_index], values[high] = values[high], values[store_index]

        left_size = store_index - low
        right_size = high - store_index

        if left_size < right_size:
            _quick_sort_in_place(values, low, store_index - 1)
            low = store_index + 1
        else:
            _quick_sort_in_place(values, store_index + 1, high)
            high = store_index - 1


def _median_index(values: list, first: int, second: int, third: int) -> int:
    first_value = values[first]
    second_value = values[second]
    third_value = values[third]

    if first_value <= second_value <= third_value or third_value <= second_value <= first_value:
        return second
    if second_value <= first_value <= third_value or third_value <= first_value <= second_value:
        return first
    return third


def _insertion_sort_range(values: list, low: int, high: int) -> None:
    for index in range(low + 1, high + 1):
        current = values[index]
        position = index - 1
        while position >= low and values[position] > current:
            values[position + 1] = values[position]
            position -= 1
        values[position + 1] = current


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
