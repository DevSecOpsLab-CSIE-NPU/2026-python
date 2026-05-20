import unittest

class DSU:
    def __init__(self):
        self.parent = {}
        self.top = {}     # 紀錄該群組是否連接到最上緣
        self.bottom = {}  # 紀錄該群組是否連接到最下緣

    def add(self, p, is_top, is_bottom):
        # 新增一個陷阱節點
        if p not in self.parent:
            self.parent[p] = p
            self.top[p] = is_top
            self.bottom[p] = is_bottom

    def find(self, p):
        root = p
        # 尋找根節點
        while self.parent[root] != root:
            root = self.parent[root]
            
        # 路徑壓縮：將沿途所有節點直接指向根節點，加速未來查詢
        curr = p
        while curr != root:
            nxt = self.parent[curr]
            self.parent[curr] = root
            curr = nxt
        return root

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP != rootQ:
            # 將 P 群組併入 Q 群組
            self.parent[rootP] = rootQ
            # 合併時，若任一群組有連接邊界，合併後的群組也會連接該邊界
            self.top[rootQ] = self.top[rootQ] or self.top[rootP]
            self.bottom[rootQ] = self.bottom[rootQ] or self.bottom[rootP]

def solve_traps(N, M, traps):
    """
    判斷每個陷阱是否可以放置而不導致道路封死。
    """
    dsu = DSU()
    grid = set()
    results = []
    
    for x, y in traps:
        is_top = (x == N - 1)
        is_bottom = (x == 0)
        
        new_top = is_top
        new_bottom = is_bottom
        
        neighbors = []
        # 檢查周圍 8 個方位是否有已經放置的陷阱
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if (nx, ny) in grid:
                    root = dsu.find((nx, ny))
                    neighbors.append(root)
                    # 預先計算若加入此陷阱，是否會觸碰上下邊界
                    new_top = new_top or dsu.top[root]
                    new_bottom = new_bottom or dsu.bottom[root]
                    
        # 若放入該陷阱後，會使得連接上邊界與下邊界的陷阱群集結，代表道路被封死
        if new_top and new_bottom:
            results.append(">_<")
        else:
            # 不會封死，允許放置，並與周遭的陷阱群組合併
            results.append("<(_ _)>")
            grid.add((x, y))
            dsu.add((x, y), is_top, is_bottom)
            for root in neighbors:
                dsu.union((x, y), root)
                
    return results

class TestUVA11321(unittest.TestCase):
    def test_example_blocked(self):
        # 測試案例 1：陷阱連成斜線，導致道路封死
        # 在 3x10 的地圖中，放入 (0,2), (1,3) 後，再放 (2,4) 會將上下界連通
        N, M = 3, 10
        traps = [(0, 2), (1, 3), (2, 4)]
        results = solve_traps(N, M, traps)
        self.assertEqual(results, ["<(_ _)>", "<(_ _)>", ">_<"], "第三個陷阱會連接上下邊界，應該被拒絕")
            
    def test_height_one(self):
        # 測試案例 2：高度為 1 的地圖，任何一個陷阱都會直接封死道路
        self.assertEqual(solve_traps(1, 5, [(0, 2)]), [">_<"], "高度為 1 時放任何陷阱都會封死")

if __name__ == '__main__':
    unittest.main()