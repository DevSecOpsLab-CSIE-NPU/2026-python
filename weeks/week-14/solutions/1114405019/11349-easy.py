# UVA 11349 — Symmetric Matrix（AI 簡單版）
# 判斷一個 n×n 矩陣是否為「中心對稱矩陣」
#
# 判斷條件：
#   (1) 所有元素均非負（>= 0）
#   (2) 對所有 i, j 滿足：M[i][j] == M[n-1-i][n-1-j]（注意：Python 索引從 0 開始）


def is_symmetric(matrix, n):
    # all() 搭配生成器：只要有一個條件不成立就立即返回 False
    return all(
        matrix[i][j] >= 0 and matrix[i][j] == matrix[n - 1 - i][n - 1 - j]
        for i in range(n)
        for j in range(n)
    )


T = int(input())
for t in range(1, T + 1):
    # 輸入格式為 "N = n"，取最後一個 token 轉整數
    n = int(input().split()[-1])
    # 讀取 n 行 n 個整數，組成二維矩陣
    matrix = [list(map(int, input().split())) for _ in range(n)]
    result = "Symmetric." if is_symmetric(matrix, n) else "Non-symmetric."
    print(f"Test #{t}: {result}")
