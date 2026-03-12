"""
UVA 118 - Mutant Flatworld Explorers（正式版）

題意摘要（繁中）：
1. 世界座標範圍是 (0,0) 到 (max_x,max_y)。
2. 每個機器人有初始座標與朝向（N/E/S/W），再接收一串指令（L/R/F）。
3. 若 F 會讓機器人掉出邊界：
   - 若目前格子有 scent（標記），則忽略這次 F。
   - 否則機器人 LOST，並在「掉落前最後座標」留下 scent。
4. 每個機器人依序執行，前一個機器人留下的 scent 會影響後面機器人。
"""

from __future__ import annotations

from typing import List, Set, Tuple

# 使用順時針順序，方便做左轉/右轉
DIRS = ["N", "E", "S", "W"]

# 每個方向前進一格時，座標變化量
MOVE = {
    "N": (0, 1),
    "E": (1, 0),
    "S": (0, -1),
    "W": (-1, 0),
}


def turn_left(direction: str) -> str:
    """左轉 90 度。"""
    idx = DIRS.index(direction)
    return DIRS[(idx - 1) % 4]


def turn_right(direction: str) -> str:
    """右轉 90 度。"""
    idx = DIRS.index(direction)
    return DIRS[(idx + 1) % 4]


def is_outside(x: int, y: int, max_x: int, max_y: int) -> bool:
    """判斷座標是否超出世界邊界。"""
    return x < 0 or x > max_x or y < 0 or y > max_y


def simulate_robot(
    start_x: int,
    start_y: int,
    start_dir: str,
    commands: str,
    max_x: int,
    max_y: int,
    scents: Set[Tuple[int, int]],
) -> Tuple[int, int, str, bool]:
    """
    模擬單一機器人的完整指令執行。

    參數：
    - start_x, start_y, start_dir: 初始狀態
    - commands: 指令字串（L/R/F）
    - max_x, max_y: 世界右上角
    - scents: 已存在的標記集合（共用狀態）

    回傳：
    - (final_x, final_y, final_dir, lost)
    """
    x, y, direction = start_x, start_y, start_dir

    for cmd in commands:
        if cmd == "L":
            direction = turn_left(direction)
        elif cmd == "R":
            direction = turn_right(direction)
        elif cmd == "F":
            dx, dy = MOVE[direction]
            nx, ny = x + dx, y + dy

            # 若前進後會出界，依照 scent 規則判斷
            if is_outside(nx, ny, max_x, max_y):
                if (x, y) in scents:
                    # 這格已有標記，忽略這次會掉落的前進指令
                    continue
                # 第一次從這格掉出去：留下標記並 LOST
                scents.add((x, y))
                return x, y, direction, True

            # 沒出界就正常前進
            x, y = nx, ny

    return x, y, direction, False


def solve_text(text: str) -> str:
    """
    解析完整輸入並回傳完整輸出（多行）。

    輸入格式：
    - 第一行：max_x max_y
    - 之後每兩行一組：
      - 行A：x y dir
      - 行B：commands
    """
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines:
        return ""

    # 讀取世界邊界
    max_x_str, max_y_str = lines[0].split()
    max_x, max_y = int(max_x_str), int(max_y_str)

    scents: Set[Tuple[int, int]] = set()
    out_lines: List[str] = []

    i = 1
    while i + 1 < len(lines):
        # 行A：機器人初始狀態
        x_str, y_str, d = lines[i].split()
        x, y = int(x_str), int(y_str)

        # 行B：機器人指令
        commands = lines[i + 1]

        fx, fy, fd, lost = simulate_robot(
            x, y, d, commands, max_x, max_y, scents
        )

        if lost:
            out_lines.append(f"{fx} {fy} {fd} LOST")
        else:
            out_lines.append(f"{fx} {fy} {fd}")

        i += 2

    return "\n".join(out_lines)


if __name__ == "__main__":
    import sys

    data = sys.stdin.read()
    if data.strip():
        print(solve_text(data))
