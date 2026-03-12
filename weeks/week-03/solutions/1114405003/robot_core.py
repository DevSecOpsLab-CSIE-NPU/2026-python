from __future__ import annotations

MOVE_DELTAS = {
    'N': (0, 1),
    'E': (1, 0),
    'S': (0, -1),
    'W': (-1, 0),
}
LEFT_TURN = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
RIGHT_TURN = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
VALID_DIRECTIONS = set(MOVE_DELTAS.keys())
VALID_COMMANDS = {'L', 'R', 'F'}


class RobotWorld:
    def __init__(self, max_x: int, max_y: int):
        if max_x < 0 or max_y < 0:
            raise ValueError("map size must be non-negative")
        self.max_x = max_x
        self.max_y = max_y
        self.scents: set[tuple[int, int, str]] = set()

    def is_outside(self, x: int, y: int) -> bool:
        return x < 0 or y < 0 or x > self.max_x or y > self.max_y

    def create_robot(self, x: int, y: int, direction: str) -> 'Robot':
        return Robot(x, y, direction, self)


class Robot:
    def __init__(self, x: int, y: int, direction: str, world: RobotWorld):
        if direction not in VALID_DIRECTIONS:
            raise ValueError(f"invalid direction '{direction}'")
        if x < 0 or y < 0 or x > world.max_x or y > world.max_y:
            raise ValueError("initial position outside boundaries")
        self.x = x
        self.y = y
        self.direction = direction
        self.lost = False
        self.world = world

    def turn_left(self):
        if self.lost:
            return
        self.direction = LEFT_TURN[self.direction]

    def turn_right(self):
        if self.lost:
            return
        self.direction = RIGHT_TURN[self.direction]

    def move_forward(self):
        if self.lost:
            return
        dx, dy = MOVE_DELTAS[self.direction]
        next_x = self.x + dx
        next_y = self.y + dy
        if self.world.is_outside(next_x, next_y):
            scent = (self.x, self.y, self.direction)
            if scent in self.world.scents:
                return
            self.world.scents.add(scent)
            self.lost = True
            return
        self.x, self.y = next_x, next_y

    def execute(self, commands: str):
        for c in commands:
            if self.lost:
                break
            if c not in VALID_COMMANDS:
                raise ValueError(f"invalid command '{c}'")
            if c == 'L':
                self.turn_left()
            elif c == 'R':
                self.turn_right()
            elif c == 'F':
                self.move_forward()

    def state(self) -> tuple[int, int, str, bool]:
        return (self.x, self.y, self.direction, self.lost)

    def __repr__(self) -> str:
        status = 'LOST' if self.lost else 'ALIVE'
        return f"Robot({self.x},{self.y},{self.direction},{status})"
