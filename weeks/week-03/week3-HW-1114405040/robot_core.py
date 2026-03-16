from __future__ import annotations

from dataclasses import dataclass


DIRECTIONS = ("N", "E", "S", "W")
LEFT_TURNS = {"N": "W", "W": "S", "S": "E", "E": "N"}
RIGHT_TURNS = {"N": "E", "E": "S", "S": "W", "W": "N"}
MOVES = {
    "N": (0, 1),
    "E": (1, 0),
    "S": (0, -1),
    "W": (-1, 0),
}
VALID_COMMANDS = {"L", "R", "F"}


@dataclass(slots=True)
class Robot:
    x: int
    y: int
    direction: str
    lost: bool = False

    def __post_init__(self) -> None:
        if self.direction not in DIRECTIONS:
            raise ValueError(f"Unsupported direction: {self.direction}")

    def turn_left(self) -> None:
        if not self.lost:
            self.direction = LEFT_TURNS[self.direction]

    def turn_right(self) -> None:
        if not self.lost:
            self.direction = RIGHT_TURNS[self.direction]

    def pose(self) -> tuple[int, int, str, bool]:
        return self.x, self.y, self.direction, self.lost

    def snapshot(self) -> dict[str, object]:
        return {
            "x": self.x,
            "y": self.y,
            "direction": self.direction,
            "lost": self.lost,
        }


@dataclass(slots=True)
class World:
    width: int
    height: int
    scent_marks: set[tuple[int, int, str]] | None = None

    def __post_init__(self) -> None:
        if self.width < 0 or self.height < 0:
            raise ValueError("World dimensions must be non-negative")
        if self.scent_marks is None:
            self.scent_marks = set()

    def is_inside(self, x: int, y: int) -> bool:
        return 0 <= x <= self.width and 0 <= y <= self.height

    def has_scent(self, x: int, y: int, direction: str) -> bool:
        return (x, y, direction) in self.scent_marks

    def add_scent(self, x: int, y: int, direction: str) -> None:
        self.scent_marks.add((x, y, direction))

    def clear_scents(self) -> None:
        self.scent_marks.clear()

    def scent_summary(self) -> list[str]:
        return [f"({x}, {y}, {direction})" for x, y, direction in sorted(self.scent_marks)]


def execute_command(world: World, robot: Robot, command: str) -> str:
    if command not in VALID_COMMANDS:
        raise ValueError(f"Unsupported command: {command}")

    if robot.lost:
        return "LOST_IGNORED"

    if command == "L":
        robot.turn_left()
        return "TURN_LEFT"

    if command == "R":
        robot.turn_right()
        return "TURN_RIGHT"

    dx, dy = MOVES[robot.direction]
    next_x = robot.x + dx
    next_y = robot.y + dy
    if world.is_inside(next_x, next_y):
        robot.x = next_x
        robot.y = next_y
        return "MOVE"

    if world.has_scent(robot.x, robot.y, robot.direction):
        return "SCENT_BLOCKED"

    world.add_scent(robot.x, robot.y, robot.direction)
    robot.lost = True
    return "LOST"


def execute_commands(world: World, robot: Robot, commands: str) -> list[str]:
    actions: list[str] = []
    for command in commands:
        action = execute_command(world, robot, command)
        actions.append(action)
        if robot.lost:
            break
    return actions


def run_scenario(
    width: int,
    height: int,
    start_x: int,
    start_y: int,
    direction: str,
    commands: str,
    scents: set[tuple[int, int, str]] | None = None,
) -> tuple[Robot, World, list[str]]:
    world = World(width, height, set(scents or set()))
    robot = Robot(start_x, start_y, direction)
    actions = execute_commands(world, robot, commands)
    return robot, world, actions