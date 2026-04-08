import sys


class FenwickTree:
	# Fenwick Tree 維護可用品牌編號的出現次數（1 表示可用，0 表示已用掉）。
	def __init__(self, n: int) -> None:
		self.n = n
		self.bit = [0] * (n + 1)

	# 單點加值：把某個品牌標記為可用或移除（delta 可為 +1 或 -1）。
	def add(self, idx: int, delta: int) -> None:
		while idx <= self.n:
			self.bit[idx] += delta
			idx += idx & -idx

	def kth(self, k: int) -> int:
		# 找目前可用品牌中的第 k 小編號。
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
	# 一開始 1..N 每個品牌都可用，頻率先設為 1。
	for x in range(1, n + 1):
		ft.add(x, 1) 

	ans = [0] * (n + 1)
	# 由後往前還原：第 i 位要選「目前剩下中第 smaller_before[i] + 1 小」的品牌。
	for i in range(n, 0, -1):
		k = smaller_before[i] + 1
		brand = ft.kth(k)
		ans[i] = brand
		ft.add(brand, -1)

	sys.stdout.write("\n".join(map(str, ans[1:])))


if __name__ == "__main__":
	main()
