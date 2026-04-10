def solve():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    t = int(next(it))
    results = []
    for _ in range(t):
        r = int(next(it))
        streets = [int(next(it)) for _ in range(r)]
        streets.sort()
        mid = streets[r // 2]
        total = sum(abs(s - mid) for s in streets)
        results.append(str(total))
    sys.stdout.write("\n".join(results))

if __name__ == "__main__":
    solve()