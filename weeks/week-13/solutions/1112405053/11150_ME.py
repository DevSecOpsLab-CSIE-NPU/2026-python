import sys


def compress_positions(length, stones):
	positions = [0] + sorted(stones) + [length]
	compressed = [0]
	shift = 0
	prev = 0

	for pos in positions[1:]:
		gap = pos - prev
		if gap > 90:
			shift += gap - 90
		compressed.append(pos - shift)
		prev = pos

	return compressed


def solve_case(length, s, t, stones):
	positions = compress_positions(length, stones)
	compressed_length = positions[-1]
	stone_set = set(positions[1:-1])

	limit = compressed_length + t
	inf = 10**9
	dp = [inf] * (limit + 1)
	dp[0] = 0

	for i in range(1, limit + 1):
		best = inf
		left = max(0, i - t)
		right = i - s
		if right >= left:
			for j in range(left, right + 1):
				if dp[j] < best:
					best = dp[j]
		if best < inf:
			dp[i] = best + (1 if i in stone_set else 0)

	return min(dp[compressed_length:limit + 1])


def main():
	data = list(map(int, sys.stdin.read().split()))
	if not data:
		return

	out = []
	idx = 0
	n = len(data)
	while idx < n:
		length = data[idx]
		idx += 1
		if idx + 2 >= n:
			break
		s = data[idx]
		t = data[idx + 1]
		m = data[idx + 2]
		idx += 3
		stones = data[idx:idx + m]
		idx += m
		out.append(str(solve_case(length, s, t, stones)))

	sys.stdout.write("\n".join(out))


if __name__ == '__main__':
	main()

