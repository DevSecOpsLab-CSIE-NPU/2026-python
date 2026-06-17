"""Search implementations for week-17 0617 practice."""


def linear_search(data: list, target) -> int:
    """Return the index of target in data, or -1 if not found."""
    for index, value in enumerate(data):
        if value == target:
            return index
    return -1


def binary_search(data: list, target) -> int:
    """Return index of target in sorted data, or -1 if not found.

    Behavior on unsorted input:
        This function does not validate whether data is sorted.
        If data is unsorted, returned result is undefined and may be incorrect.
    """
    left, right = 0, len(data) - 1
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
