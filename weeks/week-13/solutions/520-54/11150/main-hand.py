import sys
from math import gcd


def solve(data):
    values = data.split()

    if not values:
        return ""

    pos = 0

    L = int(values[pos])
    pos += 1

    S = int(values[pos])
    T = int(values[pos + 1])
    M = int(values[pos + 2])
    pos += 3

    stones = []

    for _ in range(M):
        stones.append(int(values[pos]))
        pos += 1

    stones.sort()

    if S == T:
        answer = 0

        for stone in stones:
            if stone % S == 0:
                answer += 1

        return str(answer)

    period = 1

    for number in range(S, T + 1):
        period = period // gcd(period, number) * number

    safe_limit = period + T * 10

    compressed_stones = []
    original_prev = 0
    compressed_now = 0

    for stone in stones:
        gap = stone - original_prev

        if gap > safe_limit:
            gap = safe_limit + gap % period

        compressed_now += gap
        compressed_stones.append(compressed_now)
        original_prev = stone

    last_gap = L - original_prev

    if last_gap > safe_limit:
        last_gap = safe_limit + last_gap % period

    compressed_L = compressed_now + last_gap

    stone_set = set(compressed_stones)
    max_position = compressed_L + T

    INF = 10 ** 9
    dp = [INF] * (max_position + 1)
    dp[0] = 0

    for i in range(1, max_position + 1):
        best = INF

        for jump in range(S, T + 1):
            previous = i - jump

            if previous >= 0:
                if dp[previous] < best:
                    best = dp[previous]

        if i in stone_set:
            dp[i] = best + 1
        else:
            dp[i] = best

    answer = min(dp[compressed_L:max_position + 1])

    return str(answer)


def main():
    data = sys.stdin.read()
    print(solve(data))


if __name__ == "__main__":
    main()
