from collections import deque

def solve():
    while True:
        vals = list(map(int, input().split()))
        L, S, T, M = vals[0], vals[1], vals[2], vals[3]
        
        if L == 0 and S == 0 and T == 0 and M == 0:
            break
        
        stones = set()
        if M > 0:
            stones = set(map(int, input().split()))
        
        # BFS
        queue = deque([(0, 0)])  # (position, stones_stepped)
        visited = {0: 0}
        ans = float('inf')
        
        while queue:
            pos, cnt = queue.popleft()
            
            # Can jump over bridge
            if pos + S >= L:
                ans = min(ans, cnt)
                continue
            
            # Try all jump distances
            for jump in range(S, T + 1):
                nxt = pos + jump
                
                if nxt >= L:
                    ans = min(ans, cnt)
                else:
                    ncnt = cnt + (1 if nxt in stones else 0)
                    if nxt not in visited or visited[nxt] > ncnt:
                        visited[nxt] = ncnt
                        queue.append((nxt, ncnt))
        
        print(ans)

if __name__ == "__main__":
    solve()
