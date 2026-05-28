import sys 
from collections import deque

def solve_case(L, S, T, stones):
    stone_set = set(stones)
    max_stone = max(stones) if stones else 0
    max_pos = min(L, max_stone + T)

    INF = 10**9
    dist = [INF] * (max_pos + 1)
    dist[0] = 0
    dq = deque([0])
    ans = INF

    while dq:
        pos = dq.popleft()
        if pos >= L:
            ans = min(ans, dist[pos])
            continue
        for jump in range(S, T+1):
            nxt = pos + jump
            if nxt >= L:
                ans = min(ans, dist[pos])
                continue
            if nxt > max_pos:
                continue
            cost = 1 if nxt in stone_set else 0
            nd = dist[pos] + cost
            if nd < dist[nxt]:
                dist[nxt] = nd
                if cost == 0:
                    dq.appendleft(nxt)
                else:
                    dq.append(nxt)
    return ans if ans != INF else 0

def solve():
    date = list(map(int, sys.stdin.read().split()))
    if not date:
        return
    idx = 0
    out = []
    while idx < len(date):
        L = date[idx]; idx += 1
        S = date[idx]; T = date[idx+1]; M = date[idx+2]; idx += 3
        stones = date[idx: idx+M]; idx += M
        out.append(str(solve_case(L, S, T, stones)))
    print("\n".join(out))

if __name__ == '__main__':
    solve()