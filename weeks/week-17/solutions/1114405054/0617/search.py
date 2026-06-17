def linear_search(data: list, target) -> int:
    if not isinstance(data, list):
        raise TypeError(f"data must be a list, got {type(data).__name__}")
    for i, value in enumerate(data):
        if value == target:
            return i
    return -1


def binary_search(data: list, target) -> int:
    """透過二元搜尋法尋找目標值的索引。

    警告：
        傳入的 data 必須是已升冪排序的 list。若傳入未排序的 data，
        本函式將不會主動拋出例外，但其行為未定義（可能回傳 -1 或錯誤的索引）。

    Args:
        data: 已排序的搜尋來源陣列（不可修改）。
        target: 欲尋找的目標值。

    Returns:
        int: 目標值的索引；若未找到或資料未排序，則回傳 -1。
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
