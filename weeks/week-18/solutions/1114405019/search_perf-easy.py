"""
簡化／好記版本：只留下 CPE 當場手打時真正需要記住的兩個函式。
不含 timeit、雷達圖、檔案輸入這些「裝飾」，方便練習時專心背邏輯。
"""


def linear_search(arr, target):
    """
    線性搜尋：從第一個元素開始，一個一個比對到底。

    口訣：「從頭找到尾，找到就回頭」
    - 不要求 arr 已排序，所以隨機亂序的陣列也能用。
    - cmp 用來計算總共比了幾次，每比一次 +1。
    """
    cmp = 0
    for i in range(len(arr)):
        cmp += 1
        if arr[i] == target:
            return i, cmp          # 找到了，立刻回頭，不要多比
    return None, cmp                # 比到最後都沒有，才算 NOT FOUND


def binary_search(arr, target):
    """
    二分搜尋：每次都看中間那個，比較完直接砍掉一半。

    口訣：「先看中間，比大砍右，比小砍左」
    - 前提：arr 一定要先排好（升冪），否則砍半的邏輯會錯。
    - lo / hi 是目前還沒被排除的範圍兩端（含 lo 和 hi 本身）。
    - 迴圈條件用 lo <= hi（不是 <），因為當 lo == hi 時，
      代表還剩 1 個元素沒檢查，這就是最容易漏掉邊界的地方。
    """
    cmp = 0
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2        # 中間位置，整數除法直接捨去小數
        cmp += 1
        if arr[mid] == target:
            return mid, cmp          # 中間就是答案，回頭
        elif arr[mid] < target:
            lo = mid + 1              # target 比中間大 -> 答案在右半邊，砍掉左邊（含 mid）
        else:
            hi = mid - 1              # target 比中間小 -> 答案在左半邊，砍掉右邊（含 mid）
    return None, cmp                  # lo > hi 代表範圍已經砍到空，確定找不到
