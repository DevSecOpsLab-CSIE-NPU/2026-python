"""Search helpers for Stage 2."""


def linear_search(data, target):
    for index, value in enumerate(data):
        if value == target:
            return index
    return -1


def binary_search(data, target):
    """Return the index of target in sorted data, or -1 for unsorted input.

    The function requires data to be sorted in non-decreasing order. If the
    input is not sorted, it returns -1 instead of searching.
    """

    if any(data[index] > data[index + 1] for index in range(len(data) - 1)):
        return -1

    left = 0
    right = len(data) - 1

    while left <= right:
        middle = (left + right) // 2
        value = data[middle]

        if value == target:
            return middle
        if value < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1


def set_search(data, target):
    return target in set(data)