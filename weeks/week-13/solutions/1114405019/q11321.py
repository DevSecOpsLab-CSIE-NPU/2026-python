import sys

class DSU:
    def __init__(self, n):
        self.p = list(range(n))
    def find(self, i):
        if self.p[i] == i: return i
        self.p[i] = self.find(self.p[i])
        return self.p[i]
    def union(self, i, j):
        root_i, root_j = self.find(i), self.find(j)
        if root_i != root_j:
            self.p[root_i] = root_j

def solve():
    data = sys.stdin.read().split()
    if not data: return
    N, M, T = map(int, data[:3])
    dsu = DSU(T + 2)
    TOP, BOTTOM = T, T + 1
    traps = {}
    idx = 3
    for t_id in range(T):
        x, y = int(data[idx]), int(data[idx+1])
        idx += 2
        neighbors = []
        for dx in [-1,0,1]:
            for dy in [-1,0,1]:
                if dx == 0 and dy == 0: continue
                if (x+dx, y+dy) in traps: neighbors.append(traps[(x+dx, y+dy)])
        
        old_p = list(dsu.p)
        for n_id in neighbors: dsu.union(t_id, n_id)
        if x == N-1: dsu.union(t_id, TOP)
        if x == 0: dsu.union(t_id, BOTTOM)
            
        if dsu.find(TOP) == dsu.find(BOTTOM):
            print(">_<")
            dsu.p = old_p
        else:
            print("<(_ _)>")
            traps[(x, y)] = t_id

if __name__ == "__main__":
    solve()
