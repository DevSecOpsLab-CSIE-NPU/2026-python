
import sys


def min_trials(k: int, n: int) -> int | None:
	if n <= 1:
		return 0
	for m in range(1, 64):
		s = 0
		term = 1
		for i in range(1, min(k, m) + 1):
			term = term * (m - i + 1) // i
			s += term
			if s >= n:
				return m
	return None


def main():
	data = sys.stdin.read().strip().split()
	if not data:
		return
	it = iter(data)
	out_lines = []
	for a, b in zip(it, it):
		k = int(a)
		n = int(b)
		if k == 0:
			break
		res = min_trials(k, n)
		if res is None:
			out_lines.append("More than 63 trials needed.")
		else:
			out_lines.append(str(res))
	sys.stdout.write("\n".join(out_lines))


if __name__ == '__main__':
	main()
