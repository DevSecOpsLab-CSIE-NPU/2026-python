class Robot:
    """資工系專用：機器人邏輯核心 (UVA 118 規則)"""
    def __init__(self, x, y, direction, map_w, map_h, scents):
        self.x = x
        self.y = y
        self.direction = direction
        self.map_w = map_w
        self.map_h = map_h
        self.scents = scents # set of (x, y, dir)
        self.lost = False

        # 方向定義：北、東、南、西 (順時針)
        self.dirs = ['N', 'E', 'S', 'W']
        self.moves = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}

    def turn_left(self):
        if self.lost: return
        idx = (self.dirs.index(self.direction) - 1) % 4
        self.direction = self.dirs[idx]

    def turn_right(self):
        if self.lost: return
        idx = (self.dirs.index(self.direction) + 1) % 4
        self.direction = self.dirs[idx]

    def move_forward(self):
        if self.lost: return
        dx, dy = self.moves[self.direction]
        new_x, new_y = self.x + dx, self.y + dy

        # 檢查是否在邊界內
        if 0 <= new_x <= self.map_w and 0 <= new_y <= self.map_h:
            self.x, self.y = new_x, new_y
        else:
            # 檢查目前位置是否有危險氣味 (Scent)
            if (self.x, self.y, self.direction) not in self.scents:
                self.lost = True
                # 在掉落前的位置留下氣味
                self.scents.add((self.x, self.y, self.direction))
            # 如果已有氣味，則忽略該危險指令

    def execute(self, commands):
        """批次執行指令串"""
        for cmd in commands:
            if self.lost: break
            if cmd == 'L': self.turn_left()
            elif cmd == 'R': self.turn_right()
            elif cmd == 'F': self.move_forward()

    def get_status(self):
        status = f"{self.x} {self.y} {self.direction}"
        if self.lost: status += " LOST"
        return status
