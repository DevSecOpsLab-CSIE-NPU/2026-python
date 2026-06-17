def linear_search(data: list, target) -> int:
    for i, val in enumerate(data):
        if val == target:
            return i
    return -1


def binary_search(data: list, target) -> int:
    """
    Binary search. data must be sorted in ascending order.
    If data is unsorted, the behavior is undefined (caller's responsibility).
    Returns index of target or -1 if not found.
    """
    left, right = 0, len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
