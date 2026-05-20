import sys

# 這個程式解決 UVA 11321 (陷阱路徑) 題目
# 核心邏輯：使用並查集 (DSU) 判斷 8 方位連通的陷阱是否「從頂部連到底部」
# 如果陷阱連線能從 x=N-1 連到 x=0，則會擋住從左 (y=0) 到右 (y=M-1) 的 4 方位路徑。

class DSU:
    def __init__(self, n):
        # 初始化 parent 陣列，每個節點的根是自己
        self.parent = list(range(n))
    
    def find(self, i):
        # 尋找根節點（路徑壓縮優化）
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        # 合併兩個集合
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            return True
        return False

def solve():
    # 讀取輸入 N, M, T
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    T = int(input_data[2])
    
    # 建立並查集
    # 節點 0 到 T-1 代表第幾個陷阱
    # 虛擬節點 T 代表「頂部邊界 (x = N-1)」
    # 虛擬節點 T+1 代表「底部邊界 (x = 0)」
    dsu = DSU(T + 2)
    TOP = T
    BOTTOM = T + 1
    
    traps = {} # 紀錄座標 (x, y) 到陷阱編號的映射
    idx = 3
    
    for t_id in range(T):
        x = int(input_data[idx])
        y = int(input_data[idx+1])
        idx += 2
        
        # 備份 parent 狀態，如果放了會封死，我們要還原 (雖然這題只需不放即可)
        # 但 DSU 還原較複雜，我們可以先「預判」
        
        # 檢查新陷阱會跟哪些現有陷阱或邊界相連
        connected_to = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0: continue
                nx, ny = x + dx, y + dy
                if (nx, ny) in traps:
                    connected_to.append(traps[(nx, ny)])
        
        # 暫存當前的 parent 以便「模擬」放陷阱
        old_parent = list(dsu.parent)
        
        # 嘗試合併
        for neighbor_id in connected_to:
            dsu.union(t_id, neighbor_id)
        
        # 如果在邊界，與虛擬節點合併
        if x == N - 1:
            dsu.union(t_id, TOP)
        if x == 0:
            dsu.union(t_id, BOTTOM)
            
        # 檢查是否封死 (TOP 和 BOTTOM 連通)
        if dsu.find(TOP) == dsu.find(BOTTOM):
            print(">_<")
            # 復原 DSU 狀態，因為這個陷阱「不放上去」
            dsu.parent = old_parent
        else:
            print("<(_ _)>")
            traps[(x, y)] = t_id

if __name__ == "__main__":
    solve()
