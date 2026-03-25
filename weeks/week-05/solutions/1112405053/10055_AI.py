import sys


# Fenwick Tree（Binary Indexed Tree）
# 支援：單點加值、前綴和、區間和，時間複雜度皆為 O(log n)
class FenwickTree:
	def __init__(self, size: int) -> None:
		self.n = size
		self.bit = [0] * (size + 1)

	def add(self, index: int, delta: int) -> None:
		while index <= self.n:
			self.bit[index] += delta
			index += index & -index

	def prefix_sum(self, index: int) -> int:
		total = 0
		while index > 0:
			total += self.bit[index]
			index -= index & -index
		return total

	def range_sum(self, left: int, right: int) -> int:
		return self.prefix_sum(right) - self.prefix_sum(left - 1)


def main() -> None:
	# 一次讀入所有整數
	data = list(map(int, sys.stdin.buffer.read().split()))
	if not data:
		return

	n, q = data[0], data[1]
	idx = 2

	ft = FenwickTree(n)
	# state[i]：fi 目前狀態（0=遞增, 1=遞減）
	state = [0] * (n + 1)
	out = []

	for _ in range(q):
		v = data[idx]
		idx += 1

		if v == 1:
			# 反轉第 i 個函數狀態，並同步更新 Fenwick Tree
			i = data[idx]
			idx += 1
			if state[i] == 0:
				state[i] = 1
				ft.add(i, 1)
			else:
				state[i] = 0
				ft.add(i, -1)
		else:
			# 查詢區間 [l, r] 內遞減函數數量，奇數 -> 整體遞減(1)，偶數 -> 遞增(0)
			l = data[idx]
			r = data[idx + 1]
			idx += 2
			decreasing_count = ft.range_sum(l, r)
			out.append(str(decreasing_count & 1))

	sys.stdout.write("\n".join(out))


if __name__ == "__main__":
	main()
