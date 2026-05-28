# UVA 11349 — Symmetric Matrix（手打版）
# 判斷 n×n 矩陣是否為「中心對稱矩陣」
# 條件：(1) 所有元素 >= 0  (2) M[i][j] == M[n-1-i][n-1-j]

def solve():
    T = int(input())  # 讀取測試組數
    for t in range(1, T + 1):
        n = int(input().split()[-1])  # 解析 "N = n" 格式，取最後一個 token
        # 讀取 n×n 矩陣
        m = [list(map(int, input().split())) for _ in range(n)]
        ok = True
        for i in range(n):
            for j in range(n):
                # 同時檢查：非負 且 中心對稱
                if m[i][j] < 0 or m[i][j] != m[n - 1 - i][n - 1 - j]:
                    ok = False
                    break
            if not ok:
                break
        print(f"Test #{t}: {'Symmetric.' if ok else 'Non-symmetric.'}")

solve()
