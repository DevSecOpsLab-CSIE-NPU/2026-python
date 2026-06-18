
"""Stage 2 — 三種搜尋：linear / binary / set。
 
三者都不修改傳入的 data。回傳型別刻意不一致，反映各自的語意：
  - linear_search / binary_search 回傳 index（找不到回 -1）
  - set_search 回傳 bool（是否存在）
 
Stage 2 不使用內建 `in`（對 list）與 `bisect`——那兩個是 Stage 3 的
baseline 對照組。set_search 用的是 set 的雜湊查找，屬於不同演算法，是這個
函式本身的定義機制，不在禁用範圍內。
"""
 
 
def linear_search(data: list, target) -> int:
    """線性搜尋：逐一比對，回傳第一個相等元素的 index，找不到回 -1。
 
    不修改傳入的 data。時間複雜度 O(n)。
    """
    for index, value in enumerate(data):
        if value == target:
            return index
    return -1
 
 
def binary_search(data: list, target) -> int:
    """二分搜尋：前提 data 已由小到大排序，回傳 target 的 index，找不到回 -1。
 
    不修改傳入的 data，時間複雜度 O(log n)。
 
    未排序的行為（自訂）：本函式不會幫你排序，也不會檢查是否已排序。若傳入
    未排序的 data，二分法的前提被破壞，回傳值未定義（可能回 -1，也可能回一個
    剛好落在中間的 index）。呼叫端負責先保證 data 已排序——此處刻意不偷偷排序，
    因為排序會改動/複製資料，且會把 O(log n) 的成本悄悄變成 O(n log n)。
    """
    lo = 0
    hi = len(data) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if data[mid] == target:
            return mid
        if data[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
 
 
def set_search(data: list, target) -> bool:
    """集合搜尋：用 set 的雜湊查找回傳 target 是否存在。
 
    不修改傳入的 data。建立 set 為 O(n)、單次查找平均 O(1)。
    注意：此函式每次呼叫都重建 set，所以單次查詢沒有優勢；它的價值要在
    「同一份資料先建一次 set、之後反覆查詢很多次」時才攤提得回來。
    """
    return target in set(data)