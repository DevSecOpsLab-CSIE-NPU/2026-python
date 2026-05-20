# AI 教你的簡單版本 - UVA 11321 Magic Road
# 題目概念：在N*M網格上放置陷阱，檢查是否會封死從左到右的通路

from collections import deque

def can_reach(N, M, traps):
    """
    檢查是否能從左邊的任意位置走到右邊的任意位置
    使用BFS找通路
    grid[x][y] = 1 表示有陷阱
    """
    # 創建網格
    grid = {}
    for x, y in traps:
        grid[(x, y)] = True
    
    # BFS 從左邊任意位置開始
    queue = deque()
    visited = set()
    
    # 起點：左邊第一列的所有位置（x 軸為 0 的所有點）
    for x in range(N):
        if (x, 0) not in grid:  # 不是陷阱
            queue.append((x, 0))
            visited.add((x, 0))
    
    # BFS
    while queue:
        x, y = queue.popleft()
        
        # 如果到達右邊邊界，表示有通路
        if y == M - 1:
            return True
        
        # 嘗試四個方向：上、下、左、右
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            
            # 檢查邊界
            if 0 <= nx < N and 0 <= ny < M:
                # 檢查是否已訪問或是陷阱
                if (nx, ny) not in visited and (nx, ny) not in grid:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
    
    # 沒有找到通路
    return False


def solve():
    while True:
        line = input().split()
        N, M, T = int(line[0]), int(line[1]), int(line[2])
        
        if N == 0 and M == 0 and T == 0:
            break
        
        traps = set()  # 存儲所有已放置的陷阱
        
        # 放置 T 個陷阱
        for _ in range(T):
            x, y = map(int, input().split())
            
            # 檢查放置陷阱是否會導致道路封死
            # 臨時放置陷阱
            test_traps = traps.copy()
            test_traps.add((x, y))
            
            # 檢查是否還有通路
            if can_reach(N, M, test_traps):
                # 有通路，可以放置陷阱
                print("<(_ _)>")
                traps.add((x, y))
            else:
                # 沒有通路，不能放置陷阱
                print(">_<")


# 執行
if __name__ == "__main__":
    solve()
