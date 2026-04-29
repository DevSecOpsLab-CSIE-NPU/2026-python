import sys
from functools import lru_cache

MOD = 1000000007
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def solve():
    data = sys.stdin.read().strip().splitlines()
    if not data:
        return
    
    T = int(data[0].strip())
    idx = 1
    
    for case in range(1, T + 1):
        N, M = map(int, data[idx].split())
        idx += 1
        
        grid = [list(map(int, data[idx + i].split())) for i in range(N)]
        idx += N
        
        ans = count(N, M, grid)
        print(f"Case {case}: {ans}")

def count(N, M, grid):
    cells = [(r, c) for r in range(N) for c in range(M) if grid[r][c] == 1]
    n = len(cells)
    if n == 0:
        return 1
    
    pos_to_idx = {cells[i]: i for i in range(n)}
    
    @lru_cache(maxsize=None)
    def dfs(mask):
        if mask == (1 << n) - 1:
            return 1
        
        ways = 0
        first = (mask.bit_length() - 1).bit_length()
        for i in range(n):
            if not (mask >> i) & 1:
                first = i
                break
        
        r, c = cells[first]
        for cyc in make_cycle(first, mask, N, M, grid, cells, pos_to_idx):
            new_mask = mask
            for j in cyc:
                new_mask |= (1 << j)
            ways = (ways + dfs(new_mask)) % MOD
        
        return ways
    
    def make_cycle(start, used, N, M, grid, cells, pos_to_idx):
        cycles = []
        
        def go(r, c, path, seen):
            if len(path) >= 3 and (r, c) == cells[start]:
                if len(set(path)) == len(path):
                    cycles.append([pos_to_idx[p] for p in path])
                return
            
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] == 1:
                    p = (nr, nc)
                    if p in pos_to_idx and p not in seen:
                        go(nr, nc, path + [p], seen | {p})
        
        go(cells[start][0], cells[start][1], [cells[start]], {cells[start]})
        return cycles
    
    return dfs(0)

if __name__ == "__main__":
    solve()