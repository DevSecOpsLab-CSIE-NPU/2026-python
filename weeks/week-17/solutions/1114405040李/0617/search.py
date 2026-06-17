"""Linear and binary search implementations."""


def linear_search(data: list, target) -> int:
    """Return the index of target in data, or -1 when target is not present."""
    for index, item in enumerate(data):
        if item == target:
            return index
    return -1


def binary_search(data: list, target) -> int:
    """Return the index of target in sorted data, or -1 when target is absent.

    Precondition:
        data must already be sorted in ascending order. This function does not
        sort or mutate the input list.
    """
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
