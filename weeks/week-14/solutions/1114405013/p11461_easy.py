"""
UVA 11461 — 容易記憶版

用 while 迴圈逐一產生完全平方數，不用開根號運算，
直覺好懂，容易記憶。
"""


def count_square_numbers(a, b):
    """
    計算閉區間 [a, b] 中完全平方數的個數（直覺版）

    從 1 開始往上檢查每個數的平方是否落在 [a, b] 範圍內，
    不需要用到 math 函式庫。
    """
    count = 0
    i = 1
    while True:
        square = i * i
        if square > b:
            break
        if square >= a:
            count += 1
        i += 1
    return count


def solve() -> None:
    """讀取標準輸入，每行 a b，直到 a=b=0 結束"""
    while True:
        a, b = map(int, input().split())
        if a == 0 and b == 0:
            break
        print(count_square_numbers(a, b))


if __name__ == "__main__":
    solve()
