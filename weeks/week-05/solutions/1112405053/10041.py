import sys


for line in sys.stdin:
	n = int(line.strip())
	print(bin(n)[2:])
