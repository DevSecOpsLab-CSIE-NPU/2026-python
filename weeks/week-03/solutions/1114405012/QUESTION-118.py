#!/usr/bin/env python3
"""UVA 118 - Mutant Flatworld Explorers.

模擬機器人在矩形地圖上的移動，處理 LOST 與 scent 規則。
"""

from __future__ import annotations

import sys


DIRECTIONS = "NESW"
MOVE = {
    "N": (0, 1),
    "E": (1, 0),
    "S": (0, -1),
    "W": (-1, 0),
}


def turn_left(direction: str) -> str:
    """將方向向左轉 90 度。"""
    index = DIRECTIONS.index(direction)
    return DIRECTIONS[(index - 1) % 4]


def turn_right(direction: str) -> str:
    """將方向向右轉 90 度。"""
    index = DIRECTIONS.index(direction)
    return DIRECTIONS[(index + 1) % 4]


def simulate_robot(
    x: int,
    y: int,
    direction: str,
    instructions: str,
    max_x: int,
    max_y: int,
    scents: set[tuple[int, int]],
) -> tuple[int, int, str, bool]:
    """回傳機器人執行完後的狀態與是否 LOST。"""
    for command in instructions:
        if command == "L":
            direction = turn_left(direction)
            continue

        if command == "R":
            direction = turn_right(direction)
            continue

        if command == "F":
            dx, dy = MOVE[direction]
            nx = x + dx
            ny = y + dy

            if 0 <= nx <= max_x and 0 <= ny <= max_y:
                x, y = nx, ny
                continue

            # 若前進會掉出邊界，且當前格有 scent，則忽略該指令
            if (x, y) in scents:
                continue

            # 沒有 scent 則機器人掉落，並在掉落前座標留下 scent
            scents.add((x, y))
            return x, y, direction, True

    return x, y, direction, False


def main() -> None:
    lines = [line.rstrip("\n") for line in sys.stdin]
    if not lines:
        return

    idx = 0
    while idx < len(lines) and not lines[idx].strip():
        idx += 1
    if idx >= len(lines):
        return

    max_x, max_y = map(int, lines[idx].split())
    idx += 1

    scents: set[tuple[int, int]] = set()
    outputs: list[str] = []

    while idx < len(lines):
        if not lines[idx].strip():
            idx += 1
            continue

        x_str, y_str, direction = lines[idx].split()
        x = int(x_str)
        y = int(y_str)
        idx += 1

        if idx >= len(lines):
            break

        instructions = lines[idx].strip()
        idx += 1

        final_x, final_y, final_direction, lost = simulate_robot(
            x,
            y,
            direction,
            instructions,
            max_x,
            max_y,
            scents,
        )

        if lost:
            outputs.append(f"{final_x} {final_y} {final_direction} LOST")
        else:
            outputs.append(f"{final_x} {final_y} {final_direction}")

    sys.stdout.write("\n".join(outputs))


if __name__ == "__main__":
    main()
