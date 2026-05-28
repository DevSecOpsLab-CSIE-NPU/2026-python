# U01. 骰子模擬（UVA 10409 Die Game）
# 用 class 封裝骰子狀態，示範物件導向如何讓模擬題更清晰

# ── 骰子初始狀態 ──────────────────────────────────────────
# 題目規定：頂=1, 北=2, 西=3
# 相對面之和為 7：1↔6, 2↔5, 3↔4

class Die:
    """骰子，追蹤六個面的朝向：top, bottom, north, south, east, west"""

    def __init__(self):
        self.top    = 1
        self.bottom = 6
        self.north  = 2
        self.south  = 5
        self.west   = 3
        self.east   = 4

    def roll_north(self):
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
        {"north": self.roll_north,
         "south": self.roll_south,
         "east":  self.roll_east,
         "west":  self.roll_west}[direction]()

    def __repr__(self):
        return (f"Die(top={self.top}, bottom={self.bottom}, "
                f"N={self.north}, S={self.south}, E={self.east}, W={self.west})")


# ── 解題主程式 ────────────────────────────────────────────
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


# ── 手動測試 ──────────────────────────────────────────────
if __name__ == "__main__":
    test_cases = [
        ("north", 2),
        ("south", 5),
        ("east",  4),
        ("west",  3),
        ("north south", 1),     # 滾回原位，頂面還是 1
        ("north east south west", 1),
    ]

    for moves, expected in test_cases:
        die = Die()
        for m in moves.split():
            die.roll(m)
        result = die.top
        status = "OK" if result == expected else f"FAIL (expected {expected})"
        print(f"moves={moves!r:30s}  top={result}  {status}")
