import sys


def main() -> None:
	is_open_quote = True
	output_parts = []

	for ch in sys.stdin.read():
		if ch == '"':
			if is_open_quote:
				output_parts.append("``")
			else:
				output_parts.append("''")
			is_open_quote = not is_open_quote
		else:
			output_parts.append(ch)

	sys.stdout.write("".join(output_parts))


if __name__ == "__main__":
	main()
