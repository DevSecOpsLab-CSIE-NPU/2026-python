def linear_search(data: list, target) -> int:
    for i, v in enumerate(data):
        if v == target:
            return i
    return -1


def binary_search(data: list, target) -> int:
    """Binary search. data must be sorted in ascending order.
    If data is unsorted, behavior is undefined (may return incorrect index or fail to find target)."""
    left, right = 0, len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            return mid
        if data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
