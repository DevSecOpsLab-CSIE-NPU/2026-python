def linear_search(data: list, target) -> int:
    for i, val in enumerate(data):
        if val == target:
            return i
    return -1


def binary_search(data: list, target) -> int:
    lo, hi = 0, len(data) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if data[mid] == target:
            return mid
        if data[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def set_search(data: list, target) -> bool:
    return target in set(data)
