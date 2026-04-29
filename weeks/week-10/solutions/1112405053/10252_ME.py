
import sys


def solve_all(data):
	it = iter(data)
	t = int(next(it))
	out_lines = []
	for _ in range(t):
		n = int(next(it))
		xs = [0]*n
		ys = [0]*n
		for i in range(n):
			xs[i] = int(next(it))
			ys[i] = int(next(it))
		xs.sort()
		ys.sort()
		if n % 2 == 1:
			xm = xs[n//2]
			ym = ys[n//2]
			sumx = sum(abs(x - xm) for x in xs)
			sumy = sum(abs(y - ym) for y in ys)
			cntx = 1
			cnty = 1
		else:
			xl = xs[n//2 - 1]
			xh = xs[n//2]
			yl = ys[n//2 - 1]
			yh = ys[n//2]
			sumx = sum(abs(x - xl) for x in xs)
			sumy = sum(abs(y - yl) for y in ys)
			cntx = xh - xl + 1
			cnty = yh - yl + 1
		out_lines.append(f"{sumx + sumy} {cntx * cnty}")
	return "\n".join(out_lines)


def main():
	data = sys.stdin.read().strip().split()
	if not data:
		return
	print(solve_all(data))


if __name__ == '__main__':
	main()
