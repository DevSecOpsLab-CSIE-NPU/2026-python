import sys

"""
11150 hand-written 版本

此檔提供可讀性較高的實作，包含壓縮位置與 DP 的說明，方便學習演算法要點。
"""


def solve_case(length: int, min_hop: int, max_hop: int, stones: list[int]) -> int:
    # 如果每次只能跳固定距離，就直接看有哪些石子會落在跳點上。
    if min_hop == max_hop:
        step = min_hop
        return sum(1 for stone in stones if stone % step == 0)

    # 先把很長的空隙壓縮，因為超過 k 的部分對答案沒有影響。
    # 這樣可以把原本很長的河道縮短，讓 DP 的狀態數量變少。
    limit = max_hop * (max_hop - 1)
    compressed_stones: list[int] = []
    last = 0
    shift = 0

    for point in stones + [length]:
        current = point - shift
        gap = current - last
        if gap > limit:
            shift += gap - limit
            current = last + limit
        if point != length:
            compressed_stones.append(current)
        last = current

    compressed_length = length - shift
    is_stone = [0] * (compressed_length + 1)
    for stone in compressed_stones:
        is_stone[stone] = 1

    inf = 10 ** 9
    dp = [inf] * (compressed_length + 1)
    dp[0] = 0

    # dp[i] 表示跳到 i 這個位置時，最少踩到幾顆石子。
    # 因為每一步都只會往前跳，所以可以照位置由小到大更新。
    for position in range(1, compressed_length + 1):
        best = inf
        for hop in range(min_hop, max_hop + 1):
            prev = position - hop
            if prev < 0:
                break
            best = min(best, dp[prev])
        if best < inf:
            dp[position] = best + is_stone[position]

    start = max(0, compressed_length - max_hop)
    return min(dp[start:compressed_length + 1])


def main() -> None:
    # 這題可能有多組測資，所以要一路讀到輸入結束。
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    index = 0
    outputs = []
    while index < len(data):
        # 每一組測資的格式是：L、S、T、石子數量、石子位置列表。
        length = data[index]
        index += 1
        min_hop, max_hop, stone_count = data[index:index + 3]
        index += 3
        stones = data[index:index + stone_count]
        index += stone_count
        outputs.append(str(solve_case(length, min_hop, max_hop, stones)))

    sys.stdout.write("\n".join(outputs))


if __name__ == "__main__":
    main()