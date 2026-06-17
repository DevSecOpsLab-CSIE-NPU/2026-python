def linear_search(data: list, target) -> int:
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1


def binary_search(data: list, target) -> int:
    for i in range(len(data) - 1):
        if data[i] > data[i + 1]:
            raise ValueError("data must be sorted in ascending order")

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
