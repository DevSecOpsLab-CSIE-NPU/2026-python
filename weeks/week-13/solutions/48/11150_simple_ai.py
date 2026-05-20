# AI 教你的簡單版本 - UVA 11150 Frog Bridge
# 題目概念：青蛙跳過獨木橋，需要找最少踩到的石子數

from collections import deque

def solve():
    """
    使用BFS找出最少踩到的石子數
    狀態：(當前位置, 踩到石子數)
    """
    
    while True:
        line = input().split()
        L = int(line[0])  # 橋長
        S = int(line[1])  # 最小跳躍距離
        T = int(line[2])  # 最大跳躍距離
        M = int(line[3])  # 石子數量
        
        if L == 0 and S == 0 and T == 0 and M == 0:
            break
        
        # 讀取石子位置
        if M > 0:
            stones = set(map(int, input().split()))
        else:
            stones = set()
        
        # BFS 找最少踩到石子數
        # 隊列中存放 (當前位置, 踩到石子數)
        queue = deque([(0, 0)])  # 從位置0開始，踩0個石子
        visited = {0: 0}  # visited[位置] = 最少踩到的石子數
        
        min_stones = float('inf')
        
        while queue:
            pos, stone_count = queue.popleft()
            
            # 如果已經跳過橋坡，更新最小值
            if pos + S >= L:
                min_stones = min(min_stones, stone_count)
                continue
            
            # 嘗試跳躍 S 到 T 距離
            for jump in range(S, T + 1):
                next_pos = pos + jump
                
                # 如果要跳到或跳過橋坡
                if next_pos >= L:
                    min_stones = min(min_stones, stone_count)
                    continue
                
                # 計算在下一位置踩到石子數
                next_stone_count = stone_count
                if next_pos in stones:
                    next_stone_count += 1
                
                # 如果這個位置還沒訪問過，或者用更少石子到達
                if next_pos not in visited or visited[next_pos] > next_stone_count:
                    visited[next_pos] = next_stone_count
                    queue.append((next_pos, next_stone_count))
        
        print(min_stones)


# 執行
if __name__ == "__main__":
    solve()
