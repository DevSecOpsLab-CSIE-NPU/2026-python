"""
題目：UVA 11150 - 青蛙跳過獨木橋
使用BFS找最少踩到的石子數
"""

from collections import deque

def solve_frog(L, S, T, stones):
    """
    使用BFS找到從0跳到L的最少踩石子數
    """
    # 將stones轉換為集合便於查詢
    stone_set = set(stones)
    
    # BFS: (當前位置, 踩到的石子數)
    queue = deque([(0, 0)])
    visited = {0}
    
    while queue:
        pos, stone_count = queue.popleft()
        
        # 嘗試所有可能的跳躍距離 [S, T]
        for jump in range(S, T + 1):
            new_pos = pos + jump
            
            # 如果已經跳過終點，返回結果
            if new_pos >= L:
                return stone_count
            
            # 如果還未訪問過此位置
            if new_pos not in visited:
                visited.add(new_pos)
                # 檢查是否踩到石子
                if new_pos in stone_set:
                    queue.append((new_pos, stone_count + 1))
                else:
                    queue.append((new_pos, stone_count))
    
    return -1  # 如果無法到達

# 主程式迴圈
while True:
    try:
        # 讀取L, S, T, M
        line = input().split()
        if len(line) < 3:
            break
        
        L = int(line[0])
        S = int(line[1])
        T = int(line[2])
        M = int(line[3])
        
        # 讀取石子位置
        stones = []
        if M > 0:
            stone_line = input().split()
            stones = [int(x) for x in stone_line]
        
        # 求解
        result = solve_frog(L, S, T, stones)
        print(result)
    except EOFError:
        break
