import sys

# 提高 Python 的遞迴深度限制（防止 DSU find 函數因巢狀過深而崩潰）
sys.setrecursionlimit(2000000)

class DSU:
    """ 並查集 (Disjoint Set Union) 類別，用於維護陷阱的連通狀態 """
    def __init__(self, size):
        self.parent = list(range(size))
        
    def find(self, i):
        # 路徑壓縮優化 (Path Compression)
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            return True
        return False

def solve():
    # 讀取所有輸入
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    # 讀取 N, M, T
    N = int(input_data[0])
    M = int(input_data[1])
    T = int(input_data[2])
    
    # 建立二維網格狀態，0 表示空地，1 表示已有陷阱
    # 由於 N, M 最大可達 1000，使用一維 DSU 維護
    # 點 (x, y) 對應的 DSU 編號為 x * M + y
    # 設兩個虛擬節點： UP = N * M, DOWN = N * M + 1
    UP = N * M
    DOWN = N * M + 1
    
    dsu = DSU(N * M + 2)
    grid = [[0] * M for _ in range(N)]
    
    # 上下左右四個方向
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    idx = 3
    output = []
    
    for _ in range(T):
        if idx >= len(input_data):
            break
        x = int(input_data[idx])
        y = int(input_data[idx+1])
        idx += 2
        
        # 特殊情況：若高度為 1，放任何陷阱都會直接把路截斷
        if N == 1:
            output.append(">_<")
            continue
            
        current_id = x * M + y
        
        # 找出放了這個陷阱後，它會與哪些「既有的陷阱集合」連通
        # 我們需要蒐集所有相鄰陷阱的 Root，以及是否會連到 UP 或 DOWN
        neighbor_roots = set()
        connect_to_up = False
        connect_to_down = False
        
        # 檢查自身是否觸及邊界（x = N-1 為上邊界，x = 0 為下邊界）
        if x == N - 1:
            connect_to_up = True
        if x == 0:
            connect_to_down = True
            
        # 檢查四個方向的鄰居
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if grid[nx][ny] == 1: # 鄰居也是陷阱
                    neighbor_roots.add(dsu.find(nx * M + ny))
            else:
                # 越過上下界的情況（與前面直接判斷 x 相同，此處做雙重保險）
                if nx >= N:
                    connect_to_up = True
                if nx < 0:
                    connect_to_down = True
                    
        # 包含虛擬節點的當前集合檢查
        if connect_to_up:
            neighbor_roots.add(dsu.find(UP))
        if connect_to_down:
            neighbor_roots.add(dsu.find(DOWN))
            
        # 關鍵判斷：如果這些即將合併的集合中，同時包含了 UP 的根和 DOWN 的根
        # 代表一旦放下這個陷阱，上下邊界就會被串聯起來，把路封死
        if dsu.find(UP) in neighbor_roots and dsu.find(DOWN) in neighbor_roots:
            output.append(">_<")
        else:
            # 道路沒被封死，允許放置
            output.append("<(_ _)>")
            grid[x][y] = 1 # 正式標記為陷阱
            
            # 在 DSU 中真正執行合併
            if connect_to_up:
                dsu.union(current_id, UP)
            if connect_to_down:
                dsu.union(current_id, DOWN)
                
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 1:
                    dsu.union(current_id, nx * M + ny)
                    
    # 批次輸出結果，優化 I/O 速度
    print('\n'.join(output))

if __name__ == '__main__':
    solve()