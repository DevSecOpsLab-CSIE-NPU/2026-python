import sys


memo = {1: 1}


def cycle_length(number: int) -> int:
	if number in memo:
		return memo[number]

	sequence = []
	current = number

	while current not in memo:
		sequence.append(current)
		if current % 2 == 0:
			current //= 2
		else:
			current = 3 * current + 1

	length = memo[current]
	for value in reversed(sequence):
		length += 1
		memo[value] = length

	return memo[number]


for line in sys.stdin:
	line = line.strip()
	if not line:
		continue

	left, right = map(int, line.split())
	start = min(left, right)
	end = max(left, right)

	answer = 0
	for value in range(start, end + 1):
		answer = max(answer, cycle_length(value))

	print(left, right, answer)
