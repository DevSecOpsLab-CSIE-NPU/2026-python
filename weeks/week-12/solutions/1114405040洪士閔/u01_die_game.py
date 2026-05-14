"""U01. 骰子模擬（UVA 10409 Die Game）。

這份版本用 class 封裝骰子的六個面，讓旋轉邏輯更好讀、也更好維護，
並加上較完整的繁體中文註解。
"""

import sys


# 題目規定的初始方向：頂=1, 北=2, 西=3，對面和為 7。
class Die:
    """追蹤骰子六個面的朝向。"""

    def __init__(self):
        self.top = 1
        self.bottom = 6
        self.north = 2
        self.south = 5
        self.west = 3
        self.east = 4

    def roll_north(self):
        # 往北滾：頂面、南面、底面、北面會互換位置。
        self.top, self.south, self.bottom, self.north = (
            self.north, self.top, self.south, self.bottom
        )

    def roll_south(self):
        # 往南滾：頂面、北面、底面、南面會互換位置。
        self.top, self.north, self.bottom, self.south = (
            self.south, self.top, self.north, self.bottom
        )

    def roll_east(self):
        # 往東滾：頂面、西面、底面、東面會互換位置。
        self.top, self.west, self.bottom, self.east = (
            self.east, self.top, self.west, self.bottom
        )

    def roll_west(self):
        # 往西滾：頂面、東面、底面、西面會互換位置。
        self.top, self.east, self.bottom, self.west = (
            self.west, self.top, self.east, self.bottom
        )

    def roll(self, direction: str):
        # 依照輸入方向，呼叫對應的滾動方法。
        {
            "north": self.roll_north,
            "south": self.roll_south,
            "east": self.roll_east,
            "west": self.roll_west,
        }[direction]()

    def __repr__(self):
        return (
            f"Die(top={self.top}, bottom={self.bottom}, "
            f"N={self.north}, S={self.south}, E={self.east}, W={self.west})"
        )


# 主程式：讀入每一行指令，直到 STOP 為止。
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
    # 手動測試：確認幾個基本滾動方向是否正確。
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
