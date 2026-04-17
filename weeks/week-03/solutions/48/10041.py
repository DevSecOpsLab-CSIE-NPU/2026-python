import sys


def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    t = data[0]
    idx = 1
    out = []

    for _ in range(t):
        r = data[idx]
        idx += 1
        arr = data[idx:idx + r]
        idx += r

        arr.sort()
        median = arr[r // 2]
        total = sum(abs(x - median) for x in arr)
        out.append(str(total))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
