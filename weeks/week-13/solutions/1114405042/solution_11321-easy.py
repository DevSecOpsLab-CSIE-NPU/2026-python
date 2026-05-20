# 題目 11321: 網格陷阱判定 (簡易版 - 使用廣度優先搜尋 BFS)
# 這個版本每次放陷阱前，都會從起點開始跑一次 BFS 來檢查是否能走到終點
# 雖然速度較慢，但是邏輯最直覺、最容易理解和記憶。

def solve():
    import sys
    from collections import deque
    
    data = sys.stdin.read().split()
    if not data: return
    
    N = int(data[0])
    M = int(data[1])
    T = int(data[2])
    idx = 3
    
    # 用一個集合來儲存目前已經放置的陷阱座標
    traps = set()
    
    # 4 個移動方向 (上下左右)
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    # 檢查是否能從左側 (y=0) 走到右側 (y=M-1)
    def can_reach():
        # 起點是所有 y=0 且沒有陷阱的格子
        queue = deque()
        visited = set()
        
        for i in range(N):
            if (i, 0) not in traps:
                queue.append((i, 0))
                visited.add((i, 0))
                
        # 如果起點全被封死，直接回傳 False
        if not queue: return False
        
        while queue:
            x, y = queue.popleft()
            
            # 如果走到了終點 (最右側)，代表有路徑
            if y == M - 1:
                return True
                
            # 探索 4 個方向
            for dx, dy in moves:
                nx, ny = x + dx, y + dy
                # 確保在網格內，且不是陷阱，且還沒走過
                if 0 <= nx < N and 0 <= ny < M:
                    if (nx, ny) not in traps and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
        
        return False
        
    # 處理每一個陷阱
    for _ in range(T):
        x = int(data[idx])
        y = int(data[idx+1])
        idx += 2
        
        # 嘗試先放上去
        traps.add((x, y))
        
        # 檢查放上去後是否還有路
        if can_reach():
            print("<(_ _)>")
        else:
            # 沒有路的話，就把陷阱拿掉
            traps.remove((x, y))
            print(">_<")

if __name__ == '__main__':
    solve()
