import sys
from collections import deque


def add_edge(g, u, v, c):
	g[u].append([v, c, len(g[v])])
	g[v].append([u, 0, len(g[u]) - 1])


def dinic(g, s, t):
	n = len(g)
	flow = 0
	INF = 10**30

	while True:
		lv = [-1] * n
		lv[s] = 0
		q = deque([s])
		while q:
			u = q.popleft()
			for v, c, _ in g[u]:
				if c and lv[v] < 0:
					lv[v] = lv[u] + 1
					q.append(v)
		if lv[t] < 0:
			return flow

		it = [0] * n

		def dfs(u, f):
			if u == t:
				return f
			while it[u] < len(g[u]):
				i = it[u]
				v, c, r = g[u][i]
				if c and lv[v] == lv[u] + 1:
					got = dfs(v, min(f, c))
					if got:
						g[u][i][1] -= got
						g[v][r][1] += got
						return got
				it[u] += 1
			return 0

		while True:
			pushed = dfs(s, INF)
			if not pushed:
				break
			flow += pushed


def main():
	a = list(map(int, sys.stdin.buffer.read().split()))
	if not a:
		return
	p = 0
	n, m = a[p], a[p + 1]
	p += 2

	nm = n * m
	score = [0] * nm
	atk = [[] for _ in range(nm)]

	for r in range(n):
		for c in range(m):
			i = r * m + c
			score[i] = a[p]
			p += 1
			w = a[p]
			p += 1
			for _ in range(w):
				rr, cc = a[p], a[p + 1]
				p += 2
				atk[i].append(rr * m + cc)

	S, T = nm, nm + 1
	g = [[] for _ in range(nm + 2)]

	pos = 0
	neg = 0
	for i, v in enumerate(score):
		if v > 0:
			pos += v
			add_edge(g, S, i, v)
		elif v < 0:
			neg += -v
			add_edge(g, i, T, -v)

	INF = pos + neg + 1

	# choose x => must choose all prerequisites of x
	for r in range(n):
		for c in range(m):
			x = r * m + c
			if c:
				add_edge(g, x, x - 1, INF)
			for y in atk[x]:
				add_edge(g, x, y, INF)

	print(pos - dinic(g, S, T))


if __name__ == "__main__":
	main()
