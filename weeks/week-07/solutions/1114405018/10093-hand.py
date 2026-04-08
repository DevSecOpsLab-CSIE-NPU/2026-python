from functools import lru_cache
import sys


def generate_row_states(m):
   
    states = []
    for s in range(1 << m):
       
        if s & (s << 1):
            continue
  
        if s & (s << 2):
            continue
        states.append(s)
    return states

def max_artillery(grid):
    n = len(grid)
    if n == 0:
        return 0

    m = len(grid[0])

    # states: 單列合法狀態清單
    states = generate_row_states(m)


    cnt = [s.bit_count() for s in states]

    
    blocked = []
    for row in grid:
        mask = 0
        for j, ch in enumerate(row):
            if ch == "H":
                mask |= 1 << j
        blocked.append(mask)

    row_candidates = []
    for i in range(n):
        cands = []
        for idx, s in enumerate(states):
            if (s & blocked[i]) == 0:
                cands.append(idx)
        row_candidates.append(cands)

    zero_idx = states.index(0)

    @lru_cache(maxsize=None)
    def dfs(i, prev1, prev2):

        if i == n:
            return 0

        best = 0
        s_prev1 = states[prev1]
        s_prev2 = states[prev2]

        for cur in row_candidates[i]:
            s_cur = states[cur]


            if (s_cur & s_prev1) != 0:
                continue
            if (s_cur & s_prev2) != 0:
                continue

            best = max(best, cnt[cur] + dfs(i + 1, cur, prev1))
        return best
    
    return dfs(0, zero_idx, zero_idx)

def solve(text):

    parts = text.split()
    if not parts:
        return "0"
    
    n = int(parts[0])
    m = int(parts[1])
    rows = parts[2:2+ n]
    grid = [list(row) for row in rows]
    return str(max_artillery(grid))

def main():
    print(solve(sys.stdin.read()))

if __name__ == "__main__":
    main()
    