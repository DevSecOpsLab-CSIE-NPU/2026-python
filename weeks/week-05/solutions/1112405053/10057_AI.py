import sys


def main() -> None:
	# 讀入整段文字，取第一個字元做判斷
	s = sys.stdin.read()
	if not s:
		return

	ch = s[0]

	# 依 ASCII 區間判斷：大寫、小寫、其他
	if "A" <= ch <= "Z":
		sys.stdout.write("U")
	elif "a" <= ch <= "z":
		sys.stdout.write("L")
	else:
		sys.stdout.write("O")


if __name__ == "__main__":
	main()
