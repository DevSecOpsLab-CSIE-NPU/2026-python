import sys


def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return

    it = iter(data)
    L = next(it)
    S = next(it)
    T = next(it)
    M = next(it)
    stones = [next(it) for _ in range(M)] if M > 0 else []

    positions = [0] + sorted(stones) + [L]

    comp = [0]
    cur = 0
    stone_set = set(stones)
    for i in range(1, len(positions)):
        gap = positions[i] - positions[i - 1]
        delta = gap if gap <= T else T
        cur += delta
        comp.append(cur)

    max_pos = comp[-1]
    hasStone = [False] * (max_pos + 1)

    for orig, c in zip(positions, comp):
        if orig in stone_set:
            hasStone[c] = True

    INF = 10**9
    dp = [INF] * (max_pos + 1)
    dp[0] = 0

    for x in range(1, max_pos + 1):
        best = INF
        for step in range(S, T + 1):
            prev = x - step
            if prev < 0:
                break
            if dp[prev] < best:
                best = dp[prev]
        if best < INF:
            dp[x] = best + (1 if hasStone[x] else 0)

    print(dp[max_pos])


if __name__ == '__main__':
    main()
