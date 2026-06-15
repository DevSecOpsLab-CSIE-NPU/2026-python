import sys

# 手打版本：優化轉移邏輯，應對魔改網格題目
def solve():
    raw = sys.stdin.read().split()
    if not raw: return
    T = int(raw[0])
    idx = 1
    for t in range(1, T + 1):
        N, M = int(raw[idx]), int(raw[idx+1])
        idx += 2
        grid = []
        lr, lc = -1, -1
        for i in range(N):
            row = [int(c) for c in raw[idx]]
            grid.append(row)
            for j in range(M):
                if row[j] == 1: lr, lc = i, j
            idx += 1

        if lr == -1:
            print(f"Case {t}: 1")
            continue

        MOD = 1000000007
        dp = {0: 1}

        for r in range(N):
            nxt_dp = {}
            for s, v in dp.items():
                if not (s >> (2 * M) & 3): nxt_dp[s << 2] = v
            dp = nxt_dp
            for c in range(M):
                nxt_dp = {}
                for s, v in dp.items():
                    L = (s >> (2 * c)) & 3
                    U = (s >> (2 * (c + 1))) & 3
                    base = s & ~(3 << (2 * c)) & ~(3 << (2 * (c + 1)))
                    if grid[r][c] == 0:
                        if not L and not U: nxt_dp[base] = (nxt_dp.get(base, 0) + v) % MOD
                    else:
                        if not L and not U:
                            nxt_dp[base | 1 | (2 << (2 * c + 2))] = (nxt_dp.get(base | 1 | (2 << (2 * c + 2)), 0) + v) % MOD
                        elif not L or not U:
                            val = L or U
                            nxt_dp[base | (val << (2 * c))] = (nxt_dp.get(base | (val << (2 * c)), 0) + v) % MOD
                            nxt_dp[base | (val << (2 * c + 2))] = (nxt_dp.get(base | (val << (2 * c + 2)), 0) + v) % MOD
                        elif L == 1 and U == 1:
                            cnt, st = 1, base
                            for i in range(c + 2, M + 1):
                                target = (st >> (2 * i)) & 3
                                if target == 1: cnt += 1
                                elif target == 2: cnt -= 1
                                if not cnt:
                                    nxt_dp[st & ~(3 << (2 * i)) | (1 << (2 * i))] = (nxt_dp.get(st & ~(3 << (2 * i)) | (1 << (2 * i)), 0) + v) % MOD
                                    break
                        elif L == 2 and U == 2:
                            cnt, st = 1, base
                            for i in range(c - 1, -1, -1):
                                target = (st >> (2 * i)) & 3
                                if target == 2: cnt += 1
                                elif target == 1: cnt -= 1
                                if not cnt:
                                    nxt_dp[st & ~(3 << (2 * i)) | (2 << (2 * i))] = (nxt_dp.get(st & ~(3 << (2 * i)) | (2 << (2 * i)), 0) + v) % MOD
                                    break
                        elif L == 2 and U == 1:
                            nxt_dp[base] = (nxt_dp.get(base, 0) + v) % MOD
                        elif L == 1 and U == 2:
                            if r == lr and c == lc and not base: nxt_dp[0] = (nxt_dp.get(0, 0) + v) % MOD
                dp = nxt_dp
        print(f"Case {t}: {dp.get(0, 0)}")

if __name__ == "__main__": solve()
