def linear_search(data: list, target) -> int:
    """Perform a linear search on the given data.

    Args:
        data (list): The list to search through.
        target: The value to search for.

    Returns:
        int: The index of the target if found, otherwise -1.
    """
    for index, value in enumerate(data):
        if value == target:
            return index
    return -1


def binary_search(data: list, target) -> int:
    """Perform a binary search on the given sorted data.

    Args:
        data (list): The sorted list to search through.
        target: The value to search for.

    Returns:
        int: The index of the target if found, otherwise -1.

    Note:
        If the input data is not sorted, the behavior of this function is undefined.
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