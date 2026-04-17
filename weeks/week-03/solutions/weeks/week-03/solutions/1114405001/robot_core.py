# 方向映射
DIRECTIONS = {
    'N': (0, -1),
    'E': (1, 0),
    'S': (0, 1),
    'W': (-1, 0)
}

TURN_LEFT = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
TURN_RIGHT = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}

class Robot:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.lost = False

    def turn_left(self):
        self.direction = TURN_LEFT[self.direction]

    def turn_right(self):
        self.direction = TURN_RIGHT[self.direction]

    def move_forward(self, grid_width, grid_height, scents):
        if self.lost:
            return
        dx, dy = DIRECTIONS[self.direction]
        new_x = self.x + dx
        new_y = self.y + dy
        if new_x < 0 or new_x > grid_width or new_y < 0 or new_y > grid_height:
            # 檢查 scent
            if (self.x, self.y, self.direction) not in scents:
                self.lost = True
                scents.add((self.x, self.y, self.direction))
            # 如果有 scent，不移動
        else:
            self.x = new_x
            self.y = new_y
