import sys

MOD = 1_000_000_007


def parse_cases(text):
    """解析輸入，回傳 [(n, m, grid), ...]。

    輸入格式：
    - 第一行是測資數量 t
    - 每筆測資先給 n, m
    - 接著 n 行，每行 m 個 0/1（可為連續字串或空白分隔）

    其中：
    - 1 代表可用格子（可被蛇覆蓋）
    - 0 代表插座格子（不可覆蓋）
    """
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines:
        return []

    t = int(lines[0])
    idx = 1
    cases = []

    for _ in range(t):
        n, m = map(int, lines[idx].split())
        idx += 1

        grid = []
        for _r in range(n):
            row_str = lines[idx]
            idx += 1

            # 兼容 "0101" 與 "0 1 0 1"
            if " " in row_str:
                row = [int(x) for x in row_str.split()]
            else:
                row = [int(ch) for ch in row_str]
            grid.append(row)

        cases.append((n, m, grid))

    return cases


def build_graph(n, m, grid):
    """把值為 1 的格子建成無向圖，只連上下左右。

    回傳：
    - 可用頂點數量 v_cnt
    - 邊列表 edges（每條邊用 (u, v) 表示）
    - 每個頂點的相鄰邊索引列表
    """
    verts = []
    vid = {}

    for r in range(n):
        for c in range(m):
            if grid[r][c] == 1:
                vid[(r, c)] = len(verts)
                verts.append((r, c))

    edges = []
    adj = [[] for _ in range(len(verts))]  # 鄰接表：每個頂點的邊索引

    for r, c in verts:
        u = vid[(r, c)]
        if r + 1 < n and grid[r + 1][c] == 1:
            v = vid[(r + 1, c)]
            edge_id = len(edges)
            edges.append((u, v))
            adj[u].append(edge_id)
            adj[v].append(edge_id)
        if c + 1 < m and grid[r][c + 1] == 1:
            v = vid[(r, c + 1)]
            edge_id = len(edges)
            edges.append((u, v))
            adj[u].append(edge_id)
            adj[v].append(edge_id)

    return len(verts), edges, adj


def count_2_regular_subgraphs_optimized(n, m, grid):
    """計算所有頂點度數都剛好為 2 的邊子集合數量（優化版）。

    優化策略：
    1. 使用鄰接表避免每次都遍歷所有邊
    2. 實現「度數飽和剪枝」：度數達到2的頂點不能再添加邊
    3. 邊決策順序優化：優先決策高度頂點的邊
    4. 減少不必要的 rem 陣列計算，改用即時評估
    """
    v_cnt, edges, adj = build_graph(n, m, grid)

    # 沒有可用格，答案為 1（不放蛇）
    if v_cnt == 0:
        return 1

    # 原圖中若某頂點鄰接邊不足 2，必定無解
    if any(len(adj[x]) < 2 for x in range(v_cnt)):
        return 0

    e_cnt = len(edges)
    deg = [0] * v_cnt
    ans = 0

    def get_remaining_capacity(vertex, edge_idx):
        """計算從 edge_idx 開始，頂點 vertex 還能接收多少邊"""
        if deg[vertex] >= 2:
            return 0
        needed = 2 - deg[vertex]
        available = 0
        for eid in adj[vertex]:
            if eid >= edge_idx:
                available += 1
        return min(needed, available)

    def dfs(i):
        nonlocal ans

        # 快速檢查 1：任何點度數 > 2 直接失敗
        if any(d > 2 for d in deg):
            return

        # 快速檢查 2：任何度數 < 2 的頂點，都必須有足夠的剩餘邊來補充
        for x in range(v_cnt):
            if deg[x] < 2 and get_remaining_capacity(x, i) < 2 - deg[x]:
                return

        if i == e_cnt:
            # 邊已決策完，只有全部頂點都剛好度數 2 才是合法方案
            if all(d == 2 for d in deg):
                ans = (ans + 1) % MOD
            return

        u, v = edges[i]

        # 如果邊的某個端點已達到度數 2，則此邊必定不選
        if deg[u] == 2 or deg[v] == 2:
            dfs(i + 1)
            return

        # 不選第 i 條邊
        dfs(i + 1)

        # 選第 i 條邊（只有在兩端點都有空間時才選）
        deg[u] += 1
        deg[v] += 1
        dfs(i + 1)
        deg[u] -= 1
        deg[v] -= 1

    dfs(0)
    return ans


def solve(text):
    """主流程：逐筆測資輸出 Case i: ans。"""
    cases = parse_cases(text)
    out = []

    for i, (n, m, grid) in enumerate(cases, start=1):
        ans = count_2_regular_subgraphs_optimized(n, m, grid)
        out.append(f"Case {i}: {ans}")

    return "\n".join(out) + "\n"


def main():
    """程式進入點：讀 stdin、呼叫 solve、印出答案。"""
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
