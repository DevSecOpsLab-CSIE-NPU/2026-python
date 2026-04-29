import sys
from collections import deque, defaultdict


def solve(text):
    """求從起點出發到任一酒吧可取得的最大 ATM 金額（優化版）。

    優化策略：
    1. 使用 defaultdict 簡化邊的去重邏輯
    2. 改善數據結構選擇（deque 用於 BFS/拓樸排序）
    3. 合併重複的邊界檢查，減少代碼冗餘
    4. 使用生成器表達式替代列表推導式中的條件判斷
    5. 優化輔助標記數組初始化
    """
    # 將整份輸入攤平成整數串列
    a = list(map(int, text.split()))
    if not a:
        return ""

    # 讀入基本圖資訊
    it = iter(a)
    n, m = next(it), next(it)

    # 使用 defaultdict 簡化邊表管理
    g = defaultdict(list)  # 原圖
    rg = defaultdict(list)  # 反向圖
    
    for _ in range(m):
        u, v = next(it), next(it)
        g[u].append(v)
        rg[v].append(u)

    # 讀取 ATM 金額
    money = [0] * (n + 1)
    for i in range(1, n + 1):
        money[i] = next(it)

    # 讀取起點、酒吧資訊
    s, p = next(it), next(it)
    bars = {next(it) for _ in range(p)}

    sys.setrecursionlimit(1000000)

    # ---------- Kosaraju 第 1 次 DFS：求完成順序 ----------
    vis = [False] * (n + 1)
    order = []

    def dfs1(u):
        """DFS 計算完成順序，改用迭代避免遞迴深度問題"""
        stack = [u]
        path = []
        
        while stack:
            node = stack[-1]
            if vis[node]:
                stack.pop()
                if node in path:
                    order.append(node)
                    path.remove(node)
                continue
            
            vis[node] = True
            path.append(node)
            
            for v in g[node]:
                if not vis[v]:
                    stack.append(v)

    for i in range(1, n + 1):
        if not vis[i]:
            dfs1(i)

    # ---------- Kosaraju 第 2 次 DFS：切 SCC ----------
    comp = [0] * (n + 1)
    sm = []      # 各 SCC 的 ATM 金額總和
    has_bar = [] # 各 SCC 是否含酒吧

    def dfs2(u, cid):
        """遞迴方式更清晰"""
        comp[u] = cid
        sm[cid] += money[u]
        has_bar[cid] = has_bar[cid] or (u in bars)
        
        for v in rg[u]:
            if comp[v] == 0:
                dfs2(v, cid)

    for u in reversed(order):
        if comp[u] == 0:
            sm.append(0)
            has_bar.append(False)
            dfs2(u, len(sm) - 1)

    # ---------- 縮點成 DAG（使用集合自動去重）----------
    k = len(sm)
    dag = [set() for _ in range(k)]
    
    for u in range(1, n + 1):
        cu = comp[u]
        for v in g[u]:
            cv = comp[v]
            if cu != cv:
                dag[cu].add(cv)

    # ---------- 計算「從起點 SCC 可達」的節點 ----------
    start = comp[s]
    reach = [False] * k
    queue = deque([start])
    reach[start] = True
    
    while queue:
        u = queue.popleft()
        for v in dag[u]:
            if not reach[v]:
                reach[v] = True
                queue.append(v)

    # ---------- 拓樸排序 + DP（使用 deque 提高效率）----------
    indeg = [0] * k
    for u in range(k):
        if reach[u]:
            for v in dag[u]:
                if reach[v]:
                    indeg[v] += 1

    NEG_INF = -10**30
    dp = [NEG_INF] * k
    dp[start] = sm[start]

    # 初始化入度為 0 的可達節點
    q = deque(u for u in range(k) if reach[u] and indeg[u] == 0)

    while q:
        u = q.popleft()
        
        if dp[u] == NEG_INF:
            continue
        
        # 鬆弛後繼邊
        for v in dag[u]:
            if reach[v]:
                if dp[u] + sm[v] > dp[v]:
                    dp[v] = dp[u] + sm[v]
                
                # 更新入度，變 0 就入隊
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

    # 在「可達 + 含酒吧」的 SCC 中取最大答案
    ans = max(
        (dp[i] for i in range(k) if reach[i] and has_bar[i]),
        default=0
    )
    
    return str(ans) + "\n"


def main():
    """標準輸入輸出入口。"""
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
