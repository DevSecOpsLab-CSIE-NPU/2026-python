import sys
from math import gcd


def solve(data):
    """
    直觀版本解法。

    本題重點：
    1. 橋長 L 很大，不能直接開 dp 到 L。
    2. 石子最多只有 100 顆，可以根據石子位置壓縮距離。
    3. 壓縮後再做動態規劃。
    """

    values = data.split()

    if not values:
        return ""

    pos = 0

    # 讀取橋長。
    L = int(values[pos])
    pos += 1

    # 讀取最小跳距 S、最大跳距 T、石子數 M。
    S = int(values[pos])
    T = int(values[pos + 1])
    M = int(values[pos + 2])
    pos += 3

    # 讀取所有石子位置。
    stones = []

    for _ in range(M):
        stones.append(int(values[pos]))
        pos += 1

    # 石子位置一定要排序，
    # 因為後面要計算相鄰石子之間的距離。
    stones.sort()

    # 特殊情況：
    # 如果 S == T，代表青蛙每次只能跳固定距離。
    # 此時青蛙會落在 S, 2S, 3S, ... 這些位置。
    # 所以只要統計哪些石子位置可以被 S 整除即可。
    if S == T:
        answer = 0

        for stone in stones:
            if stone % S == 0:
                answer += 1

        return str(answer)

    # 計算 S 到 T 的最小公倍數。
    # 這個值用於距離壓縮時保留長距離的週期特性。
    period = 1

    for number in range(S, T + 1):
        period = period // gcd(period, number) * number

    # 設定安全距離。
    # 如果兩個重要位置中間距離超過 safe_limit，
    # 就可以把這段很長的無石子區間壓短。
    safe_limit = period + T * 10

    # compressed_stones 用來記錄石子壓縮後的位置。
    compressed_stones = []

    # original_prev 是上一個原始重要位置。
    # 一開始從起點 0 開始。
    original_prev = 0

    # compressed_now 是目前壓縮後的位置。
    compressed_now = 0

    # 逐一處理每顆石子。
    for stone in stones:
        # gap 是原始座標中，上一個重要位置到目前石子的距離。
        gap = stone - original_prev

        # 如果 gap 太大，代表中間有一大段沒有石子。
        # 這種距離不需要完整保留，可以縮短。
        if gap > safe_limit:
            gap = safe_limit + gap % period

        # 更新壓縮後位置。
        compressed_now += gap

        # 記錄目前石子的壓縮位置。
        compressed_stones.append(compressed_now)

        # 更新上一個原始重要位置。
        original_prev = stone

    # 最後還要處理最後一顆石子到終點 L 的距離。
    last_gap = L - original_prev

    if last_gap > safe_limit:
        last_gap = safe_limit + last_gap % period

    compressed_L = compressed_now + last_gap

    # 將壓縮後石子位置放進 set，
    # 方便快速判斷某個位置是否有石子。
    stone_set = set(compressed_stones)

    # 因為青蛙跳到或跳過終點都算成功，
    # 所以 DP 至少要做到 compressed_L + T。
    max_position = compressed_L + T

    # 設定一個很大的數字，代表目前無法到達。
    INF = 10 ** 9

    # dp[i] 表示青蛙跳到位置 i 時，最少踩到幾顆石子。
    dp = [INF] * (max_position + 1)

    # 起點沒有石子，所以成本為 0。
    dp[0] = 0

    # 開始填 DP 表。
    for i in range(1, max_position + 1):
        # best 表示跳到 i 之前，所有可能來源位置中的最小成本。
        best = INF

        # 青蛙可以跳 S 到 T 格。
        for jump in range(S, T + 1):
            previous = i - jump

            # previous >= 0 才是合法來源位置。
            if previous >= 0:
                if dp[previous] < best:
                    best = dp[previous]

        # 如果 i 這個位置有石子，踩到石子數要加 1。
        if i in stone_set:
            dp[i] = best + 1
        else:
            dp[i] = best

    # 青蛙只要跳到 compressed_L 或更遠就成功。
    # 因此答案是 compressed_L 到 compressed_L + T 中最小的 dp。
    answer = min(dp[compressed_L:max_position + 1])

    return str(answer)


def main():
    """
    從標準輸入讀取資料，輸出答案。
    """

    data = sys.stdin.read()
    print(solve(data))


if __name__ == "__main__":
    main()