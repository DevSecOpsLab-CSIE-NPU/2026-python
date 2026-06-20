DIR_ORDER = ["N", "E", "S", "W"]

DIRS = {
    "N": (0, 1),
    "E": (1, 0),
    "S": (0, -1),
    "W": (-1, 0),
}


class Robot:
    def __init__(self, x, y, direction, world=None, world_ref=None):
        self.x = x
        self.y = y
        self.dir = direction
        self.world = world
        self.world_ref = world_ref
        self.lost = False

    def _turn_left(self):
        idx = DIR_ORDER.index(self.dir)
        self.dir = DIR_ORDER[(idx - 1) % 4]

    def _turn_right(self):
        idx = DIR_ORDER.index(self.dir)
        self.dir = DIR_ORDER[(idx + 1) % 4]

    def _forward(self):
        if self.lost:
            return
        dx, dy = DIRS[self.dir]
        nx, ny = self.x + dx, self.y + dy
        if self.world and (nx < 0 or ny < 0 or nx > self.world[0] or ny > self.world[1]):
            if self.world_ref and (self.x, self.y, self.dir) in self.world_ref.scents:
                return
            self.lost = True
            if self.world_ref:
                self.world_ref.scents.add((self.x, self.y, self.dir))
            return
        self.x, self.y = nx, ny

    def execute(self, commands):
        for c in commands:
            if c not in "LRF":
                raise ValueError(f"無效指令: {c}")
            if self.lost:
                return
            if c == "L":
                self._turn_left()
            elif c == "R":
                self._turn_right()
            elif c == "F":
                self._forward()

    def state(self):
        status = f"({self.x}, {self.y}, {self.dir})"
        if self.lost:
            status += " LOST"
        return status


class RobotWorld:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.scents = set()
        self.robots = []

    def add_robot(self, robot):
        self.robots.append(robot)
