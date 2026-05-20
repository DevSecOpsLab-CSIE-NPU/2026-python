import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    # 讀取地圖大小與陷阱數
    N, M, T = map(int, input_data[:3])
    
    # 🌟 特殊極端狀況：如果只有一列，任何陷阱都會直接切斷道路
    if N == 1:
        print('\n'.join([">_<"] * T))
        return

    # 初始化並查集（DSU）：每個格子的老大一開始都是自己
    # 格子 (x, y) 的編號為 x * M + y
    parent = list(range(N * M))
    
    def find(i):
        """ 尋找集團的老大（含路徑壓縮，縮短以後找人的時間） """
        path = []
        while parent[i] != i:
            path.append(i)
            i = parent[i]
        for node in path:  # 手動壓縮路徑，好懂又不會因為遞迴而崩潰
            parent[node] = i
        return i

    def union(i, j):
        """ 讓兩個格子認同一個老大 """
        root_i, root_j = find(i), find(j)
        if root_i != root_j:
            parent[root_i] = root_j

    # 記錄地圖上哪些地方已經有陷阱了
    has_trap = [[False] * M for _ in range(N)]
    output = []
    
    # 四個方向（上下左右）
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # 開始處理每一個陷阱
    idx = 3
    for _ in range(T):
        x, y = int(input_data[idx]), int(input_data[idx+1])
        idx += 2
        
        current_id = x * M + y
        
        # 1. 模擬：找出如果放了這個陷阱，它會跟周圍的哪些「老大」連成一團
        all_roots = {find(current_id)} # 先把自己原本的老大算進去
        
        # 如果自己本身就在邊界，把邊界的特性記下來
        if x == 0:     all_roots.add(find(0 * M + y))      # 碰到下邊界 (轉置後的左牆)
        if x == N - 1: all_roots.add(find((N-1) * M + y))  # 碰到上邊界 (轉置後的右牆)
        
        # 看看鄰居是不是陷阱，是的話把鄰居的老大也拉進來考慮
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and has_trap[nx][ny]:
                all_roots.add(find(nx * M + ny))
        
        # 2. 關鍵防線判斷：
        # 我們檢查所有可能相連的老大裡，有沒有同時包含「最下層的老大們」與「最上層的老大們」
        # 簡單寫法：直接拿所有的下邊界格子、上邊界格子去 find 看看有沒有在 all_roots 裡面
        has_bottom = any(find(i) in all_roots for i in range(M))          # 意即 x = 0
        has_top = any(find((N - 1) * M + i) in all_roots for i in range(M)) # 意即 x = N - 1
        
        if has_bottom and has_top:
            # 會連成一線把路封死！
            output.append(">_<")
        else:
            # 安全，可以放！
            output.append("<(_ _)>")
            has_trap[x][y] = True # 正式放上陷阱
            
            # 真正執行並查集合併
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M and has_trap[nx][ny]:
                    union(current_id, nx * M + ny)
                    
    # 一次印出答案
    print('\n'.join(output))

if __name__ == '__main__':
    solve()