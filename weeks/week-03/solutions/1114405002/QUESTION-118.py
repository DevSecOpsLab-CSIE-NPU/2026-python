import sys


TURN_LEFT = {"N": "W", "W": "S", "S": "E", "E": "N"}
TURN_RIGHT = {"N": "E", "E": "S", "S": "W", "W": "N"}
MOVE = {"N": (0, 1), "S": (0, -1), "E": (1, 0), "W": (-1, 0)}


def main() -> None:
    lines = [line.strip() for line in sys.stdin if line.strip()]
    if not lines:
        return

    width, height = map(int, lines[0].split())
    scents = set()
    output = []
    index = 1

    while index < len(lines):
        x, y, direction = lines[index].split()
        x = int(x)
        y = int(y)
        instructions = lines[index + 1]
        index += 2

        lost = False

        for command in instructions:
            if command == "L":
                direction = TURN_LEFT[direction]
            elif command == "R":
                direction = TURN_RIGHT[direction]
            elif command == "F":
                dx, dy = MOVE[direction]
                next_x = x + dx
                next_y = y + dy

                if not (0 <= next_x <= width and 0 <= next_y <= height):
                    if (x, y, direction) in scents:
                        continue
                    scents.add((x, y, direction))
                    lost = True
                    break

                x = next_x
                y = next_y

        result = f"{x} {y} {direction}"
        if lost:
            result += " LOST"
        output.append(result)

    sys.stdout.write("\n".join(output) + ("\n" if output else ""))


if __name__ == "__main__":
    main()