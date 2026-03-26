import sys


def main() -> None:
	lines = sys.stdin.read().splitlines()
	if not lines:
		return

	max_length = max(len(line) for line in lines)
	rotated = []

	for column in range(max_length):
		new_row = []
		for row in range(len(lines) - 1, -1, -1):
			if column < len(lines[row]):
				new_row.append(lines[row][column])
			else:
				new_row.append(" ")
		rotated.append("".join(new_row))

	sys.stdout.write("\n".join(rotated))


if __name__ == "__main__":
	main()
