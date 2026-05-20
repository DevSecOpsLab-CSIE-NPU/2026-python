import sys
from math import gcd


def lcm(a, b):
    return a // gcd(a, b) * b


def calculate_period(start, end):
    period = 1

    for value in range(start, end + 1):
        period = lcm(period, value)

    return period


def compress_positions(length, stones, s, t):
    period = calculate_period(s, t)
    limit = period + t * 10

    compressed_stones = []
    previous_original = 0
    current_compressed = 0

    for stone in stones:
        gap = stone - previous_original

        if gap > limit:
            gap = limit + gap % period

        current_compressed += gap
        compressed_stones.append(current_compressed)
        previous_original = stone

    final_gap = length - previous_original

    if final_gap > limit:
        final_gap = limit + final_gap % period

    compressed_length = current_compressed + final_gap

    return compressed_length, compressed_stones


def solve(data):
    tokens = data.split()

    if not tokens:
        return ""

    index = 0
    length = int(tokens[index])
    index += 1

    s = int(tokens[index])
    t = int(tokens[index + 1])
    m = int(tokens[index + 2])
    index += 3

    stones = []

    for _ in range(m):
        stones.append(int(tokens[index]))
        index += 1

    stones.sort()

    if s == t:
        count = 0

        for stone in stones:
            if stone % s == 0:
                count += 1

        return str(count)

    compressed_length, compressed_stones = compress_positions(length, stones, s, t)
    stone_set = set(compressed_stones)
    end_position = compressed_length + t

    inf = 10 ** 9
    dp = [inf] * (end_position + 1)
    dp[0] = 0

    for position in range(1, end_position + 1):
        best_previous = inf

        for jump in range(s, t + 1):
            previous_position = position - jump

            if previous_position >= 0:
                best_previous = min(best_previous, dp[previous_position])

        stone_cost = 1 if position in stone_set else 0
        dp[position] = best_previous + stone_cost

    answer = min(dp[compressed_length:end_position + 1])

    return str(answer)


def main():
    data = sys.stdin.read()
    print(solve(data))


if __name__ == "__main__":
    main()
