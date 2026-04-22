import sys


def min_sum_and_count_1d(arr):
	"""
	一維版本：最小化 sum(|x - arr[i]|)
	回傳：最小值、可以達到最小值的整數 x 個數
	"""
	arr.sort()
	n = len(arr)

	# 奇數個點：中位數唯一
	if n % 2 == 1:
		best_x = arr[n // 2]
		best_sum = 0
		for v in arr:
			best_sum += abs(v - best_x)
		return best_sum, 1

	# 偶數個點：在 [left, right] 的每個整數都最優
	left = arr[n // 2 - 1]
	right = arr[n // 2]

	# 取區間內任一點都可得到最小值，這裡取 left 計算
	best_sum = 0
	for v in arr:
		best_sum += abs(v - left)

	count = right - left + 1
	return best_sum, count


def solve():
	nums = list(map(int, sys.stdin.buffer.read().split()))
	if not nums:
		return

	t = nums[0]
	idx = 1
	ans_lines = []

	for _ in range(t):
		n = nums[idx]
		idx += 1

		xs = []
		ys = []

		for _ in range(n):
			x = nums[idx]
			y = nums[idx + 1]
			idx += 2
			xs.append(x)
			ys.append(y)

		min_x_sum, x_count = min_sum_and_count_1d(xs)
		min_y_sum, y_count = min_sum_and_count_1d(ys)

		min_total = min_x_sum + min_y_sum
		ways = x_count * y_count
		ans_lines.append(f"{min_total} {ways}")

	sys.stdout.write("\n".join(ans_lines))


if __name__ == "__main__":
	solve()
