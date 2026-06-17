def linear_search(data: list, target) -> int:
    for i, value in enumerate(data):
        if value == target:
            return i
    return -1


def binary_search(data: list, target) -> int:
    """Binary search.

    Precondition: data must be sorted in ascending order.
    Behaviour is undefined if precondition is violated.
    """
    low, high = 0, len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
