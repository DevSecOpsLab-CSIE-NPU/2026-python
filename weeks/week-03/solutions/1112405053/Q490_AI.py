import sys


def main() -> None:
	# 讀入所有行（保留每行中的空白，不含行尾換行字元）
	lines = sys.stdin.read().splitlines()
	if not lines:
		return

	# 找出最長行，作為旋轉後的列數
	max_length = max(len(line) for line in lines)
	rotated = []

	# 順時針旋轉 90 度：新矩陣的每一列來自原矩陣的一個 column
	for column in range(max_length):
		new_row = []
		# 由下往上讀取原本各行，形成旋轉後的一列
		for row in range(len(lines) - 1, -1, -1):
			if column < len(lines[row]):
				new_row.append(lines[row][column])
			else:
				# 原行長度不足時補空白，避免字元錯位
				new_row.append(" ")
		rotated.append("".join(new_row))

	# 逐行輸出旋轉結果
	sys.stdout.write("\n".join(rotated))


if __name__ == "__main__":
	main()
