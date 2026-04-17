import sys


def solve() -> None:
    data = sys.stdin.read().split()
    if not data:
        return

    s = int(data[0])
    idx = 1
    out = []

    for _ in range(s):
        n = int(data[idx])
        p = float(data[idx + 1])
        i = int(data[idx + 2])
        idx += 3

        if p == 0.0:
            ans = 0.0
        else:
            lose_pow = (1.0 - p) ** (i - 1)
            cycle_lose = (1.0 - p) ** n
            ans = (lose_pow * p) / (1.0 - cycle_lose)

        out.append(f"{ans:.4f}")

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
