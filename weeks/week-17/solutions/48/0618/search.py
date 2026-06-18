def linear_search(data, target):
    if data is None or target is None:
        raise TypeError("data and target must not be None")
    for i, value in enumerate(data):
        if value == target:
            return i
    return -1


def binary_search(data, target):
    if data is None or target is None:
        raise TypeError("data and target must not be None")
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


def set_search(data, target):
    if data is None or target is None:
        raise TypeError("data and target must not be None")
    return target in set(data)
