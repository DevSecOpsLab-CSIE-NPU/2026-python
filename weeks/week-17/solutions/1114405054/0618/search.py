def linear_search(data: list, target) -> int:
    if not isinstance(data, list):
        raise TypeError(f"data must be a list, got {type(data).__name__}")
    for i, value in enumerate(data):
        if value == target:
            return i
    return -1


def binary_search(data: list, target) -> int:
    """二元搜尋。

    警告: data 必須是已升冪排序的 list。
    傳入未排序 data 時行為未定義，可能回傳 -1 或錯誤索引。

    Args:
        data: 已排序 list（不可修改）。
        target: 目標值。

    Returns:
        找到回 index，否則回 -1。
    """
    if not isinstance(data, list):
        raise TypeError(f"data must be a list, got {type(data).__name__}")
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


def set_search(data: list, target) -> bool:
    if not isinstance(data, list):
        raise TypeError(f"data must be a list, got {type(data).__name__}")
    return target in set(data)
