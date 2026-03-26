import sys


def count_swaps(train: list[int]) -> int:
	swaps = 0
	length = len(train)

	for i in range(length):
		for j in range(i + 1, length):
			if train[i] > train[j]:
				swaps += 1

	return swaps


def main() -> None:
	tokens = sys.stdin.read().split()
	if not tokens:
		return

	index = 0
	test_cases = int(tokens[index])
	index += 1

	output = []

	for _ in range(test_cases):
		length = int(tokens[index])
		index += 1

		train = list(map(int, tokens[index:index + length]))
		index += length

		swaps = count_swaps(train)
		output.append(f"Optimal train swapping takes {swaps} swaps.")

	sys.stdout.write("\n".join(output))


if __name__ == "__main__":
	main()
