"""UVA 118 - Mutant Flatworld Explorers."""

import sys

DIRECTIONS = "NESW"
MOVE = {
    "N": (0, 1),
    "E": (1, 0),
    "S": (0, -1),
    "W": (-1, 0),
}


def turn_left(direction: str) -> str:
    idx = DIRECTIONS.index(direction)
    return DIRECTIONS[(idx - 1) % 4]


def turn_right(direction: str) -> str:
    idx = DIRECTIONS.index(direction)
    return DIRECTIONS[(idx + 1) % 4]


def main() -> None:
    lines = [line.strip() for line in sys.stdin if line.strip() != ""]
    if not lines:
        return

    max_x, max_y = map(int, lines[0].split())
    scents = set()

    idx = 1
    while idx + 1 < len(lines):
        x_str, y_str, direction = lines[idx].split()
        x, y = int(x_str), int(y_str)
        instructions = lines[idx + 1]
        idx += 2

        lost = False
        for command in instructions:
            if command == "L":
                direction = turn_left(direction)
            elif command == "R":
                direction = turn_right(direction)
            elif command == "F":
                dx, dy = MOVE[direction]
                next_x = x + dx
                next_y = y + dy

                if 0 <= next_x <= max_x and 0 <= next_y <= max_y:
                    x, y = next_x, next_y
                    continue

                scent_key = (x, y, direction)
                if scent_key in scents:
                    continue

                scents.add(scent_key)
                lost = True
                break

        if lost:
            print(f"{x} {y} {direction} LOST")
        else:
            print(f"{x} {y} {direction}")


if __name__ == "__main__":
    main()
