import sys


def one_dimension(values):
	"""
	回傳 (最小距離和, 最優整數點個數)
	對 |x-a_i| 的總和，最小值在中位數（或中位數區間）。
	"""
	values.sort()
	n = len(values)

	if n % 2 == 1:
		m = values[n // 2]
		min_sum = sum(abs(v - m) for v in values)
		return min_sum, 1

	left = values[n // 2 - 1]
	right = values[n // 2]
	# 偶數時，區間 [left, right] 內任何整數都能達到最小值
	m = left
	min_sum = sum(abs(v - m) for v in values)
	count = right - left + 1
	return min_sum, count


def solve():
	data = list(map(int, sys.stdin.buffer.read().split()))
	if not data:
		return

	t = data[0]
	idx = 1
	out = []

	for _ in range(t):
		n = data[idx]
		idx += 1

		xs = []
		ys = []
		for _ in range(n):
			x = data[idx]
			y = data[idx + 1]
			idx += 2
			xs.append(x)
			ys.append(y)

		sx, cx = one_dimension(xs)
		sy, cy = one_dimension(ys)

		min_total = sx + sy
		ways = cx * cy
		out.append(f"{min_total} {ways}")

	sys.stdout.write("\n".join(out))


if __name__ == "__main__":
	solve()
