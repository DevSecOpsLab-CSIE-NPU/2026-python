import sys

MOD = 1_000_000_007


def parse_cases(text):
    
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
    
    v_cnt, edges = build_graph(n, m, grid)

    
    if v_cnt == 0:
        return 1

    cap = [0] * v_cnt
    for u, v in edges:
        cap[u] += 1
        cap[v] += 1
    if any(d < 2 for d in cap):
        return 0

    e_cnt = len(edges)

    
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

        for x in range(v_cnt):
            if deg[x] > 2:
                return
            if deg[x] + rem[x][i] < 2:
                return

        if i == e_cnt:
            if all(d == 2 for d in deg):
                ans = (ans + 1) % MOD
            return

        u, v = edges[i]

        dfs(i + 1)

        deg[u] += 1
        deg[v] += 1
        dfs(i + 1)
        deg[u] -= 1
        deg[v] -= 1

    dfs(0)
    return ans


def solve(text):
    cases = parse_cases(text)
    out = []

    for i, (n, m, grid) in enumerate(cases, start=1):
        ans = count_2_regular_subgraphs(n, m, grid)
        out.append(f"Case {i}: {ans}")

    return "\n".join(out) + "\n"


def main():
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()