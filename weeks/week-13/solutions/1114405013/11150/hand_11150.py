import sys


def calc_min_stones(L, S, T, stone_list):
    if S == T:
        stone_set = set(stone_list)
        pos = S
        hit = 0
        while pos <= L:
            if pos in stone_set:
                hit += 1
            pos += S
        return hit

    keep = S * T
    stones = sorted(stone_list)

    new_stones = []
    prev_real = 0
    prev_new = 0

    for x in stones:
        gap = x - prev_real
        prev_new += min(gap, keep)
        new_stones.append(prev_new)
        prev_real = x

    new_L = prev_new + min(L - prev_real, keep)

    mark = [0] * (new_L + 1)
    for x in new_stones:
        if x <= new_L:
            mark[x] = 1

    top = new_L + T
    INF = 10**9
    dp = [INF] * (top + 1)
    dp[0] = 0

    for i in range(top + 1):
        if dp[i] == INF:
            continue

        for jump in range(S, T + 1):
            j = i + jump
            if j > top:
                continue

            add = mark[j] if j <= new_L else 0
            if dp[i] + add < dp[j]:
                dp[j] = dp[i] + add

    return min(dp[new_L : top + 1])


def solve(text):
    arr = text.split()
    p = 0
    out = []

    while p < len(arr):
        L = int(arr[p])
        p += 1

        S = int(arr[p])
        T = int(arr[p + 1])
        M = int(arr[p + 2])
        p += 3

        stones = list(map(int, arr[p : p + M]))
        p += M

        out.append(str(calc_min_stones(L, S, T, stones)))

    return "\n".join(out)


def main():
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
