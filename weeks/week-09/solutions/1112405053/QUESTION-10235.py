import sys
from collections import defaultdict


MOD = 1_000_000_007


def count_ways(grid):
	n = len(grid)
	m = len(grid[0])

	# State: (mask, left)
	# mask bit j: whether edge from cell (current row, j) to the cell below is selected
	# left: whether edge from left neighbor to current cell is selected
	dp = {(0, 0): 1}

	for i in range(n):
		for j in range(m):
			ndp = defaultdict(int)
			cell_open = grid[i][j] == 1
			can_right = j + 1 < m and grid[i][j + 1] == 1
			can_down = i + 1 < n and grid[i + 1][j] == 1

			for (mask, left), ways in dp.items():
				up = (mask >> j) & 1

				if not cell_open:
					if up == 0 and left == 0:
						new_mask = mask & ~(1 << j)
						ndp[(new_mask, 0)] = (ndp[(new_mask, 0)] + ways) % MOD
					continue

				need = 2 - up - left
				if need < 0 or need > 2:
					continue

				max_r = 1 if can_right else 0
				max_d = 1 if can_down else 0

				# Choose r, d such that up + left + r + d = 2
				for r in range(max_r + 1):
					d = need - r
					if d < 0 or d > max_d:
						continue

					new_mask = mask
					if d == 1:
						new_mask |= 1 << j
					else:
						new_mask &= ~(1 << j)

					ndp[(new_mask, r)] = (ndp[(new_mask, r)] + ways) % MOD

			dp = ndp

	return dp.get((0, 0), 0)


def main():
	data = list(map(int, sys.stdin.buffer.read().split()))
	if not data:
		return

	t = data[0]
	p = 1
	out = []

	for case_id in range(1, t + 1):
		n = data[p]
		m = data[p + 1]
		p += 2

		grid = []
		for _ in range(n):
			row = data[p:p + m]
			p += m
			grid.append(row)

		ans = count_ways(grid)
		out.append(f"Case {case_id}: {ans}")

	sys.stdout.write("\n".join(out))


if __name__ == "__main__":
	main()
