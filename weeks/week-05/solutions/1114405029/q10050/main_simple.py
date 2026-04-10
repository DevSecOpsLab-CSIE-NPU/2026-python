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
        p = int(next(it))
        hartals = [int(next(it)) for _ in range(p)]
        lost = 0
        for day in range(1, n + 1):
            if day % 7 == 6 or day % 7 == 0:
                continue
            for h in hartals:
                if day % h == 0:
                    lost += 1
                    break
        results.append(str(lost))
    sys.stdout.write("\n".join(results))

if __name__ == "__main__":
    solve()