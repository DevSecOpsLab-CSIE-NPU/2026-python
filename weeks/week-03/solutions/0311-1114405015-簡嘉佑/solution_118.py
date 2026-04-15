"""
UVA 118 - Mutant Flatworld Explorers（正式版）

題意重點：
  - 世界範圍是 (0,0) 到 (max_x,max_y)。
  - 機器人依序執行指令：
      L：左轉 90 度
      R：右轉 90 度
      F：朝目前方向前進一格
  - 若某台機器人從某格往某方向前進會掉出邊界：
      1) 這台機器人 LOST
      2) 在掉落前的最後位置留下 scent
      3) 後續機器人若位於同一格、同一方向再次嘗試出界，該次 F 會被忽略

輸出：
  - 正常結束：x y d
  - 掉落：x y d LOST
"""

from __future__ import annotations

import sys

# 方向依順時針排列，便於做左右旋轉。
DIRS = ["N", "E", "S", "W"]

# 每個方向對應的座標位移。
MOVE = {
    "N": (0, 1),
    "E": (1, 0),
    "S": (0, -1),
    "W": (-1, 0),
}


def turn_left(d: str) -> str:
    """方向左轉 90 度。"""
    i = DIRS.index(d)
    return DIRS[(i - 1) % 4]


def turn_right(d: str) -> str:
    """方向右轉 90 度。"""
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
    """
    模擬單一機器人執行指令。

    :param max_x: 世界右上角 x
    :param max_y: 世界右上角 y
    :param x: 起始 x
    :param y: 起始 y
    :param d: 起始方向（N/E/S/W）
    :param commands: 指令字串（L/R/F）
    :param scents: 標記集合，元素為 (x, y, d)
                   代表在該點朝 d 前進會掉落，需忽略該次 F。
    :return: (final_x, final_y, final_direction, lost)
    """
    lost = False

    for c in commands:
        if c == "L":
            d = turn_left(d)
        elif c == "R":
            d = turn_right(d)
        elif c == "F":
            dx, dy = MOVE[d]
            nx, ny = x + dx, y + dy

            # 嘗試前進後若超出邊界，進入掉落判定流程。
            if nx < 0 or nx > max_x or ny < 0 or ny > max_y:
                # 若此點此方向已有標記，表示前人已提醒，忽略本次 F。
                if (x, y, d) in scents:
                    continue

                # 第一次從此點此方向出界：留下標記並 LOST。
                scents.add((x, y, d))
                lost = True
                break

            # 未出界，正常更新位置。
            x, y = nx, ny

    return x, y, d, lost


def format_robot_result(x: int, y: int, d: str, lost: bool) -> str:
    """把單一機器人結果格式化成題目輸出字串。"""
    if lost:
        return f"{x} {y} {d} LOST"
    return f"{x} {y} {d}"


def main() -> None:
    """讀取輸入並依序輸出每台機器人的最後狀態。"""
    first_line = sys.stdin.readline().strip()
    if not first_line:
        return

    max_x, max_y = map(int, first_line.split())
    scents: set[tuple[int, int, str]] = set()

    while True:
        robot_line = sys.stdin.readline()
        if not robot_line:
            break

        robot_line = robot_line.strip()
        if not robot_line:
            continue

        x_str, y_str, d = robot_line.split()
        x, y = int(x_str), int(y_str)

        cmd_line = sys.stdin.readline()
        if not cmd_line:
            break
        commands = cmd_line.strip()

        rx, ry, rd, lost = simulate_robot(max_x, max_y, x, y, d, commands, scents)
        print(format_robot_result(rx, ry, rd, lost))


if __name__ == "__main__":
    main()
