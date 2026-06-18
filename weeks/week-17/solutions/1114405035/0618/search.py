def linear_search(data: list, target) -> int:
    if not isinstance(data, list):
        raise TypeError("data must be a list")
    for i, val in enumerate(data):
        if val == target:
            return i
    return -1


def binary_search(data: list, target) -> int:
    if not isinstance(data, list):
        raise TypeError("data must be a list")
    # binary_search assuming data is sorted. Undefined behavior if not sorted.
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def set_search(data: list, target) -> bool:
    if not isinstance(data, list):
        raise TypeError("data must be a list")
    data_set = set(data)
    return target in data_set
