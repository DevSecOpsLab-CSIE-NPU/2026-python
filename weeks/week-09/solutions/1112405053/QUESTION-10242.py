import sys
from collections import deque


def solve() -> None:
	data = list(map(int, sys.stdin.buffer.read().split()))
	if not data:
		return

	it = iter(data)
	n = next(it)
	m = next(it)

	graph = [[] for _ in range(n + 1)]
	rev_graph = [[] for _ in range(n + 1)]

	for _ in range(m):
		u = next(it)
		v = next(it)
		graph[u].append(v)
		rev_graph[v].append(u)

	money = [0] * (n + 1)
	for i in range(1, n + 1):
		money[i] = next(it)

	start = next(it)
	p = next(it)
	bars = [next(it) for _ in range(p)]

	# 1) Iterative Kosaraju: first pass for finishing order.
	visited = [0] * (n + 1)
	order = []

	for s in range(1, n + 1):
		if visited[s]:
			continue

		stack = [(s, 0)]
		visited[s] = 1

		while stack:
			u, idx = stack[-1]
			if idx < len(graph[u]):
				v = graph[u][idx]
				stack[-1] = (u, idx + 1)
				if not visited[v]:
					visited[v] = 1
					stack.append((v, 0))
			else:
				order.append(u)
				stack.pop()

	# 2) Second pass on reversed graph: assign SCC id.
	comp_id = [-1] * (n + 1)
	comp_money = []
	comp_bar = []
	bar_set = set(bars)

	for s in reversed(order):
		if comp_id[s] != -1:
			continue

		cid = len(comp_money)
		comp_money.append(0)
		comp_bar.append(False)

		stack = [s]
		comp_id[s] = cid

		while stack:
			u = stack.pop()
			comp_money[cid] += money[u]
			if u in bar_set:
				comp_bar[cid] = True

			for v in rev_graph[u]:
				if comp_id[v] == -1:
					comp_id[v] = cid
					stack.append(v)

	csz = len(comp_money)

	# 3) Build SCC-DAG.
	dag = [[] for _ in range(csz)]
	for u in range(1, n + 1):
		cu = comp_id[u]
		for v in graph[u]:
			cv = comp_id[v]
			if cu != cv:
				dag[cu].append(cv)

	start_c = comp_id[start]

	# 4) Keep only nodes reachable from start SCC.
	reachable = [False] * csz
	q = deque([start_c])
	reachable[start_c] = True
	while q:
		u = q.popleft()
		for v in dag[u]:
			if not reachable[v]:
				reachable[v] = True
				q.append(v)

	indeg = [0] * csz
	for u in range(csz):
		if not reachable[u]:
			continue
		for v in dag[u]:
			if reachable[v]:
				indeg[v] += 1

	# 5) DAG DP (max path sum) from start SCC.
	NEG = -10**30
	dp = [NEG] * csz
	dp[start_c] = comp_money[start_c]

	topo = deque()
	for i in range(csz):
		if reachable[i] and indeg[i] == 0:
			topo.append(i)

	while topo:
		u = topo.popleft()
		if dp[u] != NEG:
			base = dp[u]
			for v in dag[u]:
				if reachable[v] and base + comp_money[v] > dp[v]:
					dp[v] = base + comp_money[v]

		for v in dag[u]:
			if reachable[v]:
				indeg[v] -= 1
				if indeg[v] == 0:
					topo.append(v)

	ans = 0
	for i in range(csz):
		if reachable[i] and comp_bar[i] and dp[i] > ans:
			ans = dp[i]

	print(ans)


if __name__ == "__main__":
	solve()
