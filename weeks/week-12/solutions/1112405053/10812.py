import sys


def main():
	data = sys.stdin.read().strip().split()
	if not data:
		return
	it = iter(map(int, data))
	out_lines = []
	try:
		while True:
			R = next(it)
			C = next(it)
			grid = [[next(it) for _ in range(C)] for _ in range(R)]
			r1 = next(it)
			c1 = next(it)
			r2 = next(it)
			c2 = next(it)
			if r1 > r2:
				r1, r2 = r2, r1
			if c1 > c2:
				c1, c2 = c2, c1

			ps = [[0] * (C + 1) for _ in range(R + 1)]
			for i in range(R):
				row_sum = 0
				for j in range(C):
					row_sum += grid[i][j]
					ps[i + 1][j + 1] = ps[i][j + 1] + row_sum

			total = ps[r2 + 1][c2 + 1] - ps[r1][c2 + 1] - ps[r2 + 1][c1] + ps[r1][c1]
			out_lines.append(str(total))
	except StopIteration:
		pass

	sys.stdout.write("\n".join(out_lines))


if __name__ == '__main__':
	main()

