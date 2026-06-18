def solve() -> None:
    import sys

    data = sys.stdin.read().strip().split()
    if not data:
        return

    it = iter(data)
    try:
        t = int(next(it))
    except StopIteration:
        return

    results = []
    for _ in range(t):
        s = int(next(it))
        d = int(next(it))

        if d > s:
            results.append("impossible")
            continue

        if (s + d) % 2 != 0:
            results.append("impossible")
            continue

        high = (s + d) // 2
        low = (s - d) // 2
        if low < 0:
            results.append("impossible")
        else:
            results.append(f"{high} {low}")

    sys.stdout.write("\n".join(results) + ("\n" if results else ""))


if __name__ == "__main__":
    solve()
