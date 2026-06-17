from timing import timeit


def linear_search(data: list, target) -> int:
    """
    Search target by checking each element from left to right.

    Args:
        data (list): Input list.
        target: Value to search for.

    Returns:
        int: Index of target if found, otherwise -1.

    Note:
        This function does not modify data.
    """
    for index, value in enumerate(data):
        if value == target:
            return index
    return -1


def binary_search(data: list, target) -> int:
    """
    Search target using binary search.

    Args:
        data (list): Sorted input list.
        target: Value to search for.

    Returns:
        int: Index of target if found, otherwise -1.

    Note:
        This function assumes data is already sorted in ascending order.
        If data is not sorted, the result is undefined.
        This function does not modify data.
    """
    left = 0
    right = len(data) - 1

    while left <= right:
        mid = (left + right) // 2

        if data[mid] == target:
            return mid
        if data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


@timeit(repeat=5)
def timed_linear_search(data, target):
    return linear_search(data, target)


@timeit(repeat=5)
def timed_binary_search(data, target):
    return binary_search(data, target)


if __name__ == "__main__":
    data = list(range(100000))
    target = 99999

    linear_result = timed_linear_search(data, target)
    binary_result = timed_binary_search(data, target)

    print("linear_search result:", linear_result)
    print("linear_search records:", timed_linear_search.records)
    print("linear_search average:", timed_linear_search.last_elapsed)

    print("binary_search result:", binary_result)
    print("binary_search records:", timed_binary_search.records)
    print("binary_search average:", timed_binary_search.last_elapsed)