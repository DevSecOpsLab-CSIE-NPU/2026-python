import sys

# 增加遞迴深度以處理較大的圖
sys.setrecursionlimit(1000000)

def solve():
    """
    UVA 10242 魔改版：ATM 搶劫
    解法：
    1. 使用 Tarjan 演算法找出圖中所有的強連通分量 (SCC)。
    2. 將每個 SCC 縮成一個點，建立縮點後的有向無環圖 (DAG)。
    3. 計算每個 SCC 點的總金額 (該 SCC 內所有 ATM 金額之和)。
    4. 在 DAG 上使用動態規劃或拓撲排序找出從起點 SCC 到達任一含酒吧 SCC 的最大路徑和。
    """
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    ptr = 0
    N = int(input_data[ptr])
    M = int(input_data[ptr+1])
    ptr += 2

    adj = [[] for _ in range(N + 1)]
    for _ in range(M):
        u = int(input_data[ptr])
        v = int(input_data[ptr+1])
        adj[u].append(v)
        ptr += 2

    atm_values = [0] * (N + 1)
    for i in range(1, N + 1):
        atm_values[i] = int(input_data[ptr])
        ptr += 1

    S = int(input_data[ptr])
    P = int(input_data[ptr+1])
    ptr += 2

    bar_nodes = set()
    for _ in range(P):
        bar_nodes.add(int(input_data[ptr]))
        ptr += 1

    # --- Tarjan SCC ---
    dfn = [0] * (N + 1)
    low = [0] * (N + 1)
    stack = []
    in_stack = [False] * (N + 1)
    scc_id = [0] * (N + 1)
    scc_count = 0
    timer = 0

    def find_scc(u):
        nonlocal timer, scc_count
        timer += 1
        dfn[u] = low[u] = timer
        stack.append(u)
        in_stack[u] = True

        for v in adj[u]:
            if not dfn[v]:
                find_scc(v)
                low[u] = min(low[u], low[v])
            elif in_stack[v]:
                low[u] = min(low[u], dfn[v])

        if low[u] == dfn[u]:
            scc_count += 1
            while True:
                node = stack.pop()
                in_stack[node] = False
                scc_id[node] = scc_count
                if node == u:
                    break

    for i in range(1, N + 1):
        if not dfn[i]:
            find_scc(i)

    # --- 縮點建立 DAG ---
    scc_values = [0] * (scc_count + 1)
    scc_has_bar = [False] * (scc_count + 1)
    dag_adj = [set() for _ in range(scc_count + 1)]

    for i in range(1, N + 1):
        sid = scc_id[i]
        scc_values[sid] += atm_values[i]
        if i in bar_nodes:
            scc_has_bar[sid] = True
        for v in adj[i]:
            if scc_id[v] != sid:
                dag_adj[sid].add(scc_id[v])

    # --- DAG DP (最長路) ---
    # dp[i] 表示從包含 S 的 SCC 到達 SCC i 的最大搶劫金額
    # 初始化為極小值，代表不可達
    dp = [-1] * (scc_count + 1)
    start_scc = scc_id[S]
    dp[start_scc] = scc_values[start_scc]

    # 拓撲排序順序（scc_id 是依據遍歷順序產生的，其逆序通常接近拓撲序）
    # 但為了保險，我們手動做一次簡單的遞迴 DP
    memo = {}
    def get_max_rob(sid):
        if sid in memo:
            return memo[sid]

        # 初始金額為自己 SCC 的金額
        # 這裡的邏輯改為：從 sid 出發能拿到的最大金額（需可達酒吧）
        res = -1
        if scc_has_bar[sid]:
            res = scc_values[sid]

        for next_sid in dag_adj[sid]:
            sub_res = get_max_rob(next_sid)
            if sub_res != -1:
                res = max(res, scc_values[sid] + sub_res)

        memo[sid] = res
        return res

    result = get_max_rob(start_scc)
    print(max(0, result))

if __name__ == "__main__":
    solve()
