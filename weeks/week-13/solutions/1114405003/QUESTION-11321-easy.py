"""
題目：UVA 11321 - 陷阱放置判定 (簡化版)
判斷新增陷阱後是否仍有通路從起點(左邊)到終點(右邊)

核心邏輯:
1. 網格大小: N行 × M列
2. 起點: 第0列(左邊)的任何非陷阱位置
3. 終點: 第M-1列(右邊)的任何位置
4. 對每個陷阱放置請求:
   - 使用BFS檢查是否還有通路
   - 如果有通路, 允許放置並輸出"<(_ _)>"
   - 如果沒有通路, 拒絕放置並輸出">_<"
"""

from collections import deque

def can_reach_right(N, M, traps):
    """
    使用BFS檢查是否有通路從左邊(y=0)到右邊(y=M-1)
    """
    # 將陷阱轉為集合,便於快速查詢
    trap_set = set(traps)
    
    # 從左邊(第一列)開始搜尋
    queue = deque()
    visited = set()
    
    # 將左邊所有非陷阱位置加入隊列
    for x in range(N):
        if (x, 0) not in trap_set:
            queue.append((x, 0))
            visited.add((x, 0))
    
    # BFS搜尋
    while queue:
        x, y = queue.popleft()
        
        # 到達右邊返回True
        if y == M - 1:
            return True
        
        # 嘗試四個方向:上、下、左、右
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            
            # 檢查: 1.在邊界內 2.未訪問 3.不是陷阱
            if 0 <= nx < N and 0 <= ny < M and (nx, ny) not in visited and (nx, ny) not in trap_set:
                visited.add((nx, ny))
                queue.append((nx, ny))
    
    return False  # 搜尋完畢沒找到通路

# 主程式
N, M, T = map(int, input().split())

traps = []  # 已放置的陷阱清單

# 處理T個陷阱放置請求
for _ in range(T):
    x, y = map(int, input().split())
    
    # 判斷新增此陷阱後是否還有通路
    if can_reach_right(N, M, traps + [(x, y)]):
        # 有通路,可以放置
        print("<(_ _)>")
        traps.append((x, y))  # 正式加入陷阱清單
    else:
        # 無通路,不能放置(會封死道路)
        print(">_<")
