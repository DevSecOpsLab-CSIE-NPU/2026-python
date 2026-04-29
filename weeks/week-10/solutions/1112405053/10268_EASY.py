
import sys


def min_trials(k, n):
	if n <= 1:
		return 0
	for m in range(1, 64):
		s = 0
		c = 1
		for i in range(1, min(k, m) + 1):
			c = c * (m - i + 1) // i
			s += c
			if s >= n:
				return m
	return None


def main():
	parts = sys.stdin.read().split()
	it = iter(parts)
	for a, b in zip(it, it):
		k = int(a); n = int(b)
		if k == 0:
			break
		r = min_trials(k, n)
		if r is None:
			print("More than 63 trials needed.")
		else:
			print(r)


if __name__ == '__main__':
	main()
