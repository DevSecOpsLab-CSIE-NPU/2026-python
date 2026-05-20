import sys


def calc_min_stones(L, S, T, stone_list):
    # 這個函式計算「最少踩到幾顆石子」。
    #
    # 參數說明：
    # L: 橋長（終點座標）
    # S: 每次最小跳躍距離
    # T: 每次最大跳躍距離
    # stone_list: 石子座標清單

    # 特例 1：如果 S == T，代表每次只能跳固定距離。
    # 這時青蛙落點序列是固定的：S, 2S, 3S, ...
    # 直接數這些落點中有幾個石子即可。
    if S == T:
        stone_set = set(stone_list)
        pos = S
        hit = 0
        while pos <= L:
            if pos in stone_set:
                hit += 1
            pos += S
        return hit

    # 一般情況（S < T）：使用「座標壓縮 + DP」。
    #
    # 為什麼要壓縮？
    # - L 最大可到 1e9，不能直接開長度 L 的 DP 陣列。
    #
    # 為什麼可以壓縮？
    # - S, T <= 10，跳躍範圍很小。
    # - 在很長的無石子區段中，超過某個長度後狀態效果會重複，
    #   因此可把「大空白」截成固定上限長度。
    # - 這裡使用 keep = S * T 當作保留長度。
    keep = S * T
    stones = sorted(stone_list)

    # new_stones: 壓縮後石子位置
    # prev_real: 前一顆石子在原座標的位置
    # prev_new: 前一顆石子在壓縮座標的位置
    new_stones = []
    prev_real = 0
    prev_new = 0

    # 逐顆石子做壓縮映射。
    # 若兩顆石子距離 gap 太大，就只保留 keep 的有效長度。
    for x in stones:
        gap = x - prev_real
        prev_new += min(gap, keep)
        new_stones.append(prev_new)
        prev_real = x

    # 把終點 L 也映射到壓縮座標。
    new_L = prev_new + min(L - prev_real, keep)

    # mark[i] = 1 代表壓縮座標 i 有石子，否則為 0。
    mark = [0] * (new_L + 1)
    for x in new_stones:
        if x <= new_L:
            mark[x] = 1

    # DP 定義：dp[i] = 到壓縮位置 i 時，最少踩石數。
    #
    # 因為題目規則是「跳到或跳過 L 就成功」，
    # 所以狀態上限要多開到 new_L + T，
    # 最後答案取 dp[new_L ... new_L+T] 的最小值。
    top = new_L + T
    INF = 10**9
    dp = [INF] * (top + 1)
    dp[0] = 0

    # 轉移：從每個可達位置 i，嘗試跳 S..T。
    for i in range(top + 1):
        if dp[i] == INF:
            continue

        for jump in range(S, T + 1):
            j = i + jump
            if j > top:
                continue

            # 若落點 j 在橋上且有石子，踩石成本 +1。
            # 若 j 已經超過 new_L，代表跳出橋，不再增加踩石。
            add = mark[j] if j <= new_L else 0
            if dp[i] + add < dp[j]:
                dp[j] = dp[i] + add

    # 回傳所有「已到達或跳過終點」狀態中的最小值。
    return min(dp[new_L : top + 1])


def solve(text):
    # 題目採 EOF 輸入：可能有多組測資，直到檔尾。
    # 使用 split() 把所有數字切成 token，再用指標 p 順序讀取。
    arr = text.split()
    p = 0
    out = []

    while p < len(arr):
        # 每組格式：
        # L
        # S T M
        # M 個石子位置
        L = int(arr[p])
        p += 1

        S = int(arr[p])
        T = int(arr[p + 1])
        M = int(arr[p + 2])
        p += 3

        stones = list(map(int, arr[p : p + M]))
        p += M

        # 每組答案一行。
        out.append(str(calc_min_stones(L, S, T, stones)))

    # 多組結果用換行串接。
    return "\n".join(out)


def main():
    # 從標準輸入讀完整內容，交給 solve() 後輸出。
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
