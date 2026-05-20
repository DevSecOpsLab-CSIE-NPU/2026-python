def solve():
    import sys

    # 讀取所有輸入
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    # 解析輸入資料
    L = int(input_data[0])
    S = int(input_data[1])
    T = int(input_data[2])
    M = int(input_data[3])

    # 讀取 M 個石子的位置
    stones = [int(x) for x in input_data[4 : 4 + M]]

    # 情況 1：當 S == T 時，步長固定，直接計算有多少石子是 S 的倍數
    if S == T:
        ans = sum(1 for stone in stones if stone % S == 0)
        print(ans)
        return

    # 情況 2：當 S < T 時，需要進行路徑壓縮
    stones.sort()

    # 為了方便處理，加入起點 0（雖然起點沒石子，但方便計算第一顆石子的距離）
    pos = [0] + stones + [L]
    new_pos = [0] * len(pos)

    # 路徑壓縮核心：若兩點距離大於 T，則將其壓縮
    # 這裡使用 T 作為基準，大於 T 的距離可以縮減為 (diff % T) + T
    for i in range(1, len(pos)):
        diff = pos[i] - pos[i - 1]
        if diff > T:
            new_pos[i] = new_pos[i - 1] + (diff % T + T)
        else:
            new_pos[i] = new_pos[i - 1] + diff

    # 壓縮後的終點位置
    new_L = new_pos[-1]

    # 建立一個集合，紀錄壓縮後哪些座標有石子（不包含起點和終點）
    stone_set = set(new_pos[1:-1])

    # 初始化 DP 陣列，求最小值故初始化為無限大 (inf)
    # 陣列長度需要到 new_L + T，因為青蛙可能會跳過終點
    max_len = new_L + T + 1
    dp = [float("inf")] * max_len
    dp[0] = 0  # 起點踩到的石子數為 0

    # 動態規劃轉移
    for i in range(1, max_len):
        # 檢查從哪些先前的點可以跳到點 i
        for j in range(S, T + 1):
            if i - j >= 0:
                dp[i] = min(dp[i], dp[i - j])

        # 如果點 i 有石子，踩上去代價 +1
        if i in stone_set:
            dp[i] += 1

    # 最終答案為：跳到「終點」或「跳過終點」的所有狀態中的最小值
    ans = min(dp[new_L : max_len])
    print(ans)


# 執行主程式
if __name__ == "__main__":
    solve()