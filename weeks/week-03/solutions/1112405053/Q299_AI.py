import sys


def count_swaps(train: list[int]) -> int:
	# 計算最少交換次數（等同於此排列中的逆序對數量）
	swaps = 0
	length = len(train)

	# 檢查所有 i < j，若 train[i] > train[j] 代表需要一次交換
	for i in range(length):
		for j in range(i + 1, length):
			if train[i] > train[j]:
				swaps += 1

	return swaps


def main() -> None:
	# 以 token 方式讀入，方便處理多行輸入
	tokens = sys.stdin.read().split()
	if not tokens:
		return

	index = 0
	# 第一個數字是測資組數
	test_cases = int(tokens[index])
	index += 1

	output = []

	for _ in range(test_cases):
		# 每組先讀火車長度 L，再讀 L 個車廂編號
		length = int(tokens[index])
		index += 1

		train = list(map(int, tokens[index:index + length]))
		index += length

		swaps = count_swaps(train)
		# 依題目指定格式輸出
		output.append(f"Optimal train swapping takes {swaps} swaps.")

	sys.stdout.write("\n".join(output))


if __name__ == "__main__":
	main()
