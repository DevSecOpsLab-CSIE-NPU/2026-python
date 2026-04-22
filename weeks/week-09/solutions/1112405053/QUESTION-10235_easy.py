import sys
from collections import defaultdict


MOD = 1_000_000_007


def count_cycle_covers(board):
	"""
	board[r][c] = 1: 可用格
	board[r][c] = 0: 插座格（不能被蛇占）

	蛇會形成環，等價於：每個可用格的度數必須剛好是 2。
	"""
	n = len(board)
	m = len(board[0])

	# 狀態 (down_mask, left_edge)
	# down_mask 的第 c bit 表示：目前格往下有沒有連邊
	# left_edge 表示：目前格有沒有來自左邊的連邊
	dp = {(0, 0): 1}

	for r in range(n):
		for c in range(m):
			next_dp = defaultdict(int)

			open_cell = board[r][c] == 1
			can_go_right = c + 1 < m and board[r][c + 1] == 1
			can_go_down = r + 1 < n and board[r + 1][c] == 1

			for (down_mask, left_edge), ways in dp.items():
				up_edge = (down_mask >> c) & 1

				# 這格是插座：不能有任何邊接到它
				if not open_cell:
					if up_edge == 0 and left_edge == 0:
						cleared_mask = down_mask & ~(1 << c)
						next_dp[(cleared_mask, 0)] = (next_dp[(cleared_mask, 0)] + ways) % MOD
					continue

				# 可用格總度數要是 2: up + left + right + down = 2
				need = 2 - up_edge - left_edge
				if need < 0 or need > 2:
					continue

				max_right = 1 if can_go_right else 0
				max_down = 1 if can_go_down else 0

				for right_edge in range(max_right + 1):
					down_edge = need - right_edge
					if down_edge < 0 or down_edge > max_down:
						continue

					new_mask = down_mask
					if down_edge == 1:
						new_mask |= 1 << c
					else:
						new_mask &= ~(1 << c)

					next_dp[(new_mask, right_edge)] = (next_dp[(new_mask, right_edge)] + ways) % MOD

			dp = next_dp

	return dp.get((0, 0), 0)


def main():
	nums = list(map(int, sys.stdin.buffer.read().split()))
	if not nums:
		return

	t = nums[0]
	idx = 1
	output = []

	for case_id in range(1, t + 1):
		n = nums[idx]
		m = nums[idx + 1]
		idx += 2

		board = []
		for _ in range(n):
			board.append(nums[idx:idx + m])
			idx += m

		ans = count_cycle_covers(board)
		output.append(f"Case {case_id}: {ans}")

	sys.stdout.write("\n".join(output))


if __name__ == "__main__":
	main()
