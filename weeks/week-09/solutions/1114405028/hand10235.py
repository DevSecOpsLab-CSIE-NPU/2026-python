

MOD = 10**9 + 7


def solve() -> None:
    import sys

    data = sys.stdin.read().split()
    if not data:
        return

    it = iter(data)
    t = int(next(it))
    out = []

    for _ in range(t):
        n = int(next(it))
        m = int(next(it))
        grid = [[int(next(it)) for _ in range(m)] for _ in range(n)]
        dp = {tuple([0] * m): 1}

        for i in range(n):
            for j in range(m):
                new_dp = {}
                for state, count in dp.items():
                    if grid[i][j] == 0:
                        if state[j] == 0:
                            ns = state[:j] + (0,) + state[j+1:]
                            new_dp[ns] = (new_dp.get(ns, 0) + count) % MOD
                        continue

                    left = state[j-1] if j > 0 else 0
                    up = state[j]
                    if left == 0 and up == 0:
                        new_label = max(state) + 1
                        ns = state[:j] + (new_label,) + state[j+1:]
                        new_dp[ns] = (new_dp.get(ns, 0) + count) % MOD
                    elif left != 0 and up != 0:
                        if left == up:
                            ns = tuple(0 if x == left else x for x in state)
                            new_dp[ns] = (new_dp.get(ns, 0) + count) % MOD
                        else:
                            merged = tuple(left if x == up else x for x in state)
                            ns = merged[:j] + (0,) + merged[j+1:]
                            new_dp[ns] = (new_dp.get(ns, 0) + count) % MOD
                    else:
                        label = left if left != 0 else up
                        ns = state[:j] + (label,) + state[j+1:]
                        new_dp[ns] = (new_dp.get(ns, 0) + count) % MOD

                dp = new_dp
            dp = {state: count for state, count in dp.items() if state[-1] == 0}
            dp = {state[:-1]: count for state, count in dp.items()}

        out.append(str(dp.get(tuple([0] * (m - 1)), 0)))

    sys.stdout.write("\n".join(out) + ("\n" if out else ""))


if __name__ == '__main__':
    solve()
