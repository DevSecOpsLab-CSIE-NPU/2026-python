"""Search algorithms for the 0617 assignment."""

from bisect import bisect_left


def linear_search(data: list, target) -> int:
    """Return the index of target in data, or -1 when target is absent."""
    for index, value in enumerate(data):
        if value == target:
            return index
    return -1


def binary_search(data: list, target) -> int:
    """Return the first index of target in sorted data, or -1 when absent.

    Precondition:
        data must already be sorted in ascending order. This function does not
        validate sorting because that would add an O(n) scan before the
        O(log n) search.
    """
    index = bisect_left(data, target)
    if index != len(data) and data[index] == target:
        return index
    return -1
