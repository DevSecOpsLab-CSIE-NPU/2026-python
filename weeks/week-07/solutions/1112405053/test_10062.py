import sys


class FenwickTree:
	def __init__(self, n: int) -> None:
		self.n = n 
		self.bit = [0] * (n + 1)

	def add(self, idx: int, delta: int) -> None:
		while idx <= self.n:
			self.bit[idx] += delta
			idx += idx & -idx

	def kth(self, k: int) -> int:
		# 找到前綴和大於等於 k 的最小索引。
		idx = 0
		step = 1 << (self.n.bit_length() - 1)
		while step:
			nxt = idx + step
			if nxt <= self.n and self.bit[nxt] < k:
				k -= self.bit[nxt]
				idx = nxt
			step >>= 1
		return idx + 1


def solve() -> None:
	data = list(map(int, sys.stdin.buffer.read().split()))
	if not data:
		return

	n = data[0]
	smaller_before = [0] * (n + 1)
	for i in range(2, n + 1):
		smaller_before[i] = data[i - 1]

	fw = FenwickTree(n)
	for brand in range(1, n + 1):
		fw.add(brand, 1)

	ans = [0] * (n + 1)
	for pos in range(n, 0, -1):
		k = smaller_before[pos] + 1
		brand = fw.kth(k)
		ans[pos] = brand
		fw.add(brand, -1)

	sys.stdout.write("\n".join(map(str, ans[1:])))


if __name__ == "__main__":
	solve()
