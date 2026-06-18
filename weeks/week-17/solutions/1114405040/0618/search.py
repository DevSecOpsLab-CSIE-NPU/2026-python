"""Linear, binary, and set-backed search examples."""


def linear_search(data: list, target) -> int:
    """Return the first index of target in data, or -1 when not found."""
    for index, value in enumerate(data):
        if value == target:
            return index
    return -1


def binary_search(data: list, target) -> int:
    """Return an index of target in sorted data, or -1 when not found.

    Precondition: data is already sorted in ascending order. The function does
    not sort or otherwise mutate the input list.
    """
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        value = data[mid]
        if value == target:
            return mid
        if value < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def set_search(data: list, target) -> bool:
    """Return whether target appears in data using a temporary set."""
    return target in set(data)
