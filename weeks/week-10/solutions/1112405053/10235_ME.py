
import sys

MOD = 1000000007


def count_cycle_covers(grid, N, M):
	# grid: list of lists, 1 = available, 0 = socket (forbidden)
	# DP state: mask (M bits) for down-edges coming into next row, left bit (0/1) for right-edge carry
	from collections import defaultdict
	dp = {(0, 0): 1}
	for i in range(N):
		for j in range(M):
			ndp = defaultdict(int)
			for (mask, left), cnt in dp.items():
				u = (mask >> j) & 1
				l = left
				avail = grid[i][j] == 1
				# determine availability of right and down neighbors
				right_avail = (j + 1 < M) and (grid[i][j + 1] == 1)
				down_avail = (i + 1 < N) and (grid[i + 1][j] == 1)
				if not avail:
					# must have degree 0 here
					if l == 0 and u == 0:
						new_mask = mask & ~(1 << j)
						ndp[(new_mask, 0)] = (ndp[(new_mask, 0)] + cnt) % MOD
					continue
				need = 2 - l - u
				if need < 0 or need > 2:
					continue
				# iterate possible (r,d) that sum to need
				if need == 0:
					r = 0; d = 0
					new_mask = (mask & ~(1 << j))
					ndp[(new_mask, 0)] = (ndp[(new_mask, 0)] + cnt) % MOD
				elif need == 2:
					# require both right and down
					if right_avail and down_avail:
						r = 1; d = 1
						new_mask = (mask & ~(1 << j)) | (1 << j)
						# new left will be r (1)
						ndp[(new_mask, 1)] = (ndp[(new_mask, 1)] + cnt) % MOD
				else:  # need == 1
					# option r=1,d=0
					if right_avail:
						r = 1; d = 0
						new_mask = (mask & ~(1 << j))
						ndp[(new_mask, 1)] = (ndp[(new_mask, 1)] + cnt) % MOD
					# option r=0,d=1
					if down_avail:
						r = 0; d = 1
						new_mask = (mask & ~(1 << j)) | (1 << j)
						ndp[(new_mask, 0)] = (ndp[(new_mask, 0)] + cnt) % MOD
			dp = ndp
		# end of row: left must be 0 for next row start; but states with left=1 are invalid because no cell to the left
		# however our transition naturally only allows left=0 at row end because right_avail false for last column
	# after all cells, accept only mask=0 and left=0
	return dp.get((0, 0), 0)


def main():
	data = sys.stdin.read().strip().split()
	if not data:
		return
	it = iter(data)
	T = int(next(it))
	out_lines = []
	for tc in range(1, T + 1):
		N = int(next(it)); M = int(next(it))
		grid = [[0]*M for _ in range(N)]
		for i in range(N):
			for j in range(M):
				grid[i][j] = int(next(it))
		# grid uses 1 for available, 0 for socket
		ans = count_cycle_covers(grid, N, M)
		out_lines.append(f"Case {tc}: {ans}")
	sys.stdout.write("\n".join(out_lines))


if __name__ == '__main__':
	main()
