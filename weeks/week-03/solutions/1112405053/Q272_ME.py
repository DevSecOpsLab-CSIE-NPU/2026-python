import sys


def main() -> None:
	text = sys.stdin.read()
	is_open = True
	output = []

	for char in text:
		if char == '"':
			if is_open:
				output.append("``")
			else:
				output.append("''")
			is_open = not is_open
		else:
			output.append(char)

	sys.stdout.write("".join(output))


if __name__ == "__main__":
	main()
