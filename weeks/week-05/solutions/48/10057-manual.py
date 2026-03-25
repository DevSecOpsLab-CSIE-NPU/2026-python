import bisect
import sys


def solve_case(values):
    values.sort()
    n = len(values)

    if n % 2 == 1:
        a = values[n // 2]
        count = bisect.bisect_right(values, a) - bisect.bisect_left(values, a)
        return a, count, 1

    low = values[n // 2 - 1]
    high = values[n // 2]
    left = bisect.bisect_left(values, low)
    right = bisect.bisect_right(values, high)
    count = right - left
    ways = high - low + 1
    return low, count, ways


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    idx = 0
    out = []

    while idx < len(data):
        n = data[idx]
        idx += 1
        values = data[idx:idx + n]
        idx += n

        a, count, ways = solve_case(values)
        out.append(f"{a} {count} {ways}")

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
