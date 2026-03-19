#!/usr/bin/env python3
"""UVA 118 手打版。

機器人移動模擬：L/R 轉向、F 前進、越界 LOST、掉落點留下 scent。
"""

import sys


def main() -> None:
    lines = [line.rstrip("\n") for line in sys.stdin]
    if not lines:
        return

    top_right = lines[0].split()
    max_x = int(top_right[0])
    max_y = int(top_right[1])

    # 方向順序：N -> E -> S -> W
    dirs = ["N", "E", "S", "W"]
    move = {
        "N": (0, 1),
        "E": (1, 0),
        "S": (0, -1),
        "W": (-1, 0),
    }

    scents: set[tuple[int, int]] = set()
    answer: list[str] = []

    idx = 1
    while idx < len(lines):
        if not lines[idx].strip():
            idx += 1
            continue

        x_str, y_str, face = lines[idx].split()
        x = int(x_str)
        y = int(y_str)
        idx += 1

        if idx >= len(lines):
            break

        commands = lines[idx].strip()
        idx += 1

        lost = False

        for command in commands:
            if command == "L":
                face_index = dirs.index(face)
                face = dirs[(face_index - 1) % 4]
            elif command == "R":
                face_index = dirs.index(face)
                face = dirs[(face_index + 1) % 4]
            else:
                dx, dy = move[face]
                nx = x + dx
                ny = y + dy

                # 正常在範圍內，直接前進
                if 0 <= nx <= max_x and 0 <= ny <= max_y:
                    x, y = nx, ny
                    continue

                # 如果這格有 scent，忽略這次會掉落的 F
                if (x, y) in scents:
                    continue

                # 第一次從此格掉落：記錄 scent 並 LOST
                scents.add((x, y))
                lost = True
                break

        if lost:
            answer.append(f"{x} {y} {face} LOST")
        else:
            answer.append(f"{x} {y} {face}")

    sys.stdout.write("\n".join(answer))


if __name__ == "__main__":
    main()
