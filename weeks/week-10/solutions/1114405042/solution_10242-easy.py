def solve_10242_easy():
    import sys
    sys.setrecursionlimit(200000)
    lines = sys.stdin.read().split()
    if not lines: return
    n, m = int(lines[0]), int(lines[1])
    idx = 2
    adj = [[] for _ in range(n + 1)]
    rev_adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = int(lines[idx]), int(lines[idx+1])
        adj[u].append(v)
        rev_adj[v].append(u)
        idx += 2
    cash = [0] * (n + 1)
    for i in range(1, n + 1):
        cash[i] = int(lines[idx])
        idx += 1
    start_node = int(lines[idx])
    p = int(lines[idx+1])
    idx += 2
    bars = set()
    for _ in range(p):
        bars.add(int(lines[idx]))
        idx += 1
        
    visited = [False] * (n + 1)
    order = []
    # Iterative DFS for order to avoid recursion depth issues on large graphs
    def dfs1(start_u):
        stack = [start_u]
        while stack:
            u = stack[-1]
            if not visited[u]:
                visited[u] = True
                for v in adj[u]:
                    if not visited[v]:
                        stack.append(v)
            else:
                if stack[-1] == u:
                    order.append(stack.pop())
                    
    for i in range(1, n + 1):
        if not visited[i]:
            dfs1(i)
            
    scc_id = [0] * (n + 1)
    scc_cash = []
    scc_has_bar = []
    current_scc = 0
    visited = [False] * (n + 1)
    for i in reversed(order):
        if not visited[i]:
            scc_cash.append(0)
            scc_has_bar.append(False)
            stack = [i]
            while stack:
                u = stack.pop()
                if not visited[u]:
                    visited[u] = True
                    scc_id[u] = current_scc
                    scc_cash[-1] += cash[u]
                    if u in bars:
                        scc_has_bar[-1] = True
                    for v in rev_adj[u]:
                        if not visited[v]:
                            stack.append(v)
            current_scc += 1
            
    scc_adj = [[] for _ in range(current_scc)]
    for u in range(1, n + 1):
        for v in adj[u]:
            if scc_id[u] != scc_id[v]:
                scc_adj[scc_id[u]].append(scc_id[v])
                
    memo = [-1] * current_scc
    def dp(u):
        if memo[u] != -1: return memo[u]
        max_val = 0
        for v in scc_adj[u]:
            res = dp(v)
            if res != -1:
                max_val = max(max_val, res)
        if max_val > 0 or scc_has_bar[u]:
            memo[u] = max_val + scc_cash[u]
        else:
            memo[u] = -1
        return memo[u]
        
    print(max(0, dp(scc_id[start_node])))

if __name__ == '__main__':
    solve_10242_easy()