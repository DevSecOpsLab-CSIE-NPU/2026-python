from dataclasses import dataclass

# The robot lost core is independent of pygame, enabling unit tests
# to validate behavior without any graphical dependencies.
# We define directions and their movement deltas globally for reuse.

directions = ["N", "E", "S", "W"]
delta = {"N": (0, 1), "E": (1, 0), "S": (0, -1), "W": (-1, 0)}


@dataclass
class Robot:
    x: int
    y: int
    dir: str
    lost: bool = False


class Grid:
    def __init__(self, width: int, height: int):
        # width and height define inclusive bounds (0..width,0..height)
        self.width = width
        self.height = height
        # scent stores tuples of (x,y,dir) where robots previously fell off
        self.scents: set[tuple[int, int, str]] = set()

    def execute(self, robot: Robot, instructions: str) -> Robot:
        """Run a sequence of commands on the given robot.

        The robot object is modified in place. If an illegal command
        appears we raise ValueError so that tests can capture misuse.
        If the robot becomes lost, subsequent commands are skipped.
        """
        for cmd in instructions:
            if robot.lost:
                break  # LOST robots stop processing
            if cmd == "L":
                self._turn_left(robot)
            elif cmd == "R":
                self._turn_right(robot)
            elif cmd == "F":
                self._forward(robot)
            else:
                raise ValueError(f"illegal instruction: {cmd}")
        return robot

    def _turn_left(self, robot: Robot) -> None:
        idx = directions.index(robot.dir)
        robot.dir = directions[(idx - 1) % 4]

    def _turn_right(self, robot: Robot) -> None:
        idx = directions.index(robot.dir)
        robot.dir = directions[(idx + 1) % 4]

    def _forward(self, robot: Robot) -> None:
        dx, dy = delta[robot.dir]
        nx = robot.x + dx
        ny = robot.y + dy
        # Check if moving off the grid
        if nx < 0 or nx > self.width or ny < 0 or ny > self.height:
            # if scent exists, ignore command
            if (robot.x, robot.y, robot.dir) in self.scents:
                return
            # else robot is lost and leaves a scent at current position
            self.scents.add((robot.x, robot.y, robot.dir))
            robot.lost = True
        else:
            robot.x = nx
            robot.y = ny


def parse_state(line: str) -> Robot:
    """Convert a string like '3 2 N' into a Robot instance."""
    parts = line.strip().split()
    if len(parts) != 3:
        raise ValueError("invalid state format")
    x, y, d = parts
    return Robot(int(x), int(y), d)


def format_state(robot: Robot) -> str:
    """Produce output string for a robot (add LOST if applicable)."""
    s = f"{robot.x} {robot.y} {robot.dir}"
    if robot.lost:
        s += " LOST"
    return s
