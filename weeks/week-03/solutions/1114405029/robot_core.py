class RobotWorld:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.scents = set()
        print(f"[系統] 地圖初始化成功: {width}x{height}")

    def is_off_map(self, x, y):
        return x < 0 or x > self.width or y < 0 or y > self.height

class Robot:
    DIRECTIONS = ['N', 'E', 'S', 'W']
    MOVEMENTS = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}

    def __init__(self, x, y, orientation, world):
        self.x, self.y = x, y
        self.orientation = orientation
        self.world = world
        self.lost = False

    def turn_left(self):
        if self.lost: return
        idx = self.DIRECTIONS.index(self.orientation)
        self.orientation = self.DIRECTIONS[(idx - 1) % 4]

    def turn_right(self):
        if self.lost: return
        idx = self.DIRECTIONS.index(self.orientation)
        self.orientation = self.DIRECTIONS[(idx + 1) % 4]

    def move_forward(self):
        if self.lost: return
        dx, dy = self.MOVEMENTS[self.orientation]
        new_x, new_y = self.x + dx, self.y + dy

        if self.world.is_off_map(new_x, new_y):
            if (self.x, self.y, self.orientation) in self.world.scents:
                print(f"[警告] 機器人在 ({self.x},{self.y}) 偵測到 Scent，忽略危險指令")
                return
            else:
                self.lost = True
                self.world.scents.add((self.x, self.y, self.orientation))
                print(f"[事件] 機器人掉落！位置: ({self.x},{self.y}) 方向: {self.orientation}")
        else:
            self.x, self.y = new_x, new_y

    def execute_command(self, cmd):
        if self.lost: return
        if cmd == 'L': self.turn_left()
        elif cmd == 'R': self.turn_right()
        elif cmd == 'F': self.move_forward()