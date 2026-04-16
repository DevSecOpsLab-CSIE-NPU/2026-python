"""Robot Lost 核心邏輯模組。

此模組不依賴 pygame，方便單元測試與重用。
"""

from __future__ import annotations

from typing import NamedTuple

DIRECTIONS = ("N", "E", "S", "W")
MOVE_DELTA = {
    "N": (0, 1),
    "E": (1, 0),
    "S": (0, -1),
    "W": (-1, 0),
}


class RobotState(NamedTuple):
    """機器人狀態資料結構。"""

    x: int
    y: int
    direction: str
    lost: bool = False


def _validate_direction(direction: str) -> str:
    direction = direction.upper()
    if direction not in DIRECTIONS:
        raise ValueError(f"非法方向: {direction}")
    return direction


def turn_left(direction: str) -> str:
    """左轉 90 度。"""
    direction = _validate_direction(direction)
    idx = DIRECTIONS.index(direction)
    return DIRECTIONS[(idx - 1) % 4]


def turn_right(direction: str) -> str:
    """右轉 90 度。"""
    direction = _validate_direction(direction)
    idx = DIRECTIONS.index(direction)
    return DIRECTIONS[(idx + 1) % 4]


def step_forward(x: int, y: int, direction: str) -> tuple[int, int]:
    """依目前方向前進一格。"""
    direction = _validate_direction(direction)
    dx, dy = MOVE_DELTA[direction]
    return x + dx, y + dy


def is_inside(max_x: int, max_y: int, x: int, y: int) -> bool:
    """檢查座標是否在地圖邊界內（含邊界）。"""
    return 0 <= x <= max_x and 0 <= y <= max_y


def simulate(
    max_x: int,
    max_y: int,
    start_x: int,
    start_y: int,
    start_dir: str,
    instructions: str,
    scents: set[tuple[int, int, str]] | None = None,
) -> tuple[int, int, str, bool, set[tuple[int, int, str]]]:
    """執行一台機器人的指令序列。

    規則：
    - L/R：轉向
    - F：前進，若越界則 LOST，並在 (x, y, dir) 留下 scent
    - 若越界前位置已存在同向 scent，則忽略該危險 F
    - 一旦 LOST，後續指令不再執行
    - 非法指令拋出 ValueError
    """
    if scents is None:
        scents = set()

    x = start_x
    y = start_y
    direction = _validate_direction(start_dir)
    lost = False

    for cmd in instructions:
        cmd = cmd.upper()

        if lost:
            break

        if cmd == "L":
            direction = turn_left(direction)
            continue

        if cmd == "R":
            direction = turn_right(direction)
            continue

        if cmd == "F":
            nx, ny = step_forward(x, y, direction)
            if is_inside(max_x, max_y, nx, ny):
                x, y = nx, ny
                continue

            scent_key = (x, y, direction)
            if scent_key in scents:
                # 有歷史氣味代表此處此方向會掉落，忽略這步危險前進
                continue

            scents.add(scent_key)
            lost = True
            break

        raise ValueError(f"非法指令: {cmd}")

    return x, y, direction, lost, scents
