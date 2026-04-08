import sys


def bit_count(x: int) -> int:
	return x.bit_count()


def main() -> None:
	data = sys.stdin.buffer.read().split()
	if not data:
		return

	n = int(data[0])
	m = int(data[1])
	rows = [line.decode() for line in data[2 : 2 + n]]

	# row_mask[i] 的 bit=1 表示該格是平原(P)可放炮兵。
	row_mask = [0] * n
	for i, row in enumerate(rows):
		mask = 0
		for j, ch in enumerate(row):
			if ch == "P":
				mask |= 1 << j
		row_mask[i] = mask

	# 預先列舉所有單列合法狀態：同列左右距離 1 或 2 都不能同時有炮兵。
	valid_states = []
	for s in range(1 << m):
		if (s & (s << 1)) == 0 and (s & (s << 2)) == 0:
			valid_states.append(s)

	state_count = len(valid_states)
	cnt = [bit_count(s) for s in valid_states]

	# 按列過濾地形可放的狀態。
	row_valid_idx = [[] for _ in range(n)]
	for i in range(n):
		allowed = row_mask[i]
		for idx, s in enumerate(valid_states):
			if (s & ~allowed) == 0:
				row_valid_idx[i].append(idx)

	NEG = -10**9

	# dp_prev[pre][prepre] 表示處理到前一列時，前一列狀態為 pre、前二列為 prepre 的最大值。
	dp_prev = [[NEG] * state_count for _ in range(state_count)]
	dp_prev[0][0] = 0

	for i in range(n):
		dp_cur = [[NEG] * state_count for _ in range(state_count)]
		for cur_idx in row_valid_idx[i]:
			cur_state = valid_states[cur_idx]
			cur_add = cnt[cur_idx]
			for pre_idx in range(state_count):
				pre_state = valid_states[pre_idx]
				# 與前一列不能同欄（上下距離 1）。
				if cur_state & pre_state:
					continue

				best = NEG
				for prepre_idx in range(state_count):
					base = dp_prev[pre_idx][prepre_idx]
					if base == NEG:
						continue
					prepre_state = valid_states[prepre_idx]
					# 與前二列不能同欄（上下距離 2）。
					if cur_state & prepre_state:
						continue
					if base > best:
						best = base

				if best != NEG:
					dp_cur[cur_idx][pre_idx] = best + cur_add

		dp_prev = dp_cur

	ans = 0
	for r in dp_prev:
		v = max(r)
		if v > ans:
			ans = v

	sys.stdout.write(str(ans))


if __name__ == "__main__":
	main()
