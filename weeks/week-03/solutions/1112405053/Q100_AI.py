import sys


# 記錄已計算過的 cycle length，避免重複計算
memo = {1: 1}


def cycle_length(number: int) -> int:
	# 若已在快取中，直接回傳
	if number in memo:
		return memo[number]

	# 暫存從 number 走到已知結果前的路徑
	sequence = []
	current = number

	# 持續做 3n+1 規則，直到碰到已知 cycle length 的數
	while current not in memo:
		sequence.append(current)
		if current % 2 == 0:
			current //= 2
		else:
			current = 3 * current + 1

	# 由已知節點往回填入快取
	length = memo[current]
	for value in reversed(sequence):
		length += 1
		memo[value] = length

	return memo[number]


# 逐行讀取多筆測資，每行格式為 i j
for line in sys.stdin:
	line = line.strip()
	if not line:
		continue

	left, right = map(int, line.split())
	# 題目要求保留原輸入順序輸出，但計算時需用小到大區間
	start = min(left, right)
	end = max(left, right)

	answer = 0
	# 找出區間 [start, end] 中最大的 cycle length
	for value in range(start, end + 1):
		answer = max(answer, cycle_length(value))

	# 輸出格式：i j max_cycle_length
	print(left, right, answer)
