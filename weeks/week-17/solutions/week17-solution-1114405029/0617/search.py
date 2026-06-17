"""Search algorithms for the 0617 assignment."""


def linear_search(data: list, target) -> int:
    """Return the index of target in data, or -1 when target is absent."""
    for index, value in enumerate(data):
        if value == target:
            return index
    return -1


def binary_search(data: list, target) -> int:
    """Return the index of target in sorted data, or -1 when absent.

    Precondition:
        data must already be sorted in ascending order. This function does not
        validate sorting because that would add an O(n) scan before the
        O(log n) search.
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
