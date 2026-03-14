from dataclasses import dataclass

# Direction order for rotation
DIRECTIONS = ["N", "E", "S", "W"]

# Movement vectors
MOVES = {
    "N": (0, 1),
    "E": (1, 0),
    "S": (0, -1),
    "W": (-1, 0),
}


@dataclass
class Robot:
    x: int
    y: int
    direction: str
    lost: bool = False


def turn_left(direction: str) -> str:
    """Rotate robot 90 degrees left."""
    idx = DIRECTIONS.index(direction)
    return DIRECTIONS[(idx - 1) % 4]


def turn_right(direction: str) -> str:
    """Rotate robot 90 degrees right."""
    idx = DIRECTIONS.index(direction)
    return DIRECTIONS[(idx + 1) % 4]


def forward_position(x: int, y: int, direction: str) -> tuple[int, int]:
    """Calculate the next position if the robot moves forward."""
    dx, dy = MOVES[direction]
    return x + dx, y + dy


def is_out_of_bounds(x: int, y: int, width: int, height: int) -> bool:
    """Check if the position is outside the grid."""
    return x < 0 or x > width or y < 0 or y > height


def execute_instruction(
    robot: Robot,
    instruction: str,
    width: int,
    height: int,
    scents: set[tuple[int, int, str]],
) -> None:
    """
    Execute a single instruction (L, R, F).
    Handles rotation, movement, LOST condition, and scent logic.
    """

    if robot.lost:
        return

    if instruction == "L":
        robot.direction = turn_left(robot.direction)

    elif instruction == "R":
        robot.direction = turn_right(robot.direction)

    elif instruction == "F":
        nx, ny = forward_position(robot.x, robot.y, robot.direction)

        if is_out_of_bounds(nx, ny, width, height):

            scent = (robot.x, robot.y, robot.direction)

            # Ignore move if scent exists
            if scent in scents:
                return

            # Leave scent and mark robot lost
            scents.add(scent)
            robot.lost = True

        else:
            robot.x = nx
            robot.y = ny

    else:
        raise ValueError("Invalid instruction")


def execute_commands(
    robot: Robot,
    commands: str,
    width: int,
    height: int,
    scents: set[tuple[int, int, str]],
) -> Robot:
    """
    Execute a sequence of instructions for a robot.
    Stops execution if robot becomes LOST.
    """

    for command in commands:

        execute_instruction(robot, command, width, height, scents)

        if robot.lost:
            break

    return robot