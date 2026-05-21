import sys

"""
11150 Frog across - 動態規劃壓縮版

解題要點：當 min_hop != max_hop 時，可把河道中超過 k = T*(T-1) 的大空隙壓縮為 k，
此技巧能把原本很長的問題壓縮成可行的 DP 狀態數量。

此檔實作：
- `compress_positions`: 將石子座標與終點依據 limit 壓縮並回傳壓縮後的長度與石子位置。
- `solve_case`: 對壓縮後的長度做一維 DP，dp[i] = 到達位置 i 時最少踩到的石子數。
"""


def compress_positions(length: int, stones: list[int], max_hop: int) -> tuple[int, list[int]]:
    # 如果河道中某段空隙大於 limit，代表在那段中間可以視為連續多個不影響結果的空格，
    # 因此可把它縮短成 limit，並同步把後面的石子座標向前平移 shift 值。
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

    return length - shift, compressed_stones


def solve_case(length: int, min_hop: int, max_hop: int, stones: list[int]) -> int:
    # 每次跳固定長度時，直接數會踩到的石子即可。
    if min_hop == max_hop:
        step = min_hop
        return sum(1 for stone in stones if stone % step == 0)

    compressed_length, compressed_stones = compress_positions(length, stones, max_hop)
    is_stone = [0] * (compressed_length + 1)
    for stone in compressed_stones:
        is_stone[stone] = 1

    inf = 10 ** 9
    dp = [inf] * (compressed_length + 1)
    dp[0] = 0

    for position in range(1, compressed_length + 1):
        best = inf
        for hop in range(min_hop, max_hop + 1):
            prev = position - hop
            if prev < 0:
                break
            if dp[prev] < best:
                best = dp[prev]
        if best < inf:
            dp[position] = best + is_stone[position]

    # 終點可以被跳過，所以只要看最後一段距離內的最佳答案即可。
    start = max(0, compressed_length - max_hop)
    return min(dp[start:compressed_length + 1])


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    index = 0
    outputs = []

    while index < len(data):
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