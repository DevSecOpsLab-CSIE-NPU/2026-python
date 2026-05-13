
import sys


def main():
	data = sys.stdin.read().strip().split()
	if not data:
		return
	it = iter(map(int, data))
	out_lines = []
	try:
		while True:
			n = next(it)
			pts = []
			for _ in range(n):
				x = next(it)
				y = next(it)
				pts.append((x, y))
			pts.sort()
			for x, y in pts:
				out_lines.append(f"{x} {y}")
	except StopIteration:
		pass

	sys.stdout.write("\n".join(out_lines))


if __name__ == '__main__':
	main()

