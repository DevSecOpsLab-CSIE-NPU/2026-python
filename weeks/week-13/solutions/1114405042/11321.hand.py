import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    if not data: return
    N, M, T = map(int, data[:3])
    idx = 3
    traps = set()
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    def check_path():
        q = deque([(i, 0) for i in range(N) if (i, 0) not in traps])
        vis = set(q)
        while q:
            x, y = q.popleft()
            if y == M - 1: return True
            for dx, dy in moves:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M and (nx, ny) not in traps and (nx, ny) not in vis:
                    vis.add((nx, ny))
                    q.append((nx, ny))
        return False

    for _ in range(T):
        x, y = int(data[idx]), int(data[idx+1])
        idx += 2
        traps.add((x, y))
        if check_path():
            print("<(_ _)>")
        else:
            traps.remove((x, y))
            print(">_<")

if __name__ == '__main__':
    solve()
