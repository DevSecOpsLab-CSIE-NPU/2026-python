import sys


def main() -> None:
	data = list(map(int, sys.stdin.buffer.read().split()))
	if not data:
		return

	n, m = data[0], data[1]
	values = data[2:]

	matrix = [values[i * m:(i + 1) * m] for i in range(n)]

	out = []
	for col in range(m):
		out.append(" ".join(str(matrix[row][col]) for row in range(n)))

	sys.stdout.write("\n".join(out))


if __name__ == "__main__":
	main()
