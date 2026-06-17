def linear_search(data, target):
    if data is None:
        raise ValueError("data must not be None")
    for i, val in enumerate(data):
        if val == target:
            return i
    return -1


def binary_search(data, target):
    if data is None:
        raise ValueError("data must not be None")
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
