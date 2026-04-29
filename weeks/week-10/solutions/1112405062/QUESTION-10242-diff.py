"""
UVA 10242 - Special, Happy Birthday
================================

題目說明：
- 有 N 個路口，M 條單向道路
- 每個路口有 ATM，金額 given
- 部分路口有酒吧
- 從市中心 S 出發，沿單向道路行駛
- 每個 ATM 只能搶一次，最終到某間酒吧
- 求最多能搶到的金額

解題思路：
- 使用 Tarjan 算法找強連通分量 (SCC)
- 壓縮圖後變成 DAG
- 在 DAG 上使用拓撲排序 + DP 求最大路徑權重
- 每個 SCC 的權重 = 區內所有節點 ATM 金額總和
"""

import sys
from collections import deque

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return

    it = iter(data)
    T = 1

    for case in range(T):
        N = int(next(it))
        M = int(next(it))

        graph = [[] for _ in range(N)]
        for _ in range(M):
            u = int(next(it)) - 1
            v = int(next(it)) - 1
            graph[u].append(v)

        values = [int(next(it)) for _ in range(N)]

        S = int(next(it)) - 1
        P = int(next(it))
        bars = [int(next(it)) - 1 for _ in range(P)]

        result = max_rob(N, graph, values, S, bars)
        print(result)

def max_rob(N, graph, values, start, bars):
    """找到從 start 到酒吧的最大金額路徑"""

    # Step 1: Tarjan 找 SCC
    scc_id, scc_val = tarjan_scc(N, graph, values)

    # Step 2: 建立 SCC 壓縮圖（去重邊）
    K = len(scc_val)
    scc_graph = [[] for _ in range(K)]
    edge_set = [set() for _ in range(K)]

    for i in range(N):
        for j in graph[i]:
            ui, uj = scc_id[i], scc_id[j]
            if ui != uj and uj not in edge_set[ui]:
                scc_graph[ui].append(uj)
                edge_set[ui].add(uj)

    # 標記有酒吧的 SCC
    scc_bar = [False] * K
    for bar in bars:
        scc_bar[scc_id[bar]] = True

    start_scc = scc_id[start]

    # Step 3: 拓撲排序 + DP
    in_degree = [0] * K
    for u in range(K):
        for v in scc_graph[u]:
            in_degree[v] += 1

    # 拓撲排序
    q = deque([u for u in range(K) if in_degree[u] == 0])
    topo_order = []
    while q:
        u = q.popleft()
        topo_order.append(u)
        for v in scc_graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)

    # DP: 按照拓撲順序更新
    dp = [-1] * K
    dp[start_scc] = scc_val[start_scc]

    for u in topo_order:
        if dp[u] != -1:
            for v in scc_graph[u]:
                new_val = dp[u] + scc_val[v]
                if dp[v] < new_val:
                    dp[v] = new_val

    # Step 4: 找可達酒吧的最大值
    ans = 0
    for i in range(K):
        if scc_bar[i] and dp[i] != -1:
            ans = max(ans, dp[i])

    return ans

def tarjan_scc(N, graph, values):
    """Tarjan 算法找強連通分量"""
    index_counter = [0]
    stack = []
    onstack = [False] * N
    indices = [-1] * N
    lowlink = [0] * N
    scc_id = [-1] * N
    scc_val = []

    def dfs(v):
        indices[v] = index_counter[0]
        lowlink[v] = index_counter[0]
        index_counter[0] += 1
        stack.append(v)
        onstack[v] = True

        for w in graph[v]:
            if indices[w] == -1:
                dfs(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif onstack[w]:
                lowlink[v] = min(lowlink[v], indices[w])

        if lowlink[v] == indices[v]:
            scc_nodes = []
            while True:
                w = stack.pop()
                onstack[w] = False
                scc_id[w] = len(scc_val)
                scc_nodes.append(w)
                if w == v:
                    break
            val = sum(values[w] for w in scc_nodes)
            scc_val.append(val)

    for v in range(N):
        if indices[v] == -1:
            dfs(v)

    return scc_id, scc_val

if __name__ == "__main__":
    solve()
