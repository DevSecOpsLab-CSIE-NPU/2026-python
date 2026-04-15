import sys


def trans(n: int) -> str:
	s = oct(n)[2:]
	return s.replace("4", "5")


for line in sys.stdin:
	line = line.strip()
	if line:
		print(trans(int(line)))
