import sys


def min_stones(length, min_jump, max_jump, stones):
    """計算青蛙過河最少會踩到幾顆石子。"""
    stone_set = set(stones)

    # 特判：若每次跳躍距離固定，落點序列就完全固定。
    if min_jump == max_jump:
        jump = min_jump
        pos = jump
        count = 0
        while pos <= length:
            if pos in stone_set:
                count += 1
            pos += jump
        return count

    # 一般情況使用「座標壓縮 + DP」。
    # 因為 S,T <= 10，當相鄰距離很大時，超過某個門檻後的效果可視為重複。
    # 這裡用 S*T 當壓縮上限，能大幅縮小狀態數量。
    max_gap = min_jump * max_jump
    sorted_stones = sorted(stones)

    compressed_stones = []
    prev = 0
    compressed_pos = 0

    for pos in sorted_stones:
        gap = pos - prev
        compressed_pos += min(gap, max_gap)
        compressed_stones.append(compressed_pos)
        prev = pos

    # 把終點也壓縮到同一座標系。
    compressed_length = compressed_pos + min(length - prev, max_gap)

    # 建立石子標記陣列：is_stone[i] = 1 表示壓縮後座標 i 有石子。
    is_stone = [0] * (compressed_length + 1)
    for pos in compressed_stones:
        if pos <= compressed_length:
            is_stone[pos] = 1

    # dp[i] = 到達壓縮座標 i 時，最少踩石數。
    # 目標是到達或跳過 compressed_length。
    limit = compressed_length + max_jump
    inf = 10**9
    dp = [inf] * (limit + 1)
    dp[0] = 0

    for cur in range(limit + 1):
        if dp[cur] == inf:
            continue

        for step in range(min_jump, max_jump + 1):
            nxt = cur + step
            if nxt > limit:
                continue

            extra = is_stone[nxt] if nxt <= compressed_length else 0
            if dp[cur] + extra < dp[nxt]:
                dp[nxt] = dp[cur] + extra

    return min(dp[compressed_length : limit + 1])


def solve(text):
    """支援 EOF 多組測資，逐組輸出最少踩石數。"""
    tokens = text.split()
    idx = 0
    answers = []

    while idx < len(tokens):
        length = int(tokens[idx])
        idx += 1

        min_jump = int(tokens[idx])
        max_jump = int(tokens[idx + 1])
        count_stones = int(tokens[idx + 2])
        idx += 3

        stones = list(map(int, tokens[idx : idx + count_stones]))
        idx += count_stones

        answers.append(str(min_stones(length, min_jump, max_jump, stones)))

    return "\n".join(answers)


def main():
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
