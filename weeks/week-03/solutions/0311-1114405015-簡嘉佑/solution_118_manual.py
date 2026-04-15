"""
UVA 118 - Mutant Flatworld Explorers (manual version)

Robots move on a rectangular world from (0,0) to (max_x,max_y).
Commands:
  L: turn left
  R: turn right
  F: move forward one step
If a robot would leave the world, it is LOST and leaves a scent at
its last valid position and facing direction.
Future robots ignore only that exact dangerous move.
"""

from __future__ import annotations

import sys

DIRS = ["N", "E", "S", "W"]
MOVE = {
    "N": (0, 1),
    "E": (1, 0),
    "S": (0, -1),
    "W": (-1, 0),
}


def turn_left(d: str) -> str:
    i = DIRS.index(d)
    return DIRS[(i - 1) % 4]


def turn_right(d: str) -> str:
    i = DIRS.index(d)
    return DIRS[(i + 1) % 4]


def simulate_robot(
    max_x: int,
    max_y: int,
    x: int,
    y: int,
    d: str,
    commands: str,
    scents: set[tuple[int, int, str]],
) -> tuple[int, int, str, bool]:
    lost = False

    for c in commands:
        if c == "L":
            d = turn_left(d)
        elif c == "R":
            d = turn_right(d)
        elif c == "F":
            dx, dy = MOVE[d]
            nx, ny = x + dx, y + dy

            if nx < 0 or nx > max_x or ny < 0 or ny > max_y:
                if (x, y, d) in scents:
                    continue
                scents.add((x, y, d))
                lost = True
                break

            x, y = nx, ny

    return x, y, d, lost


def format_robot_result(x: int, y: int, d: str, lost: bool) -> str:
    if lost:
        return f"{x} {y} {d} LOST"
    return f"{x} {y} {d}"


def main() -> None:
    first = sys.stdin.readline().strip()
    if not first:
        return

    max_x, max_y = map(int, first.split())
    scents: set[tuple[int, int, str]] = set()

    while True:
        line = sys.stdin.readline()
        if not line:
            break

        line = line.strip()
        if not line:
            continue

        x_str, y_str, d = line.split()
        x, y = int(x_str), int(y_str)

        cmd_line = sys.stdin.readline()
        if not cmd_line:
            break
        commands = cmd_line.strip()

        rx, ry, rd, lost = simulate_robot(max_x, max_y, x, y, d, commands, scents)
        print(format_robot_result(rx, ry, rd, lost))


if __name__ == "__main__":
    main()
