import sys

class DSU:
    """
    互斥集 (Disjoint Set Union) 資料結構
    用來動態維護哪些陷阱是互相連通的，並且記錄每個連通群組是否碰觸到地圖的「最上緣」與「最下緣」。
    """
    def __init__(self):
        self.parent = {}
        self.top = {}     # 紀錄該群組是否連接到最上緣 (x = N - 1)
        self.bottom = {}  # 紀錄該群組是否連接到最下緣 (x = 0)

    def add(self, p, is_top, is_bottom):
        # 新增一個陷阱節點到 DSU 中
        if p not in self.parent:
            self.parent[p] = p
            self.top[p] = is_top
            self.bottom[p] = is_bottom

    def find(self, p):
        root = p
        # 尋找這個節點所屬群組的「根節點」
        while self.parent[root] != root:
            root = self.parent[root]
            
        # 路徑壓縮 (Path Compression)：將沿途找過的節點全部直接連到根節點，大幅加速未來的查詢
        curr = p
        while curr != root:
            nxt = self.parent[curr]
            self.parent[curr] = root
            curr = nxt
        return root

    def union(self, p, q):
        # 將 p 和 q 所在的兩個群組進行合併
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP != rootQ:
            self.parent[rootP] = rootQ
            # 合併時，只要其中一個群組有碰到邊界，合併後的大群組也會被標記為碰到該邊界
            self.top[rootQ] = self.top[rootQ] or self.top[rootP]
            self.bottom[rootQ] = self.bottom[rootQ] or self.bottom[rootP]

def main():
    # 一次性讀取所有的標準輸入，並切割成列表，方便快速讀取資料
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    tokens = iter(input_data)
    
    # ZeroJudge 常會包含多組測試資料，以迴圈讀取直到 EOF
    for n_str in tokens:
        N = int(n_str)
        M = int(next(tokens))
        T = int(next(tokens))
        
        dsu = DSU()
        grid = set() # 記錄目前成功放置的陷阱座標
        
        for _ in range(T):
            x, y = int(next(tokens)), int(next(tokens))
            
            # 判斷這顆新加入的陷阱是否本身就位於上邊界或下邊界
            is_top = (x == N - 1)
            is_bottom = (x == 0)
            
            new_top, new_bottom = is_top, is_bottom
            neighbors = []
            
            # 檢查新陷阱周圍 8 個方位 (包含斜角)，看看是否有已經放置的其他陷阱
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0: continue
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in grid:
                        root = dsu.find((nx, ny))
                        neighbors.append(root)
                        # 預測：如果把新陷阱和這些鄰居接在一起，是否會同時觸碰到上下邊界？
                        new_top = new_top or dsu.top[root]
                        new_bottom = new_bottom or dsu.bottom[root]
                        
            if new_top and new_bottom:
                print(">_<") # 會將上緣與下緣相連，形成一道阻斷左右去路的牆，因此拒絕放置
            else:
                print("<(_ _)>") # 不會封死道路，允許放置
                grid.add((x, y))
                dsu.add((x, y), is_top, is_bottom)
                for root in neighbors:
                    dsu.union((x, y), root) # 確實將新陷阱與周圍的陷阱群組合併

if __name__ == '__main__':
    main()