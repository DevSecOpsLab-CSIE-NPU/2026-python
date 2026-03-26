import sys


def main() -> None:
	lines = [line.strip() for line in sys.stdin if line.strip()]
	if not lines:
		return

	max_x, max_y = map(int, lines[0].split())

	left_turn = {"N": "W", "W": "S", "S": "E", "E": "N"}
	right_turn = {"N": "E", "E": "S", "S": "W", "W": "N"}
	move = {
		"N": (0, 1),
		"E": (1, 0),
		"S": (0, -1),
		"W": (-1, 0),
	}

	scented = set()
	output = []

	index = 1
	while index + 1 < len(lines):
		x, y, direction = lines[index].split()
		x = int(x)
		y = int(y)
		commands = lines[index + 1]
		index += 2

		lost = False

		for command in commands:
			if command == "L":
				direction = left_turn[direction]
			elif command == "R":
				direction = right_turn[direction]
			else:  
				dx, dy = move[direction]
				next_x = x + dx
				next_y = y + dy

				if 0 <= next_x <= max_x and 0 <= next_y <= max_y:
					x, y = next_x, next_y
				else:
					if (x, y) in scented:
						continue
					scented.add((x, y))
					lost = True
					break

		if lost:
			output.append(f"{x} {y} {direction} LOST")
		else:
			output.append(f"{x} {y} {direction}")

	sys.stdout.write("\n".join(output))


if __name__ == "__main__":
	main()
