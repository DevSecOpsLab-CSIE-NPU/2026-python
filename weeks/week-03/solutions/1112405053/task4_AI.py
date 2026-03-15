import sys


def count_inversions(train: list[int]) -> int:
	# 計算逆序對數量：i < j 且 train[i] > train[j]
	# 在本題中，逆序對數量就是最少相鄰交換次數
	swaps = 0
	n = len(train)
	for i in range(n):
		for j in range(i + 1, n):
			if train[i] > train[j]:
				swaps += 1
	return swaps


def main() -> None:
	# 一次讀入全部整數，避免逐行處理換行格式差異
	data = list(map(int, sys.stdin.buffer.read().split()))
	if not data:
		return

	# 第一個數字是測資數量
	test_cases = data[0]
	idx = 1
	# 收集每組測資輸出
	output = []

	for _ in range(test_cases):
		# 每組先讀車廂數量 L
		length = data[idx]
		idx += 1

		# 接著讀 L 個車廂編號 
		train = data[idx:idx + length]
		idx += length

		swaps = count_inversions(train)
		# 依題目指定格式輸出
		output.append(f"Optimal train swapping takes {swaps} swaps.")

	sys.stdout.write("\n".join(output))


if __name__ == "__main__":
	main()
