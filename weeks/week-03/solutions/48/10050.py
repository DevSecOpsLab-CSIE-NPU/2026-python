import sys


def is_weekend(day: int) -> bool:
    return day % 7 == 6 or day % 7 == 0


def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    t = data[0]
    idx = 1
    out = []

    for _ in range(t):
        n = data[idx]
        idx += 1
        p = data[idx]
        idx += 1

        hs = data[idx:idx + p]
        idx += p

        lost = [False] * (n + 1)
        for h in hs:
            for day in range(h, n + 1, h):
                if not is_weekend(day):
                    lost[day] = True

        out.append(str(sum(lost)))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
