# AI Easy 版: 10409 Die Game
import sys

class Dice:
    """
    骰子類別：維護骰子的六面狀態
    初始狀態：頂=1, 北=2, 西=3
    """
    def __init__(self):
        self.top, self.north, self.west = 1, 2, 3
        self.south, self.east, self.bottom = 5, 4, 6

    def roll(self, direction):
        """根據方向翻轉骰子面"""
        if direction == 'north':
            self.top, self.north, self.bottom, self.south = self.south, self.top, self.north, self.bottom
        elif direction == 'south':
            self.top, self.south, self.bottom, self.north = self.north, self.top, self.south, self.bottom
        elif direction == 'east':
            self.top, self.east, self.bottom, self.west = self.west, self.top, self.east, self.bottom
        elif direction == 'west':
            self.top, self.west, self.bottom, self.east = self.east, self.top, self.west, self.bottom

def solve():
    raw = sys.stdin.read().split()
    if not raw: return
    idx = 0
    while idx < len(raw):
        try:
            n = int(raw[idx]); idx += 1
            if n == 0: break
            d = Dice()
            for _ in range(n):
                d.roll(raw[idx]); idx += 1
            print(d.top)
        except (ValueError, IndexError): break

if __name__ == "__main__":
    solve()
