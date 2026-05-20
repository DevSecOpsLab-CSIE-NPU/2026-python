import sys

class DSU:
    def __init__(self, size):
        self.parent = list(range(size))
        self.has_top = [False] * size
        self.has_bottom = [False] * size

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            self.has_top[root_j] |= self.has_top[root_i]
            self.has_bottom[root_j] |= self.has_bottom[root_i]

def solve():
    # 設定遞迴深度以防 DSU 遞迴過深
    sys.setrecursionlimit(2000000)
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    idx = 0
    N = int(input_data[idx])
    M = int(input_data[idx+1])
    T = int(input_data[idx+2])
    idx += 3
    
    # DSU 的大小：最多 T 個陷阱
    dsu = DSU(T)
    
    # 紀錄網格上每個位置對應的陷阱 ID (從 0 到 T-1)
    grid = {}
    
    output = []
    
    # 方向陣列：8 連通 (包含對角線)
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    
    trap_id = 0
    for _ in range(T):
        x = int(input_data[idx])
        y = int(input_data[idx+1])
        idx += 2
        
        # 檢查是否會連接上下邊界
        connects_top = (x == N - 1)
        connects_bottom = (x == 0)
        
        # 收集周圍已存在的陷阱的根節點
        adjacent_roots = set()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (nx, ny) in grid:
                neighbor_id = grid[(nx, ny)]
                root = dsu.find(neighbor_id)
                adjacent_roots.add(root)
                
        # 檢查加入這個點後，是否會讓上下相連
        for root in adjacent_roots:
            if dsu.has_top[root]:
                connects_top = True
            if dsu.has_bottom[root]:
                connects_bottom = True
                
        if connects_top and connects_bottom:
            # 會導致封死，拒絕放置
            output.append(">_<")
        else:
            # 允許放置
            output.append("<(_ _)>")
            grid[(x, y)] = trap_id
            
            # 初始化這個陷阱的上下邊界狀態
            if x == N - 1:
                dsu.has_top[trap_id] = True
            if x == 0:
                dsu.has_bottom[trap_id] = True
                
            # 與周圍的陷阱進行聯集
            for root in adjacent_roots:
                dsu.union(trap_id, root)
                
            trap_id += 1
            
    # 一次輸出所有結果
    print('\n'.join(output))

if __name__ == '__main__':
    solve()
