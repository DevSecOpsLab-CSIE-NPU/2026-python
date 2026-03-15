import sys


def count_inversions(arr: list[int]) -> int:
	swaps = 0
	n = len(arr)
	for i in range(n):
		for j in range(i + 1, n):
			if arr[i] > arr[j]:
				swaps += 1
	return swaps


def main() -> None:
	data = list(map(int, sys.stdin.buffer.read().split()))
	if not data:
		return

	t = data[0]
	index = 1
	out = []

	for _ in range(t):
		l = data[index]
		index += 1

		train = data[index:index + l]
		index += l

		s = count_inversions(train)
		out.append(f"Optimal train swapping takes {s} swaps.")

	sys.stdout.write("\n".join(out))


if __name__ == "__main__":
	main()
