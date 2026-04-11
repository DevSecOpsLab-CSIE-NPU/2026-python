import sys


def solve():
    # 手打版保留最核心的做法：排序後取中位數。
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    t = data[0]
    idx = 1
    out = []

    for _ in range(t):
        n = data[idx]
        idx += 1

        arr = data[idx:idx + n]
        idx += n

        arr.sort()
        mid = arr[n // 2]

        total = 0
        for x in arr:
            total += abs(x - mid)

        out.append(str(total))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()