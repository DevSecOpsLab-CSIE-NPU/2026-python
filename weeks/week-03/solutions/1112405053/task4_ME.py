import sys


def count_inversions(train: list[int]) -> int:
	swaps = 0
	n = len(train)
	for i in range(n):
		for j in range(i + 1, n):
			if train[i] > train[j]:
				swaps += 1
	return swaps


def main() -> None:
	data = list(map(int, sys.stdin.buffer.read().split()))
	if not data:
		return

	test_cases = data[0]
	idx = 1
	output = []

	for _ in range(test_cases):
		length = data[idx]
		idx += 1

		train = data[idx:idx + length]
		idx += length

		swaps = count_inversions(train)
		output.append(f"Optimal train swapping takes {swaps} swaps.")

	sys.stdout.write("\n".join(output))


if __name__ == "__main__":
	main()
