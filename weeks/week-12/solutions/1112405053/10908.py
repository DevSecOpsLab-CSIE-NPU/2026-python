
import sys


class DSU:
	def __init__(self, n):
		self.parent = list(range(n))
		self.rank = [0] * n

	def find(self, x):
		while self.parent[x] != x:
			self.parent[x] = self.parent[self.parent[x]]
			x = self.parent[x]
		return x

	def union(self, a, b):
		ra = self.find(a)
		rb = self.find(b)
		if ra == rb:
			return False
		if self.rank[ra] < self.rank[rb]:
			self.parent[ra] = rb
		else:
			self.parent[rb] = ra
			if self.rank[ra] == self.rank[rb]:
				self.rank[ra] += 1
		return True


def main():
	data = sys.stdin.read().strip().split()
	if not data:
		return
	it = iter(map(int, data))
	try:
		n = next(it)
		m = next(it)
	except StopIteration:
		return

	edges = []
	for _ in range(m):
		try:
			u = next(it) - 1
			v = next(it) - 1
			w = next(it)
		except StopIteration:
			break
		edges.append((w, u, v))

	edges.sort()
	dsu = DSU(n)
	total = 0
	used = 0
	for w, u, v in edges:
		if dsu.union(u, v):
			total += w
			used += 1
			if used == n - 1:
				break

	if n == 0:
		print(0)
		return
	# check connectivity
	roots = set(dsu.find(i) for i in range(n))
	if len(roots) == 1:
		print(total)
	else:
		print(-1)


if __name__ == '__main__':
	main()

