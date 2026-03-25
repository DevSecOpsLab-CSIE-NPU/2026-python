import sys


def main() -> None:
	s = sys.stdin.read()
	if not s:
		return

	ch = s[0]

	if "A" <= ch <= "Z":
		sys.stdout.write("U")
	elif "a" <= ch <= "z":
		sys.stdout.write("L")
	else:
		sys.stdout.write("O")


if __name__ == "__main__":
	main()