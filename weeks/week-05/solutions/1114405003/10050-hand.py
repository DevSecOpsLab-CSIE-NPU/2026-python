import sys


def solve():
    # 先記錄所有會罷工的工作天，再算總數。
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    idx = 0
    t = data[idx]
    idx += 1
    out = []

    for _ in range(t):
        n = data[idx]
        idx += 1
        p = data[idx]
        idx += 1

        lost = set()
        for _ in range(p):
            h = data[idx]
            idx += 1

            day = h
            while day <= n:
                # 第 6、7 天是週末，不算工作天。
                if day % 7 != 6 and day % 7 != 0:
                    lost.add(day)
                day += h

        out.append(str(len(lost)))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()