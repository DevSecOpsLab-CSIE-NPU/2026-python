def solve_10235_easy():
    import sys
    from functools import lru_cache
    lines = sys.stdin.read().split()
    if not lines: return
    T = int(lines[0])
    idx = 1
    out = []
    for case_num in range(1, T + 1):
        N = int(lines[idx])
        M = int(lines[idx+1])
        idx += 2
        grid = []
        for _ in range(N):
            grid.append([int(x) for x in lines[idx:idx+M]])
            idx += M
        MOD = 1000000007
        
        @lru_cache(None)
        def dfs(r, c, state):
            if r == N: return 1 if state == 0 else 0
            if c == M:
                if state & (1 << M): return 0
                return dfs(r + 1, 0, state << 1)
            res = 0
            left = (state >> c) & 1
            up = (state >> (c + 1)) & 1
            if grid[r][c] == 0:
                if left == 0 and up == 0: res = dfs(r, c + 1, state)
            else:
                if left == 0 and up == 0:
                    res = dfs(r, c + 1, state | (1 << c) | (1 << (c + 1)))
                elif left == 1 and up == 1:
                    res = dfs(r, c + 1, state ^ (1 << c) ^ (1 << (c + 1)))
                else:
                    res = (dfs(r, c + 1, state | (1 << c) & ~(1 << (c + 1))) + \
                           dfs(r, c + 1, state | (1 << (c + 1)) & ~(1 << c))) % MOD
            return res % MOD
        ans = dfs(0, 0, 0)
        out.append(f"Case {case_num}: {ans}")
    print("\n".join(out))

if __name__ == '__main__':
    solve_10235_easy()