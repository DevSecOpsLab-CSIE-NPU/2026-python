import sys
from math import gcd


def lcm(a, b):
    """
    計算兩個整數 a、b 的最小公倍數。

    在距離壓縮時，我們會使用 S 到 T 的最小公倍數，
    目的是盡量保留長距離空白區段的週期性。
    """

    return a // gcd(a, b) * b


def calculate_period(start, end):
    """
    計算 start 到 end 之間所有整數的最小公倍數。

    例如：
    start = 2, end = 5
    就會計算 lcm(2, 3, 4, 5)。

    本題 S、T 最大只有 10，
    所以這個計算非常小。
    """

    period = 1

    for value in range(start, end + 1):
        period = lcm(period, value)

    return period


def compress_positions(length, stones, s, t):
    """
    將原始橋長與石子位置壓縮成較短的座標。

    參數：
    length：原始橋長 L
    stones：排序後的石子位置
    s：最小跳距
    t：最大跳距

    回傳：
    compressed_length：壓縮後的橋長
    compressed_stones：壓縮後的石子位置列表

    為什麼要壓縮：
    L 最大可能是 10^9，不能直接開 dp 陣列。
    但石子最多只有 100 顆，真正重要的是石子附近。
    長距離無石子的區段可以縮短。
    """

    # 使用 S 到 T 的最小公倍數作為週期參考。
    period = calculate_period(s, t)

    # 安全距離：
    # period 用來保留週期性，
    # t * 10 用來保留足夠長的空白緩衝區。
    limit = period + t * 10

    compressed_stones = []

    # previous_original 表示上一個重要原始座標。
    # 一開始是起點 0。
    previous_original = 0

    # current_compressed 表示目前壓縮後座標。
    current_compressed = 0

    for stone in stones:
        # 計算原始座標中，上一個重要位置到目前石子的距離。
        gap = stone - previous_original

        # 如果距離太長，就進行壓縮。
        # 保留 gap % period，是為了降低可達性被破壞的機率。
        if gap > limit:
            gap = limit + gap % period

        # 更新壓縮後座標。
        current_compressed += gap

        # 記錄目前石子在壓縮座標中的位置。
        compressed_stones.append(current_compressed)

        # 更新上一個原始重要位置。
        previous_original = stone

    # 最後還要處理最後一顆石子到終點 L 的距離。
    final_gap = length - previous_original

    if final_gap > limit:
        final_gap = limit + final_gap % period

    compressed_length = current_compressed + final_gap

    return compressed_length, compressed_stones


def solve(data):
    """
    處理完整輸入資料，回傳答案字串。

    本題輸入是一組測試資料：
    第一行：L
    第二行：S T M
    第三行：M 個石子位置
    """

    tokens = data.split()

    if not tokens:
        return ""

    index = 0

    # 讀取橋長 L。
    length = int(tokens[index])
    index += 1

    # 讀取 S、T、M。
    s = int(tokens[index])
    t = int(tokens[index + 1])
    m = int(tokens[index + 2])
    index += 3

    # 讀取 M 顆石子位置。
    stones = []

    for _ in range(m):
        stones.append(int(tokens[index]))
        index += 1

    # 石子位置必須排序，才能計算相鄰距離並進行壓縮。
    stones.sort()

    # 特殊情況：
    # 如果 s == t，青蛙每次只能跳固定距離 s。
    # 能踩到的位置只會是 s 的倍數。
    if s == t:
        count = 0

        for stone in stones:
            if stone % s == 0:
                count += 1

        return str(count)

    # 一般情況：
    # 先把巨大座標壓縮成可以 DP 的大小。
    compressed_length, compressed_stones = compress_positions(length, stones, s, t)

    # 將石子位置轉成 set，加速判斷某個座標是否有石子。
    stone_set = set(compressed_stones)

    # DP 陣列需要開到 compressed_length + t。
    # 因為只要跳到或超過終點就算成功。
    end_position = compressed_length + t

    # INF 代表目前無法到達或成本非常大。
    inf = 10 ** 9

    # dp[i] 表示跳到壓縮座標 i 時，最少踩到幾顆石子。
    dp = [inf] * (end_position + 1)

    # 起點沒有石子，所以成本為 0。
    dp[0] = 0

    # 從座標 1 開始依序計算。
    for position in range(1, end_position + 1):
        best_previous = inf

        # 青蛙可以從 position - jump 跳到 position。
        # jump 的範圍是 s 到 t。
        for jump in range(s, t + 1):
            previous_position = position - jump

            if previous_position >= 0:
                best_previous = min(best_previous, dp[previous_position])

        # 如果目前位置有石子，踩到成本要加 1。
        stone_cost = 1 if position in stone_set else 0

        dp[position] = best_previous + stone_cost

    # 青蛙只要到達 compressed_length 或超過它就算過河。
    answer = min(dp[compressed_length:end_position + 1])

    return str(answer)


def main():
    """
    主程式進入點。
    """

    data = sys.stdin.read()
    print(solve(data))


if __name__ == "__main__":
    main()