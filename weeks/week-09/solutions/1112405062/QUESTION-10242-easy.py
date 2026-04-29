"""
UVA 10242 - Special, Happy Birthday (Easy Version)
=================================================

題目說明：
- Siruseri 城有 N 個路口，M 條單向道路
- 每個路口有一台 ATM，可搶劫一定金額
- 部分路口設有酒吧
- 強盜從市中心 S 出发，沿單向道路行駛
- 每個 ATM 只能搶一次，最後抵達某間酒吧慶祝
- 求最多能搶到的現金總額

解題思路（Easy 版）：
- 使用 Kosaraju 演算法找強連通分量 (SCC)
- 將圖壓縮成 DAG，方便 DP
- 在 DAG 上做最大路徑 DP
- 每個 SCC 的權值 = 區內所有 ATM 金額總和
"""

import sys
sys.setrecursionlimit(10000)  # 加大遞迴深度限制

def solve():
    """
    主函式：讀取輸入、處理資料、輸出結果
    
    輸入格式：
    - N M：路口數、道路數
    - M 行：每條道路的起點、終點
    - N 行：每個路口的 ATM 金額
    - S P：市中心編號、酒吧數量
    - P 行：酒吧所在路口編號
    """
    data = sys.stdin.read().strip().split()
    if not data:
        return
    
    it = iter(data)
    N = int(next(it))   # 路口數
    M = int(next(it))   # 道路數
    
    # --- 建立鄰接表 ---
    # graph[u]: 從路口 u 可以到達的路口列表
    # rev[u]: 反轉圖，可以到達路口 u 的路口列表
    graph = [[] for _ in range(N)]
    rev = [[] for _ in range(N)]
    for _ in range(M):
        u = int(next(it)) - 1  # 減1 因為編號從1開始
        v = int(next(it)) - 1
        graph[u].append(v)       # u → v
        rev[v].append(u)        # 反轉：v ← u
    
    # --- 讀取 ATM 金額 ---
    values = [int(next(it)) for _ in range(N)]
    
    # --- 讀取起點和酒吧 ---
    S = int(next(it)) - 1      # 市中心（起點）
    P = int(next(it))          # 酒吧數量
    bars = [int(next(it)) - 1 for _ in range(P)]  # 酒吧所在路口
    
    # --- 計算並輸出答案 ---
    ans = max_money(N, graph, rev, values, S, bars)
    print(ans)

def max_money(N, graph, rev, values, start, bars):
    """
    計算從起點到酒吧的最大搶劫金額
    
    參數：
    - N: 路口數
    - graph: 正向鄰接表
    - rev: 反轉鄰接表
    - values: 每個路口的 ATM 金額
    - start: 起點路口
    - bars: 酒吧所在路口列表
    
    回傳：最大金額
    """
    
    # ========================================
    # 第一步：Kosaraju 演算法 - 第一遍 DFS
    # ========================================
    # 目的：取得節點的完成順序
    # 從每個未訪問的節點開始 DFS，將訪問完成的節點加入 order
    visited = [False] * N
    order = []                     # 儲存 DFS 完成順序
    
    def dfs1(v):
        """對正向圖做 DFS"""
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:
                dfs1(w)
        order.append(v)            # 訪問完成後加入順序
    
    for v in range(N):
        if not visited[v]:
            dfs1(v)
    
    # ========================================
    # 第二步：Kosaraju 演算法 - 第二遍 DFS
    # ========================================
    # 目的：在反轉圖上，找出所有強連通分量 (SCC)
    # 按 order 的逆順序訪問，這樣能一次走完一個 SCC
    scc_id = [-1] * N             # 每個節點所屬的 SCC 編號
    scc_val = []                  # 每個 SCC 的權值總和
    
    def dfs2(v):
        """
        在反轉圖上做 DFS，找出 SCC 並計算權值總和
        """
        scc_id[v] = len(scc_val)  # 標記此��點所屬的 SCC
        total = values[v]           # 加上此節點的 ATM 金額
        
        # 沿反轉邊訪問
        for w in rev[v]:
            if scc_id[w] == -1:  # 如果還沒被分配到 SCC
                total += dfs2(w)   # 遞迴處理
        
        return total
    
    # 按逆順序處理（order[-1], order[-2], ...）
    for v in reversed(order):
        if scc_id[v] == -1:       # 如果還沒被分配到 SCC
            scc_val.append(dfs2(v))  # 建立新的 SCC
    
    # ========================================
    # 第三步：建立 SCC 壓縮圖
    # ========================================
    # 把每個 SCC 視為一個節點，建立新圖
    K = len(scc_val)              # SCC 數量
    scc_graph = [set() for _ in range(K)]  # SCC 間的邊
    scc_bar = [False] * K         # 記錄哪個 SCC 有酒吧
    
    for i in range(N):
        for j in graph[i]:
            # 如果兩個節點不在同一個 SCC，建立 SCC 間的邊
            if scc_id[i] != scc_id[j]:
                scc_graph[scc_id[i]].add(scc_id[j])
    
    for b in bars:
        scc_bar[scc_id[b]] = True  # 標記有酒吧的 SCC
    
    start_scc = scc_id[start]     # 起點所屬的 SCC
    
    # ========================================
    # 第四步：在 DAG 上做 DP
    # ========================================
    # 目的是找到從起始 SCC 到每個 SCC 的最大權值路徑
    # dp[i] = 到達 SCC i 的最大金額
    dp = [-float('inf')] * K
    dp[start_scc] = 0             # 起始點的金額為 0（還沒開始搶）
    
    # 反覆更新 K 次，確保所有路徑都被考慮到
    for _ in range(K):
        for u in range(K):
            if dp[u] != -float('inf'):  # 如果這個 SCC 可達
                for v in scc_graph[u]:    # 嘗試走到下一個 SCC
                    new_val = dp[u] + scc_val[v]  # 加上目標 SCC 的權值
                    if dp[v] < new_val:      # 如果更好就更新
                        dp[v] = new_val
    
    # ========================================
    # 第五步：找答案
    # ========================================
    # 找到可達酒吧的最大金額
    ans = 0
    for i in range(K):
        if scc_bar[i] and dp[i] > ans:
            ans = dp[i]
    
    return ans

if __name__ == "__main__":
    solve()