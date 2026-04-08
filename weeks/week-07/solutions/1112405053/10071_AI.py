import sys
from bisect import bisect_left, bisect_right


def main() -> None:
	# 一次讀完整筆測資：第 1 個數字是 N，後面 N 個是集合 S 的元素。
	data = list(map(int, sys.stdin.buffer.read().split()))
	if not data:
		return

	n = data[0]
	s = data[1 : 1 + n]

	left_values = []
	right_values = []

	# 左式：a * b + c，列舉所有 (a, b, c) 組合。
	for a in s:
		for b in s:
			ab = a * b
			for c in s:
				left_values.append(ab + c)

	# 右式：d * (e + f)，題目限制 d 不能為 0。
	for d in s:
		if d == 0:
			continue
		for e in s:
			for f in s:
				right_values.append(d * (e + f))

	# 將右式排序，之後可用二分搜尋統計某值出現次數。
	right_values.sort()

	ans = 0
	# 對每個左式值 v，累加 v 在右式中出現的次數。
	for v in left_values:
		ans += bisect_right(right_values, v) - bisect_left(right_values, v)

	sys.stdout.write(str(ans))


if __name__ == "__main__":
	main() 
