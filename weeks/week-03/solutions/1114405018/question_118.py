"""UVA 118 - Mutant Flatworld Explorers

題意摘要：
- 在 0,0 到 upper_x,upper_y 的矩形世界中，依序模擬多台機器人。
- 指令：L(左轉)、R(右轉)、F(前進一格)。
- 若前進會掉出邊界，該機器人標記為 LOST，並在「掉落前位置」留下 scent。
- 後續機器人若位於同一格且同方向前進也會掉落時，要忽略該 F 指令。
"""

from __future__ import annotations

import sys


# 方向依序排成環，方便用索引做左轉/右轉
DIRECTIONS = ["N", "E", "S", "W"]

# 每個方向對應的座標增量 (dx, dy)
MOVE = {
    "N": (0, 1),
    "E": (1, 0),
    "S": (0, -1),
    "W": (-1, 0),
}


def turn_left(direction: str) -> str:
    """將方向左轉 90 度。"""
    idx = DIRECTIONS.index(direction)
    return DIRECTIONS[(idx - 1) % 4]


def turn_right(direction: str) -> str:
    """將方向右轉 90 度。"""
    idx = DIRECTIONS.index(direction)
    return DIRECTIONS[(idx + 1) % 4]


def solve(data: str) -> str:
    """解析輸入並回傳所有機器人的最終狀態。"""
    # 去除空白行，避免題目測資夾雜空行時影響解析
    lines = [line.strip() for line in data.splitlines() if line.strip()]
    if not lines:
        return ""

    upper_x, upper_y = map(int, lines[0].split())

    # scent 記錄曾讓機器人掉落前的位置
    scents: set[tuple[int, int]] = set()
    outputs: list[str] = []

    i = 1
    while i + 1 < len(lines):
        x_str, y_str, direction = lines[i].split()
        x, y = int(x_str), int(y_str)
        instructions = lines[i + 1]

        lost = False

        for cmd in instructions:
            if cmd == "L":
                direction = turn_left(direction)
                continue

            if cmd == "R":
                direction = turn_right(direction)
                continue

            # cmd == 'F'：嘗試往前走一格
            dx, dy = MOVE[direction]
            nx, ny = x + dx, y + dy

            # 若仍在邊界內，直接移動
            if 0 <= nx <= upper_x and 0 <= ny <= upper_y:
                x, y = nx, ny
                continue

            # 若會掉落，先檢查當前格是否已有 scent
            # 有 scent 表示此危險動作曾發生過，需忽略此次 F
            if (x, y) in scents:
                continue

            # 首次在這格掉落：留下 scent，機器人 LOST，停止處理後續指令
            scents.add((x, y))
            lost = True
            break

        if lost:
            outputs.append(f"{x} {y} {direction} LOST")
        else:
            outputs.append(f"{x} {y} {direction}")

        i += 2

    return "\n".join(outputs)


def main() -> None:
    """程式進入點：讀 stdin，寫 stdout。"""
    result = solve(sys.stdin.read())
    if result:
        sys.stdout.write(result)


if __name__ == "__main__":
    main()
