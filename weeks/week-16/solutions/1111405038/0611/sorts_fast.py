"""Stage 3 — 加速版排序實作（演算法優化版）"""


def quick_sort_fast(data: list) -> list:
    """優化 quick sort：median-of-three + 小區間改 insertion sort。"""
    arr = list(data)
    if len(arr) <= 1:
        return arr
    _quick_sort(arr, 0, len(arr) - 1)
    return arr


def _quick_sort(arr: list, low: int, high: int) -> None:
    while low < high:
        # 小區間用 insertion sort，降低遞迴與 partition 常數成本
        if high - low + 1 <= 16:
            _insertion_sort_range(arr, low, high)
            return

        pivot_index = _median_of_three(arr, low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        p = _partition(arr, low, high)

        # 先遞迴較小分段，降低最差遞迴深度
        if p - low < high - p:
            _quick_sort(arr, low, p - 1)
            low = p + 1
        else:
            _quick_sort(arr, p + 1, high)
            high = p - 1


def _partition(arr: list, low: int, high: int) -> int:
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def _median_of_three(arr: list, low: int, high: int) -> int:
    mid = (low + high) // 2
    a = arr[low]
    b = arr[mid]
    c = arr[high]

    if a <= b <= c or c <= b <= a:
        return mid
    if b <= a <= c or c <= a <= b:
        return low
    return high


def _insertion_sort_range(arr: list, low: int, high: int) -> None:
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
