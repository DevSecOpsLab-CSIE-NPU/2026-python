import sys


def solve(text):
    """求從起點出發到任一酒吧可取得的最大 ATM 金額。

    解法骨架：
    1. 先把有向圖做 SCC（強連通分量）縮點。
       因為在同一個 SCC 內可互相到達，所以可把該 SCC 內的 ATM 金額一次全拿。
    2. 把 SCC 圖壓成 DAG 後，從起點所在 SCC 出發做最大路徑 DP。
    3. 在可達且含酒吧的 SCC 中取最大值。
    """
    # 將整份輸入攤平成整數串列，方便用 iterator 順序讀取
    a = list(map(int, text.split()))
    if not a:
        return ""

    # 讀入基本圖資訊：n 個節點、m 條有向邊
    it = iter(a)
    n, m = next(it), next(it)

    # g: 原圖鄰接表, rg: 反向圖鄰接表（Kosaraju 會用到）
    g = [[] for _ in range(n + 1)]
    rg = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = next(it), next(it)
        g[u].append(v)
        rg[v].append(u)

    # money[i]：第 i 個路口 ATM 金額（1-based）
    money = [0] + [next(it) for _ in range(n)]

    # s: 起點, p: 酒吧數量, bars: 酒吧節點集合
    s, p = next(it), next(it)
    bars = {next(it) for _ in range(p)}

    # 避免遞迴 DFS 在大圖時爆遞迴深度
    sys.setrecursionlimit(1000000)

    # ---------- Kosaraju 第 1 次 DFS：求完成順序 ----------
    vis, order = [0] * (n + 1), []

    def dfs1(u):
        # 標記拜訪，沿原圖走到底，回溯時記錄 finishing order
        vis[u] = 1
        for v in g[u]:
            if not vis[v]:
                dfs1(v)
        order.append(u)

    for i in range(1, n + 1):
        if not vis[i]:
            dfs1(i)

    # ---------- Kosaraju 第 2 次 DFS：在反圖上切 SCC ----------
    # comp[u] = 節點 u 所屬 SCC 編號
    # sm[cid] = 該 SCC 的 ATM 金額總和
    # has_bar[cid] = 該 SCC 是否含酒吧
    comp, sm, has_bar = [0] * (n + 1), [], []

    def dfs2(u, cid):
        # 在反圖上把同一 SCC 節點全部收進來
        comp[u] = cid
        sm[cid] += money[u]
        has_bar[cid] |= u in bars
        for v in rg[u]:
            if not comp[v]:
                dfs2(v, cid)

    for u in reversed(order):
        if not comp[u]:
            sm.append(0)
            has_bar.append(False)
            dfs2(u, len(sm) - 1)

    # ---------- 縮點成 DAG ----------
    # 每個 SCC 變成一個點，SCC 間邊去重後保存在 dag
    k = len(sm)
    dag = [set() for _ in range(k)]
    for u in range(1, n + 1):
        cu = comp[u]
        for v in g[u]:
            cv = comp[v]
            if cu != cv:
                dag[cu].add(cv)

    # ---------- 只考慮「從起點 SCC 可達」的子圖 ----------
    start = comp[s]
    reach = [0] * k
    st = [start]
    reach[start] = 1
    while st:
        u = st.pop()
        for v in dag[u]:
            if not reach[v]:
                reach[v] = 1
                st.append(v)

    # ---------- 對可達 DAG 做拓樸 DP ----------
    # dp[c]：到 SCC c 可取得的最大金額
    # 先計算可達子圖中的入度，之後用 Kahn 風格處理
    indeg = [0] * k
    for u in range(k):
        if reach[u]:
            for v in dag[u]:
                if reach[v]:
                    indeg[v] += 1

    neg = -10**30
    dp = [neg] * k
    dp[start] = sm[start]

    # 先把可達且入度為 0 的點放進 queue
    q = [u for u in range(k) if reach[u] and indeg[u] == 0]

    # 這裡用「遍歷可增長 list」技巧，等價於 queue pop(0) 但更省成本
    for u in q:
        # 若此點可達，嘗試鬆弛所有後繼
        if dp[u] != neg:
            for v in dag[u]:
                if reach[v] and dp[u] + sm[v] > dp[v]:
                    dp[v] = dp[u] + sm[v]

        # Kahn 拓樸：更新後繼入度，變 0 就入隊
        for v in dag[u]:
            if reach[v]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

    # 在「可達 + 含酒吧」的 SCC 中取最大答案
    ans = max((dp[i] for i in range(k) if reach[i] and has_bar[i]), default=0)
    return str(ans) + "\n"


def main():
    """標準輸入輸出入口。"""
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()