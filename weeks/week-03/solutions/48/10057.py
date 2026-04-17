import sys
from bisect import bisect_left, bisect_right


def solve() -> None:
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return

    idx = 0
    out = []
    total = len(tokens)

    while idx < total:
        n = int(tokens[idx])
        idx += 1
        if idx + n > total:
            break

        arr = list(map(int, tokens[idx:idx + n]))
        idx += n
        arr.sort()

        low = arr[(n - 1) // 2]
        high = arr[n // 2]
        count = bisect_right(arr, high) - bisect_left(arr, low)
        ways = high - low + 1

        out.append(f"{low} {count} {ways}")

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
