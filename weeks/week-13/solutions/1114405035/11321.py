# -*- coding: utf-8 -*-
import sys

# 增加遞迴深度以防萬一（雖然此題為迭代尋路）
sys.setrecursionlimit(2000000)

def solve():
    """
    UVA 11321 (ZJ b314) 茵可的陷阱路徑解題主程式
    使用並查集 (DSU) 與 8 連通障礙物判斷
    """
    # 讀取所有輸入
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    T = int(input_data[2])
    
    # DSU 初始化，大小為 N*M + 2。
    # 虛擬節點 TOP = N*M，虛擬節點 BOTTOM = N*M + 1
    num_cells = N * M
    TOP = num_cells
    BOTTOM = num_cells + 1
    
    parent = list(range(num_cells + 2))
    
    # 查找代表元素 (Path Compression)
    def find(i):
        path = []
        curr = i
        while parent[curr] != curr:
            path.append(curr)
            curr = parent[curr]
        for node in path:
            parent[node] = curr
        return curr

    # 記錄每個格子是否已經有陷阱
    is_trap = [False] * num_cells
    
    # 處理每一個陷阱放置請求
    idx = 3
    for _ in range(T):
        if idx >= len(input_data):
            break
        r = int(input_data[idx])
        c = int(input_data[idx+1])
        idx += 2
        
        # 目前欲放置陷阱的格點編號
        cell_idx = r * M + c
        
        # 收集此點放置後將會聯通的所有集合代表
        sets_to_union = {find(cell_idx)}
        
        # 8 個方向的相鄰格點
        for dr, dc in [(-1, -1), (-1, 0), (-1, 1), 
                       (0, -1),          (0, 1), 
                       (1, -1),  (1, 0),  (1, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M:
                neighbor_idx = nr * M + nc
                if is_trap[neighbor_idx]:
                    sets_to_union.add(find(neighbor_idx))
                    
        # 邊界判定：若在頂部 row，則與 TOP 虛擬節點連通
        if r == N - 1:
            sets_to_union.add(find(TOP))
        # 邊界判定：若在底部 row，則與 BOTTOM 虛擬節點連通
        if r == 0:
            sets_to_union.add(find(BOTTOM))
            
        # 檢查是否會導致 TOP 與 BOTTOM 連通（即形成一條從上到下的障礙鏈，切斷了左右通路）
        root_top = find(TOP)
        root_bottom = find(BOTTOM)
        
        if root_top in sets_to_union and root_bottom in sets_to_union:
            # 會堵死，拒絕放置
            print(">_<")
        else:
            # 可以放置
            print("<(_ _)>")
            is_trap[cell_idx] = True
            # 合併所有連通的集合
            new_root = find(cell_idx)
            for root_val in sets_to_union:
                if root_val != new_root:
                    parent[root_val] = new_root

if __name__ == "__main__":
    solve()
