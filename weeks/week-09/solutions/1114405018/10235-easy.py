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

    這裡把每個可用格子映射成圖上的一個頂點，
    若兩格上下左右相鄰，則在對應頂點間連一條無向邊。
    """
    verts = []
    vid = {}

    for r in range(n):
        for c in range(m):
            if grid[r][c] == 1:
                vid[(r, c)] = len(verts)
                verts.append((r, c))

    edges = []
    for r, c in verts:
        u = vid[(r, c)]
        if r + 1 < n and grid[r + 1][c] == 1:
            edges.append((u, vid[(r + 1, c)]))
        if c + 1 < m and grid[r][c + 1] == 1:
            edges.append((u, vid[(r, c + 1)]))

    return len(verts), edges


def count_2_regular_subgraphs(n, m, grid):
    """計算所有頂點度數都剛好為 2 的邊子集合數量。

    核心觀念：
    - 每個頂點度數 = 2，代表整張圖被若干個互不相交的環覆蓋
    - 這正對應題目中「每個可用格都恰好被某條蛇覆蓋，且蛇是環」

    做法：
    - 對每條邊做「選 / 不選」DFS 枚舉
    - 透過度數上限與剩餘可補邊數做剪枝，減少搜尋量
    """
    v_cnt, edges = build_graph(n, m, grid)

    # 沒有可用格，答案為 1（不放蛇）
    if v_cnt == 0:
        return 1

    # 原圖中若某頂點鄰接邊不足 2，必定無解
    cap = [0] * v_cnt
    for u, v in edges:
        cap[u] += 1
        cap[v] += 1
    if any(d < 2 for d in cap):
        return 0

    e_cnt = len(edges)

    # rem[x][i] = 從第 i 條邊到最後，仍可能連到頂點 x 的邊數
    # 用於判斷「就算剩下全部都選，x 能不能補到度數 2」
    rem = [[0] * (e_cnt + 1) for _ in range(v_cnt)]
    for i in range(e_cnt - 1, -1, -1):
        u, v = edges[i]
        for x in range(v_cnt):
            rem[x][i] = rem[x][i + 1]
        rem[u][i] += 1
        rem[v][i] += 1

    deg = [0] * v_cnt
    ans = 0

    def dfs(i):
        nonlocal ans

        # 剪枝 1：任何點度數 > 2 直接失敗
        # 剪枝 2：就算剩餘邊全選，仍無法補到 2 也失敗
        for x in range(v_cnt):
            if deg[x] > 2:
                return
            if deg[x] + rem[x][i] < 2:
                return

        if i == e_cnt:
            # 邊已決策完，只有全部頂點都剛好度數 2 才是合法方案
            if all(d == 2 for d in deg):
                ans = (ans + 1) % MOD
            return

        u, v = edges[i]

        # 不選第 i 條邊
        dfs(i + 1)

        # 選第 i 條邊
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
        ans = count_2_regular_subgraphs(n, m, grid)
        out.append(f"Case {i}: {ans}")

    return "\n".join(out) + "\n"


def main():
    """程式進入點：讀 stdin、呼叫 solve、印出答案。"""
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
