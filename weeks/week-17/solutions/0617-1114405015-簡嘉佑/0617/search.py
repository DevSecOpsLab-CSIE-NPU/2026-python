"""Search functions for runtime comparison."""

from __future__ import annotations


def linear_search(data: list, target) -> int:
    """Return the index of target in data, or -1 if not found."""
    for idx, value in enumerate(data):
        if value == target:
            return idx
    return -1


def binary_search(data: list, target) -> int:
    """Return index of target in sorted data, or -1 if not found.

    The input list must be sorted in non-decreasing order.
    If data is not sorted, the result is undefined and not guaranteed.
    """
    left = 0
    right = len(data) - 1

    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            return mid
        if data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
