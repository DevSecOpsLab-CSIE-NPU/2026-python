"""
題目：UVA 11150 - 青蛙跳過獨木橋 (簡化版)
使用BFS找最少踩石子數

核心概念:
1. 青蛙從位置0開始,目標是到達或超過位置L
2. 每次跳躍可以跳S到T距離(包含)
3. 踩到石子時計數器+1
4. 找到最少踩石子數
"""

from collections import deque

# 讀取輸入
while True:
    try:
        # 讀入橋長L、最小跳躍S、最大跳躍T、石子數M
        L, S, T, M = map(int, input().split())
        
        # 讀入石子位置並轉為集合(加快查詢)
        stones = set()
        if M > 0:
            stones = set(map(int, input().split()))
        
        # BFS: 紀錄(當前位置, 踩過的石子數)
        queue = deque([(0, 0)])  # 從位置0開始,踩過0顆石子
        visited = {0}  # 記錄已訪問過的位置
        
        # 搜尋
        while queue:
            pos, count = queue.popleft()
            
            # 嘗試所有可能的跳躍方式(距離S~T)
            for distance in range(S, T + 1):
                new_pos = pos + distance
                
                # 到達或超過終點L時,搜尋結束
                if new_pos >= L:
                    count_result = count  # 如果新位置是石子就+1,否則不變
                    if new_pos in stones:
                        count_result += 1
                    print(count_result)
                    raise StopIteration  # 跳出所有迴圈
                
                # 如果還沒到終點,且此位置未訪問過
                if new_pos not in visited:
                    visited.add(new_pos)
                    # 新位置是否踩到石子
                    if new_pos in stones:
                        queue.append((new_pos, count + 1))  # 踩到石子,計數+1
                    else:
                        queue.append((new_pos, count))  # 沒踩到,計數不變
    
    except StopIteration:
        pass  # 正常結束
    except EOFError:
        break  # 沒有更多輸入
