import sys

# 為了防止遞迴深度的限制導致 DSU 的 find 函式報錯，建議加上這行
sys.setrecursionlimit(20000)

def main():
    # 無腦讀取：將所有輸入轉為迭代器
    data = iter(sys.stdin.read().split())
    
    # 當 iterator 還有資料時就會繼續執行
    for n_str in data:
        N = int(n_str)
        M = int(next(data))
        T = int(next(data))
        
        # 簡化版 DSU：直接用字典來記錄
        parent = {}  # 紀錄每個節點的「老大」是誰
        top = {}     # 紀錄該節點代表的群組是否有碰到最上緣
        bottom = {}  # 紀錄該節點代表的群組是否有碰到最下緣
        grid = set() # 記錄「成功放置」在地圖上的陷阱座標
        
        # 極簡版 find 函式 (附帶路徑壓縮，能大幅加速查詢)
        def find(p):
            if parent[p] != p:
                parent[p] = find(parent[p])
            return parent[p]
            
        for _ in range(T):
            x, y = int(next(data)), int(next(data))
            
            is_top = (x == N - 1)
            is_bot = (x == 0)
            
            # 收集周圍 8 個方位有碰到的「其他陷阱群組的老大」
            neighbors = []
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0: continue
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in grid:
                        neighbors.append(find((nx, ny)))
                        
            # 預測：若放下去，會不會讓「連到上面的群組」與「連到下面的群組」同時被這顆陷阱接在一起？
            will_top = is_top or any(top[r] for r in neighbors)
            will_bot = is_bot or any(bottom[r] for r in neighbors)
            
            if will_top and will_bot:
                print(">_<")  # 道路會被封死，拒絕放置
            else:
                print("<(_ _)>") # 允許放置
                grid.add((x, y))
                parent[(x, y)] = (x, y)
                top[(x, y)], bottom[(x, y)] = is_top, is_bot
                
                # 將周圍所有的群組都「認這顆新陷阱為老大 (合併)」
                for r in neighbors:
                    root = find(r)
                    if root != (x, y):
                        parent[root] = (x, y) # 把周圍群組的老大指向新陷阱
                        top[(x, y)] = top[(x, y)] or top[root]       # 繼承碰到上緣的屬性
                        bottom[(x, y)] = bottom[(x, y)] or bottom[root] # 繼承碰到下緣的屬性

if __name__ == '__main__':
    main()