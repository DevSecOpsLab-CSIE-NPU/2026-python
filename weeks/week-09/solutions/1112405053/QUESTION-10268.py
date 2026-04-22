import sys


MAX_K = 100
MAX_TRIALS = 63


def build_dp():
	# dp[t][k] = 在最壞情況下，t 次嘗試、k 顆水球最多可判定幾層樓
	dp = [[0] * (MAX_K + 1) for _ in range(MAX_TRIALS + 1)]

	for t in range(1, MAX_TRIALS + 1):
		for k in range(1, MAX_K + 1):
			dp[t][k] = dp[t - 1][k - 1] + dp[t - 1][k] + 1

	return dp


def solve():
	dp = build_dp()
	out = []

	for line in sys.stdin:
		line = line.strip()
		if not line:
			continue

		k, n = map(int, line.split())
		if k == 0:
			break

		if k > MAX_K:
			k = MAX_K

		ans = None
		for t in range(1, MAX_TRIALS + 1):
			if dp[t][k] >= n:
				ans = t
				break

		if ans is None:
			out.append("More than 63 trials needed.")
		else:
			out.append(str(ans))

	sys.stdout.write("\n".join(out))


if __name__ == "__main__":
	solve()
