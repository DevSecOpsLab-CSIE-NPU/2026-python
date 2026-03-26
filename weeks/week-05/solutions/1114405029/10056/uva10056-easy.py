# UVA 10056 - What is the Probability ?
# easy 版本：使用最直觀方式實作


# 讀入測試資料組數
t = int(input())

# 逐組處理每一筆測試資料
for _ in range(t):
    # 讀入 n（玩家數）、p（成功機率）、i（目標玩家）
    n, p, i = input().split()

    # 轉換型態
    n = int(n)
    p = float(p)
    i = int(i)

    # 若成功機率為 0，代表永遠不會有人成功
    # 因此任何玩家的最終獲勝機率皆為 0
    if p == 0:
        print("0.0000")
    else:
        # q 為失敗機率
        q = 1 - p

        # 依公式計算第 i 位玩家最終獲勝的機率：
        # (q^(i-1) * p) / (1 - q^n)
        ans = (q ** (i - 1) * p) / (1 - q ** n)

        # 輸出結果（小數點後四位）
        print(f"{ans:.4f}")