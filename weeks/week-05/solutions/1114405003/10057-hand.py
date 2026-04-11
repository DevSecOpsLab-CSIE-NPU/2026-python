import sys


def solve():
    # 先排序，再找中位數區間。
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    idx = 0
    out = []

    while idx < len(data):
        n = data[idx]
        idx += 1

        arr = data[idx:idx + n]
        idx += n

        arr.sort()

        left = arr[(n - 1) // 2]
        right = arr[n // 2]

        same = 0
        for x in arr:
            if x == left:
                same += 1

        ways = right - left + 1
        out.append(f"{left} {same} {ways}")

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()