# U01. 骰子模擬示範
# 這個範例用類別封裝骰子狀態，示範物件導向在模擬題中的應用。

class Die:
    """骰子物件，追蹤六個面朝向：top、bottom、north、south、east、west。"""

    def __init__(self):
        # 依題目規定設定初始朝向
        self.top = 1
        self.bottom = 6
        self.north = 2
        self.south = 5
        self.west = 3
        self.east = 4

    def roll_north(self):
        # 向北滾動：top <- north, south <- top, bottom <- south, north <- bottom
        self.top, self.south, self.bottom, self.north = (
            self.north, self.top, self.south, self.bottom
        )

    def roll_south(self):
        self.top, self.north, self.bottom, self.south = (
            self.south, self.top, self.north, self.bottom
        )

    def roll_east(self):
        self.top, self.west, self.bottom, self.east = (
            self.east, self.top, self.west, self.bottom
        )

    def roll_west(self):
        self.top, self.east, self.bottom, self.west = (
            self.west, self.top, self.east, self.bottom
        )

    def roll(self, direction: str):
        # 根據輸入方向呼叫對應的滾動方法
        {
            "north": self.roll_north,
            "south": self.roll_south,
            "east": self.roll_east,
            "west": self.roll_west,
        }[direction]()

    def __repr__(self):
        return (f"Die(top={self.top}, bottom={self.bottom}, "
                f"N={self.north}, S={self.south}, E={self.east}, W={self.west})")


import sys


def solve():
    for line in sys.stdin:
        line = line.strip()
        if not line or line == "STOP":
            break
        die = Die()
        for direction in line.split():
            die.roll(direction)
        print(die.top)


if __name__ == "__main__":
    test_cases = [
        ("north", 2),
        ("south", 5),
        ("east", 4),
        ("west", 3),
        ("north south", 1),
        ("north east south west", 1),
    ]

    for moves, expected in test_cases:
        die = Die()
        for m in moves.split():
            die.roll(m)
        result = die.top
        status = "OK" if result == expected else f"FAIL (expected {expected})"
        print(f"moves={moves!r:30s}  top={result}  {status}")
