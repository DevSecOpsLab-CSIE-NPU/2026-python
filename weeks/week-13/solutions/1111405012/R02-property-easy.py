"""R02 property 詳細註解版。"""

import math


class Circle:
    def __init__(self, radius):
        # 初始化時直接走 setter，
        # 這樣一開始就會做負值檢查。
        self.radius = radius

    @property
    def radius(self):
        # getter：讀取 c.radius 時會跑到這裡。
        return self._radius

    @radius.setter
    def radius(self, value):
        # setter：指定 c.radius = 新值 時會跑到這裡。
        if value < 0:
            raise ValueError("半徑不能為負數")
        self._radius = value

    @property
    def area(self):
        # area 沒有 setter，所以是唯讀屬性。
        return math.pi * self._radius**2

    @property
    def diameter(self):
        return self._radius * 2


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        # 每次讀取時重新計算，
        # 所以 width 或 height 一改，面積就自動更新。
        return self.width * self.height

    @property
    def perimeter(self):
        return 2 * (self.width + self.height)


def main():
    c = Circle(5)
    print(c.radius)
    print(c.area)
    print(c.diameter)
    c.radius = 10
    print(c.area)

    r = Rectangle(4, 6)
    print(r.area)
    print(r.perimeter)


if __name__ == "__main__":
    main()
