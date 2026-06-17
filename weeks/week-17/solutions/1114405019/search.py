"""0617 任務二 — linear_search 與 binary_search(輕量評估,不要求完整紅綠燈)。"""


def linear_search(data: list, target) -> int:
    """逐一比對 data,回傳 target 第一次出現的 index;找不到回 -1。

    不修改傳入的 data。
    """
    for i, value in enumerate(data):
        if value == target:
            return i
    return -1


def binary_search(data: list, target) -> int:
    """在已排序的 data 中二分搜尋 target,回傳 index;找不到回 -1。

    前提:data 必須是「已排序」(由小到大)的 list,否則結果不保證正確
    ——本實作不會自動排序,也不會檢查是否已排序;收到未排序的 data 時,
    行為等同對一個假設已排序的陣列做二分搜尋,可能找不到實際存在的
    target,也可能誤判存在不存在的值,這是設計上接受的行為,呼叫端
    自行負責保證輸入已排序。

    不修改傳入的 data。
    """
    low, high = 0, len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        if data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
