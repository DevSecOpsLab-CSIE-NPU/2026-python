"""
UVA 118 - 機器人平面探索模擬。
"""

from __future__ import annotations

import sys


DIRECTIONS = "NESW"
LEFT_TURN = {"N": "W", "W": "S", "S": "E", "E": "N"}
RIGHT_TURN = {"N": "E", "E": "S", "S": "W", "W": "N"}
STEP = {"N": (0, 1), "E": (1, 0), "S": (0, -1), "W": (-1, 0)}


def parse_robot_state(line: str) -> tuple[int, int, str]:
    """解析機器人狀態字串 'x y D'。"""
    x_str, y_str, direction = line.split()
    return int(x_str), int(y_str), direction


def is_out_of_grid(x: int, y: int, max_x: int, max_y: int) -> bool:
    """若座標超出 [0, max_x] x [0, max_y] 則回傳 True。"""
    return x < 0 or x > max_x or y < 0 or y > max_y


def next_position(x: int, y: int, direction: str) -> tuple[int, int]:
    """回傳機器人向前移動一格後的下一個座標。"""
    dx, dy = STEP[direction]
    return x + dx, y + dy


def simulate_robot(
    max_x: int,
    max_y: int,
    scents: set[tuple[int, int]],
    start_x: int,
    start_y: int,
    start_direction: str,
    commands: str,
) -> tuple[int, int, str, bool]:
    """
    模擬單一機器人的完整指令流程。

    回傳 (final_x, final_y, final_direction, lost_flag)。
    """
    x, y, direction = start_x, start_y, start_direction
    lost = False

    for command in commands:
        if command == "L":
            direction = LEFT_TURN[direction]
        elif command == "R":
            direction = RIGHT_TURN[direction]
        elif command == "F":
            nx, ny = next_position(x, y, direction)
            if is_out_of_grid(nx, ny, max_x, max_y):
                if (x, y) in scents:
                    # 這一步會掉出邊界，但此位置已有氣味，忽略此指令。
                    continue
                scents.add((x, y))
                lost = True
                break
            x, y = nx, ny

    return x, y, direction, lost


def solve(text: str) -> str:
    """處理輸入中的所有機器人資料並回傳輸出字串。"""
    lines = text.splitlines()
    if not lines:
        return ""

    index = 0
    while index < len(lines) and not lines[index].strip():
        index += 1
    if index >= len(lines):
        return ""

    max_x, max_y = map(int, lines[index].split())
    index += 1

    scents: set[tuple[int, int]] = set()
    outputs: list[str] = []

    while index < len(lines):
        while index < len(lines) and not lines[index].strip():
            index += 1
        if index >= len(lines):
            break

        state_line = lines[index].strip()
        index += 1

        if index < len(lines):
            commands = lines[index].strip()
            index += 1
        else:
            commands = ""

        x, y, direction = parse_robot_state(state_line)

        fx, fy, fd, lost = simulate_robot(
            max_x=max_x,
            max_y=max_y,
            scents=scents,
            start_x=x,
            start_y=y,
            start_direction=direction,
            commands=commands,
        )

        suffix = " LOST" if lost else ""
        outputs.append(f"{fx} {fy} {fd}{suffix}")

    return "\n".join(outputs)


def main() -> None:
    """主程式進入點。"""
    data = sys.stdin.read()
    result = solve(data)
    if result:
        sys.stdout.write(result + "\n")


if __name__ == "__main__":
    main()
