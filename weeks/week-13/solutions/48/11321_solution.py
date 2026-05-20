from collections import deque

def can_reach(N, M, traps):
    """Check if can reach from left to right"""
    grid = {(x, y): True for x, y in traps}
    
    queue = deque()
    visited = set()
    
    # Start from left column
    for x in range(N):
        if (x, 0) not in grid:
            queue.append((x, 0))
            visited.add((x, 0))
    
    # BFS
    while queue:
        x, y = queue.popleft()
        
        if y == M - 1:
            return True
        
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < N and 0 <= ny < M:
                if (nx, ny) not in visited and (nx, ny) not in grid:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
    
    return False

def solve():
    while True:
        vals = list(map(int, input().split()))
        N, M, T = vals[0], vals[1], vals[2]
        
        if N == 0 and M == 0 and T == 0:
            break
        
        traps = set()
        
        for _ in range(T):
            x, y = map(int, input().split())
            
            test_traps = traps | {(x, y)}
            
            if can_reach(N, M, test_traps):
                print("<(_ _)>")
                traps.add((x, y))
            else:
                print(">_<")

if __name__ == "__main__":
    solve()
