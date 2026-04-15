import sys
from collections import deque


class Dinic:
	def __init__(self, n: int) -> None:
		self.n = n
		self.graph = [[] for _ in range(n)]

	def add_edge(self, u: int, v: int, c: int) -> None:
		self.graph[u].append([v, c, len(self.graph[v])])
		self.graph[v].append([u, 0, len(self.graph[u]) - 1])

	def max_flow(self, s: int, t: int) -> int:
		flow = 0
		inf = 10**30

		while True:
			level = [-1] * self.n
			level[s] = 0
			q = deque([s])
			while q:
				u = q.popleft()
				for v, cap, _ in self.graph[u]:
					if cap > 0 and level[v] < 0:
						level[v] = level[u] + 1
						q.append(v)

			if level[t] < 0:
				break

			it = [0] * self.n

			def dfs(u: int, pushed: int) -> int:
				if u == t:
					return pushed
				while it[u] < len(self.graph[u]):
					idx = it[u]
					v, cap, rev = self.graph[u][idx]
					if cap > 0 and level[v] == level[u] + 1:
						got = dfs(v, min(pushed, cap))
						if got > 0:
							self.graph[u][idx][1] -= got
							self.graph[v][rev][1] += got
							return got
					it[u] += 1
				return 0

			while True:
				pushed = dfs(s, inf)
				if pushed == 0:
					break
				flow += pushed

		return flow


def main() -> None:
	data = list(map(int, sys.stdin.buffer.read().split()))
	if not data:
		return

	ptr = 0
	n = data[ptr]
	ptr += 1
	m = data[ptr]
	ptr += 1

	total = n * m
	score = [0] * total
	attacks = [[] for _ in range(total)]

	for r in range(n):
		for c in range(m):
			idx = r * m + c
			score[idx] = data[ptr]
			ptr += 1
			w = data[ptr]
			ptr += 1
			arr = attacks[idx]
			for _ in range(w):
				rr = data[ptr]
				cc = data[ptr + 1]
				ptr += 2
				arr.append(rr * m + cc)

	s = total
	t = total + 1
	dinic = Dinic(total + 2)

	pos_sum = 0
	for i, sc in enumerate(score):
		if sc > 0:
			pos_sum += sc
			dinic.add_edge(s, i, sc)
		elif sc < 0:
			dinic.add_edge(i, t, -sc)

	inf = pos_sum + sum(-x for x in score if x < 0) + 1

	for r in range(n):
		for c in range(m):
			v = r * m + c
			if c > 0:
				dinic.add_edge(v, r * m + (c - 1), inf)
			for protector in attacks[v]:
				dinic.add_edge(v, protector, inf)

	min_cut = dinic.max_flow(s, t)
	ans = pos_sum - min_cut
	print(ans)


if __name__ == "__main__":
	main()
