def linear_search(data: list, target) -> int:
    """逐一比對，回傳第一個符合索引，找不到回 -1。
    不會修改傳入的 data。
    """
    for i, v in enumerate(data):
        if v == target:
            return i
    return -1

def binary_search(data: list, target) -> int:
    """二分搜尋，前提：data 已依升冪排序（non-decreasing）。
    若收到未排序的 data，會直接 raise ValueError（以避免自行改變輸入或回傳在排序後的 index）。
    回傳 index 或 -1。
    """
    # 檢查是否已排序（簡單 O(n) 檢查）
    if any(data[i] > data[i+1] for i in range(len(data) - 1)):
        raise ValueError("binary_search requires sorted data (ascending)")

    lo, hi = 0, len(data) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1