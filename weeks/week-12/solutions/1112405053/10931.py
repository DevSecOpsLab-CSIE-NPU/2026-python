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
			W = next(it)
			weights = [next(it) for _ in range(n)]
			if W < 0:
				out_lines.append("0")
				continue
			dp = [0] * (W + 1)
			dp[0] = 1
			for w in weights:
				if w > W:
					continue
				for j in range(W, w - 1, -1):
					dp[j] += dp[j - w]
			out_lines.append(str(dp[W]))
	except StopIteration:
		pass

	sys.stdout.write("\n".join(out_lines))


if __name__ == '__main__':
	main()

