import sys


def count_inversions(arr: list[int]) -> int:
	# 逆序對計數：統計所有前大後小的配對數
	# 對應題意中的最少交換次數
	swaps = 0
	n = len(arr)
	for i in range(n):
		for j in range(i + 1, n):
			if arr[i] > arr[j]:
				swaps += 1
	return swaps


def main() -> None:
	# 讀入所有整數資料（包含測資數、L、排列）
	data = list(map(int, sys.stdin.buffer.read().split()))
	if not data:
		return

	# 測資筆數
	t = data[0]
	index = 1
	# 儲存最終輸出行 
	out = []

	for _ in range(t):
		# 本組列車長度 L
		l = data[index]
		index += 1

		# 本組列車排列
		train = data[index:index + l]
		index += l

		s = count_inversions(train)
		# 依題目指定格式輸出
		out.append(f"Optimal train swapping takes {s} swaps.")

	sys.stdout.write("\n".join(out))


if __name__ == "__main__":
	main()
