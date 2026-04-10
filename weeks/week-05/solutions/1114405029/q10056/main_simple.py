def solve():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    t = int(next(it))
    results = []
    for _ in range(t):
        n = int(next(it))
        p = float(next(it))
        i = int(next(it))
        q = 1 - p
        if abs(q - 1) < 1e-12:
            win = 1.0 / n
        else:
            win = p * (q ** (i - 1)) / (1 - q ** n)
        results.append("{:.4f}".format(win))
    sys.stdout.write("\n".join(results))

if __name__ == "__main__":
    solve()