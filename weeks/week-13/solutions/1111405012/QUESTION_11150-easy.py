"""
題目 11150: 青蛙過獨木橋 (簡易版 - Easy)

使用 BFS (廣度優先搜尋) 找出最少踩到的石子數

演算法思路：
1. 每次可以跳 S 到 T 的距離
2. 如果著陸點有石子，踩踏計數加 1
3. 使用 BFS 探索最短成本路徑
"""

from collections import deque


def min_stones_stepped(L, S, T, stones):
    """
    計算青蛙過橋最少踩到的石子數

    使用 BFS 找最少踩踏數：
    - 起點：位置 0，踩踏數 0
    - 終點：位置 >= L
    - 轉移：每次跳 S 到 T 距離
    """
    # 將石子位置轉換為集合以加快查詢
    stones_set = set(stones)

    # BFS 隊列：(當前位置, 踩踏數)
    queue = deque([(0, 0)])

    # 記錄已訪問的位置及最少踩踏數
    visited = {0: 0}

    while queue:
        # 取出隊列前端
        pos, steps = queue.popleft()

        # 如果已到達或超過終點，返回踩踏數
        if pos >= L:
            return steps

        # 嘗試所有可能的跳躍距離 (S 到 T)
        for distance in range(S, T + 1):
            # 計算下一個著陸位置
            next_pos = pos + distance

            # 檢查是否踩到石子
            if next_pos in stones_set:
                stones_count = 1  # 踩到石子
            else:
                stones_count = 0  # 沒踩到

            # 新的踩踏數
            new_steps = steps + stones_count

            # 如果已經到達或超過終點
            if next_pos >= L:
                return new_steps

            # 只在未訪問或找到更少踩踏的路徑時才加入隊列
            if next_pos not in visited or visited[next_pos] > new_steps:
                # 更新訪問記錄
                visited[next_pos] = new_steps
                # 加入隊列繼續探索
                queue.append((next_pos, new_steps))

    return -1


def solve(L=None, S=None, T=None, stones=None):
    """
    主求解函數
    接收橋長、跳躍範圍和石子位置，返回最少踩踏數
    """
    if L is None or S is None or T is None or stones is None:
        return -1

    return min_stones_stepped(L, S, T, stones)
