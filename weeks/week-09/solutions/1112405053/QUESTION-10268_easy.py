import sys


MAX_BALLOONS = 100
MAX_TRIALS = 63


def precompute_max_floors():
	"""
	dp[t][k] = 最壞情況下，用 t 次測試、k 顆水球
	最多可以確定幾層樓的臨界樓層。
	"""
	dp = [[0] * (MAX_BALLOONS + 1) for _ in range(MAX_TRIALS + 1)]

	for t in range(1, MAX_TRIALS + 1):
		for k in range(1, MAX_BALLOONS + 1):
			# 破掉：往下 dp[t-1][k-1] 層
			# 沒破：往上 dp[t-1][k] 層
			# 再加上當前測試這一層
			dp[t][k] = dp[t - 1][k - 1] + dp[t - 1][k] + 1

	return dp


def solve():
	dp = precompute_max_floors()
	answers = []

	for line in sys.stdin:
		line = line.strip()
		if not line:
			continue

		k, n = map(int, line.split())
		if k == 0 and n == 0:
			break

		# 題目保證 k <= 100，這裡保險處理
		if k > MAX_BALLOONS:
			k = MAX_BALLOONS

		result = None
		for trials in range(1, MAX_TRIALS + 1):
			if dp[trials][k] >= n:
				result = trials
				break

		if result is None:
			answers.append("More than 63 trials needed.")
		else:
			answers.append(str(result))

	sys.stdout.write("\n".join(answers))


if __name__ == "__main__":
	solve()
