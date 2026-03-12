from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Set, Tuple

Direction = str
ScentMark = Tuple[int, int, Direction]

DIRECTIONS = ("N", "E", "S", "W")
# 方向對應的位移向量（x, y）
MOVE_VECTOR = {
    "N": (0, 1),
    "E": (1, 0),
    "S": (0, -1),
    "W": (-1, 0),
}


@dataclass(frozen=True)
class RobotState:
    x: int
    y: int
    direction: Direction
    lost: bool = False


def turn_left(direction: Direction) -> Direction:
    # 以循環索引實作左轉，N -> W -> S -> E -> N
    idx = DIRECTIONS.index(direction)
    return DIRECTIONS[(idx - 1) % 4]


def turn_right(direction: Direction) -> Direction:
    # 以循環索引實作右轉，N -> E -> S -> W -> N
    idx = DIRECTIONS.index(direction)
    return DIRECTIONS[(idx + 1) % 4]


def _would_fall_off(x: int, y: int, width: int, height: int) -> bool:
    # 地圖範圍為 (0,0) 到 (width,height)，含邊界
    return x < 0 or x > width or y < 0 or y > height


def apply_command(
    state: RobotState,
    command: str,
    width: int,
    height: int,
    scent: Set[ScentMark],
) -> RobotState:
    # 一旦 LOST，該機器人後續指令一律忽略
    if state.lost:
        return state

    if command == "L":
        return RobotState(state.x, state.y, turn_left(state.direction), False)

    if command == "R":
        return RobotState(state.x, state.y, turn_right(state.direction), False)

    if command == "F":
        dx, dy = MOVE_VECTOR[state.direction]
        nx, ny = state.x + dx, state.y + dy
        if not _would_fall_off(nx, ny, width, height):
            return RobotState(nx, ny, state.direction, False)

        # scent 以 (x, y, dir) 記錄，方向不同視為不同危險點
        mark = (state.x, state.y, state.direction)
        if mark in scent:
            # 同位置同方向再次越界時，忽略這次前進
            return state

        # 首次在此位置方向越界：留下 scent 並標記 LOST
        scent.add(mark)
        return RobotState(state.x, state.y, state.direction, True)

    raise ValueError(f"Unsupported command: {command}")


def run_commands(
    start_state: RobotState,
    commands: Iterable[str],
    width: int,
    height: int,
    scent: Set[ScentMark] | None = None,
) -> tuple[RobotState, Set[ScentMark]]:
    if scent is None:
        scent = set()

    state = start_state
    for command in commands:
        state = apply_command(state, command, width, height, scent)
        if state.lost:
            # 規則：LOST 後停止執行剩餘指令
            break

    return state, scent


def format_state(state: RobotState) -> str:
    suffix = " LOST" if state.lost else ""
    return f"{state.x} {state.y} {state.direction}{suffix}"
