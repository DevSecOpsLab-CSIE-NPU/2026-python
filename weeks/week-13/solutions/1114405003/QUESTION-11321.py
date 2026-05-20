"""
題目：UVA 11321 - 陷阱放置判定
判斷新增陷阱後是否仍有通路從起點到終點
"""

from collections import deque

def has_path(N, M, traps):
    """
    使用BFS檢測是否有通路從左邊到右邊
    left side (y=0) to right side (y=M-1)
    """
    # 陷阱集合便於查詢
    trap_set = set(traps)
    
    # 起點: 左邊的所有點 (x, 0)，如果不是陷阱
    queue = deque()
    visited = set()
    
    for x in range(N):
        if (x, 0) not in trap_set:
            queue.append((x, 0))
            visited.add((x, 0))
    
    # BFS搜尋
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 上下左右
    
    while queue:
        x, y = queue.popleft()
        
        # 到達右邊則有通路
        if y == M - 1:
            return True
        
        # 探索四個方向
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # 檢查邊界
            if 0 <= nx < N and 0 <= ny < M:
                # 檢查是否已訪問且不是陷阱
                if (nx, ny) not in visited and (nx, ny) not in trap_set:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
    
    return False

# 讀取輸入
N, M, T = map(int, input().split())

# 陷阱清單
traps = []

# 處理每個陷阱放置請求
for _ in range(T):
    x, y = map(int, input().split())
    
    # 檢查放置此陷阱後是否仍有通路
    if has_path(N, M, traps + [(x, y)]):
        # 可以放置
        print("<(_ _)>")
        traps.append((x, y))
    else:
        # 不可以放置
        print(">_<")
