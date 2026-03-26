import sys


def main() -> None:
	# 讀入所有非空白行（第一行是地圖邊界，後續每兩行是一台機器人）
	lines = [line.strip() for line in sys.stdin if line.strip()]
	if not lines:
		return

	# 世界右上角座標（左下角固定為 0,0）
	max_x, max_y = map(int, lines[0].split())

	# 方向旋轉對照表
	left_turn = {"N": "W", "W": "S", "S": "E", "E": "N"}
	right_turn = {"N": "E", "E": "S", "S": "W", "W": "N"}
	# 各方向前進一格的座標變化
	move = {
		"N": (0, 1),
		"E": (1, 0),
		"S": (0, -1),
		"W": (-1, 0),
	}

	# 記錄曾經導致機器人掉落的「最後安全座標」
	scented = set()
	output = []

	index = 1
	# 每台機器人由兩行組成：初始狀態 + 指令字串
	while index + 1 < len(lines):
		x, y, direction = lines[index].split()
		x = int(x)
		y = int(y)
		commands = lines[index + 1]
		index += 2

		lost = False

		# 依序執行指令
		for command in commands:
			if command == "L":
				direction = left_turn[direction]
			elif command == "R":
				direction = right_turn[direction]
			else:
				dx, dy = move[direction]
				next_x = x + dx
				next_y = y + dy

				# 若仍在邊界內，正常移動
				if 0 <= next_x <= max_x and 0 <= next_y <= max_y:
					x, y = next_x, next_y
				else:
					# 若此座標已有 scent，忽略這次會掉落的 F 指令
					if (x, y) in scented:
						continue
					# 否則留下 scent，該機器人掉落
					scented.add((x, y))
					lost = True
					break

		# 依題目格式輸出結果
		if lost:
			output.append(f"{x} {y} {direction} LOST")
		else:
			output.append(f"{x} {y} {direction}")

	sys.stdout.write("\n".join(output))


if __name__ == "__main__":
	main()
