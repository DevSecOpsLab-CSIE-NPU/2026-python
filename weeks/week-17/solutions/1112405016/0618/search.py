import bisect

# Global cache for optimized set search to avoid rebuilding the set each query
_SET_CACHE = {}


def linear_search(data: list, target) -> int:
    """線性搜尋：逐一比對，回傳 index，找不到回 -1"""
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1


def binary_search(data: list, target) -> int:
    """二分搜尋：前提 data 已排序；回傳 index 或 -1"""
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
    """雜湊搜尋（未優化）：每次呼叫都新建 set，回傳是否存在（bool）"""
    hash_set = set(data)
    return target in hash_set


# ==========================================
# Stage 3 加速版與 Baselines (優化與標準庫版)
# ==========================================


def linear_search_builtin(data: list, target) -> int:
    """線性搜尋（內建版）：使用 C 實作的 in 搭配 .index() 作為 baseline"""
    if target in data:
        return data.index(target)
    return -1


def binary_search_bisect(data: list, target) -> int:
    """二分搜尋（標準庫版）：使用 bisect 模組進行搜尋"""
    idx = bisect.bisect_left(data, target)
    if idx < len(data) and data[idx] == target:
        return idx
    return -1


def set_search_optimized(data: list, target) -> bool:
    """雜湊搜尋（演算法優化版）：使用全域快取，同一個 data 的 id 只建一次 set"""
    data_id = id(data)
    if data_id not in _SET_CACHE:
        _SET_CACHE[data_id] = set(data)
    return target in _SET_CACHE[data_id]
