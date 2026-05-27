"""
UVA 11349 — Symmetric Matrix（對稱矩陣）
ZeroJudge e513

功能：判斷 n×n 方陣是否為中心對稱矩陣
定義：
  1. 所有元素 >= 0
  2. M[i][j] = M[n-1-i][n-1-j]（中心對稱）
"""


def is_symmetric(matrix):
    """
    判斷二維方陣是否為中心對稱矩陣

    參數：
        matrix: list[list[int]] — n×n 方陣

    回傳值：
        bool — 對稱回傳 True，否則 False
    """
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            # 條件一：元素不可為負數
            if matrix[i][j] < 0:
                return False
            # 條件二：中心對稱檢查
            if matrix[i][j] != matrix[n - 1 - i][n - 1 - j]:
                return False
    return True


def solve() -> None:
    """讀取標準輸入，輸出每筆測試資料的判斷結果"""
    t = int(input().strip())
    for case_no in range(1, t + 1):
        line = input().strip()
        # 輸入格式：N = n
        n = int(line.split("=")[1].strip())
        matrix = []
        for _ in range(n):
            row = list(map(int, input().split()))
            matrix.append(row)
        if is_symmetric(matrix):
            print(f"Test #{case_no}: Symmetric.")
        else:
            print(f"Test #{case_no}: Non-symmetric.")


if __name__ == "__main__":
    solve()
