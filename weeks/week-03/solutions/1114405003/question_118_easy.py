"""UVA 118 - Robot motion with scent, easy version with Chinese comments."""

from __future__ import annotations

import sys


def solve(input_text: str) -> str:
    # 方向依序為北、東、南、西，方便左右轉換
    directions = ["N", "E", "S", "W"]
    moves = {
        "N": (0, 1),
        "E": (1, 0),
        "S": (0, -1),
        "W": (-1, 0),
    }

    lines = [line.strip() for line in input_text.splitlines() if line.strip()]
    if not lines:
        return ""

    max_x, max_y = map(int, lines[0].split())
    scent: set[tuple[int, int]] = set()
    outputs: list[str] = []

    index = 1
    while index < len(lines):
        x_str, y_str, direction = lines[index].split()
        x = int(x_str)
        y = int(y_str)
        commands = lines[index + 1]
        index += 2

        lost = False
        for command in commands:
            if command == "L":
                direction = directions[(directions.index(direction) - 1) % 4]
            elif command == "R":
                direction = directions[(directions.index(direction) + 1) % 4]
            elif command == "F":
                dx, dy = moves[direction]
                next_x = x + dx
                next_y = y + dy
                if not (0 <= next_x <= max_x and 0 <= next_y <= max_y):
                    if (x, y) in scent:
                        continue
                    scent.add((x, y))
                    lost = True
                    break
                x = next_x
                y = next_y

        line = f"{x} {y} {direction}"
        if lost:
            line += " LOST"
        outputs.append(line)

    return "\n".join(outputs)


def main() -> None:
    data = sys.stdin.read()
    result = solve(data)
    if result:
        sys.stdout.write(result)


if __name__ == "__main__":
    main()