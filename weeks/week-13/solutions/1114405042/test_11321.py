import unittest

class DSU:
    def __init__(self, size):
        self.parent = list(range(size))
        self.has_top = [False] * size
        self.has_bottom = [False] * size

    def find(self, i):
        if self.parent[i] == i: return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            self.has_top[root_j] |= self.has_top[root_i]
            self.has_bottom[root_j] |= self.has_bottom[root_i]

def solve_grid(N, M, traps):
    dsu = DSU(len(traps))
    grid = {}
    output = []
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    trap_id = 0
    for x, y in traps:
        connects_top = (x == N - 1)
        connects_bottom = (x == 0)
        
        adjacent_roots = set()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (nx, ny) in grid:
                neighbor_id = grid[(nx, ny)]
                root = dsu.find(neighbor_id)
                adjacent_roots.add(root)
                
        for root in adjacent_roots:
            if dsu.has_top[root]: connects_top = True
            if dsu.has_bottom[root]: connects_bottom = True
                
        if connects_top and connects_bottom:
            output.append(">_<")
        else:
            output.append("<(_ _)>")
            grid[(x, y)] = trap_id
            if x == N - 1: dsu.has_top[trap_id] = True
            if x == 0: dsu.has_bottom[trap_id] = True
            for root in adjacent_roots:
                dsu.union(trap_id, root)
            trap_id += 1
            
    return output

class Test11321(unittest.TestCase):
    def test_grid_1(self):
        """
        測試封死道路的情況
        """
        N = 3
        M = 10
        # 放置陷阱：(0,2), (1,2), (2,2) - 這會把整個路徑切斷
        traps = [(0, 2), (1, 2), (2, 2)]
        result = solve_grid(N, M, traps)
        self.assertEqual(result, ["<(_ _)>", "<(_ _)>", ">_<"])

if __name__ == '__main__':
    unittest.main()
