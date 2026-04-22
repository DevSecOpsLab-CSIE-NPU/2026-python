import sys
from collections import deque


def build_scc(n, graph, rev_graph, money, bars):
	"""Kosaraju（迭代版）：回傳每個點的 SCC id、每個 SCC 的金額總和、是否含酒吧。"""
	visited = [False] * (n + 1)
	finish_order = []

	# 第一次 DFS：取得完成順序
	for start in range(1, n + 1):
		if visited[start]:
			continue

		stack = [(start, 0)]
		visited[start] = True

		while stack:
			u, idx = stack[-1]
			if idx < len(graph[u]):
				v = graph[u][idx]
				stack[-1] = (u, idx + 1)
				if not visited[v]:
					visited[v] = True
					stack.append((v, 0))
			else:
				finish_order.append(u)
				stack.pop()

	# 第二次 DFS（反圖）：切出 SCC
	comp_id = [-1] * (n + 1)
	comp_money = []
	comp_has_bar = []
	bar_set = set(bars)

	for start in reversed(finish_order):
		if comp_id[start] != -1:
			continue

		cid = len(comp_money)
		comp_money.append(0)
		comp_has_bar.append(False)

		stack = [start]
		comp_id[start] = cid

		while stack:
			u = stack.pop()
			comp_money[cid] += money[u]
			if u in bar_set:
				comp_has_bar[cid] = True

			for v in rev_graph[u]:
				if comp_id[v] == -1:
					comp_id[v] = cid
					stack.append(v)

	return comp_id, comp_money, comp_has_bar


def build_condensed_dag(n, graph, comp_id, comp_count):
	"""把原圖縮成 SCC DAG。"""
	dag = [[] for _ in range(comp_count)]

	for u in range(1, n + 1):
		cu = comp_id[u]
		for v in graph[u]:
			cv = comp_id[v]
			if cu != cv:
				dag[cu].append(cv)

	return dag


def max_money_to_bar(start_comp, dag, comp_money, comp_has_bar):
	"""在 DAG 上做最長路 DP，回傳從 start_comp 到任一酒吧 SCC 的最大值。"""
	csz = len(dag)

	# 只保留起點可達區域
	reachable = [False] * csz
	q = deque([start_comp])
	reachable[start_comp] = True

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

	neg_inf = -10**30
	dp = [neg_inf] * csz
	dp[start_comp] = comp_money[start_comp]

	topo = deque(i for i in range(csz) if reachable[i] and indeg[i] == 0)

	while topo:
		u = topo.popleft()

		if dp[u] != neg_inf:
			for v in dag[u]:
				if reachable[v]:
					cand = dp[u] + comp_money[v]
					if cand > dp[v]:
						dp[v] = cand

		for v in dag[u]:
			if reachable[v]:
				indeg[v] -= 1
				if indeg[v] == 0:
					topo.append(v)

	ans = 0
	for i in range(csz):
		if reachable[i] and comp_has_bar[i]:
			ans = max(ans, dp[i])
	return ans


def solve():
	nums = list(map(int, sys.stdin.buffer.read().split()))
	if not nums:
		return

	it = iter(nums)
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

	comp_id, comp_money, comp_has_bar = build_scc(n, graph, rev_graph, money, bars)
	dag = build_condensed_dag(n, graph, comp_id, len(comp_money))
	start_comp = comp_id[start]

	print(max_money_to_bar(start_comp, dag, comp_money, comp_has_bar))


if __name__ == "__main__":
	solve()
