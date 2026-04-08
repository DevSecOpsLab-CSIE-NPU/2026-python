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
		# Find the smallest index pos such that prefix_sum(pos) >= k.
		pos = 0
		bitmask = 1 << (self.n.bit_length() - 1)
		while bitmask:
			nxt = pos + bitmask
			if nxt <= self.n and self.bit[nxt] < k:
				k -= self.bit[nxt]
				pos = nxt
			bitmask >>= 1
		return pos + 1


def main() -> None:
	data = list(map(int, sys.stdin.buffer.read().split()))
	if not data:
		return

	n = data[0]
	smaller_before = [0] * (n + 1)
	for i in range(2, n + 1):
		smaller_before[i] = data[i - 1]

	ft = FenwickTree(n)
	for x in range(1, n + 1):
		ft.add(x, 1)

	ans = [0] * (n + 1)
	for i in range(n, 0, -1):
		k = smaller_before[i] + 1
		brand = ft.kth(k)
		ans[i] = brand
		ft.add(brand, -1) 

	sys.stdout.write("\n".join(map(str, ans[1:])))


if __name__ == "__main__":
	main()
