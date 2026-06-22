def linear_search(data: list, target) -> int:
    """線性搜尋：逐一比對，回傳 index，找不到回 -1"""
    # 禁用 in，使用手寫迴圈
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1


def binary_search(data: list, target) -> int:
    """二分搜尋：前提 data 已排序；回傳 index 或 -1。

    若未排序，本實作不做內部排序或驗證，可能搜尋失敗並回傳 -1。
    """
    # 禁用 bisect，手寫二分搜尋
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
    """雜湊搜尋：用 set / hash 結構，回傳是否存在（bool）"""
    # 建立 set 結構並查詢
    hash_set = set(data)
    # 此處 in 作用於 set (雜湊查表)，非作用於 list (線性比對)
    return target in hash_set
