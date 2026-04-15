import sys


for line in sys.stdin:
	if not line.strip():
		continue
	n, m = map(int, line.split())
	s = k = 0
	while s <= m:
		s += n + k
		k += 1
	print(k)
