def linear_search(data: list, target) -> int:
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1


def binary_search(data: list, target) -> int:
    """Binary search on sorted list.
    If data is not sorted, behavior is undefined (no check performed).
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
