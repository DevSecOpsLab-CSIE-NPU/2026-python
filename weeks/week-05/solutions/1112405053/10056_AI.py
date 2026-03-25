import sys


def main() -> None:
	# 讀入所有整數：前兩個是 n, m，後面是矩陣元素
	data = list(map(int, sys.stdin.buffer.read().split()))
	if not data:
		return

	n, m = data[0], data[1]
	values = data[2:]

	# 還原成 n x m 原矩陣
	matrix = [values[i * m:(i + 1) * m] for i in range(n)]

	# 轉置輸出：第 col 欄會變成新矩陣的一列
	out = []
	for col in range(m):
		out.append(" ".join(str(matrix[row][col]) for row in range(n)))

	sys.stdout.write("\n".join(out))


if __name__ == "__main__":
	main()
