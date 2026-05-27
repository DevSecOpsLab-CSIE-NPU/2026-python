"""
UVA 11349 — 容易記憶版

使用 Python 的內建函式 all() 搭配生成式，
一行核心程式碼完成檢查，更容易記憶。
"""


def is_symmetric(matrix):
    """
    判斷二維方陣是否為中心對稱矩陣（簡潔版）

    使用 all() 一次檢查所有條件：
      - 所有元素 >= 0
      - 所有 M[i][j] == M[n-1-i][n-1-j]
    """
    n = len(matrix)
    # all() 搭配生成式，一次檢查全部條件
    return all(
        matrix[i][j] >= 0 and matrix[i][j] == matrix[n - 1 - i][n - 1 - j]
        for i in range(n)
        for j in range(n)
    )


def solve() -> None:
    """讀取標準輸入，輸出每筆測試資料的判斷結果"""
    t = int(input().strip())
    for case_no in range(1, t + 1):
        n = int(input().strip().split("=")[1].strip())
        matrix = [list(map(int, input().split())) for _ in range(n)]
        print(f"Test #{case_no}: {'Symmetric.' if is_symmetric(matrix) else 'Non-symmetric.'}")


if __name__ == "__main__":
    solve()
