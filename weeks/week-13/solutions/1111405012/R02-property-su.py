"""R02 property 簡化版。"""

import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("半徑不能為負數")
        self._radius = value

    @property
    def area(self):
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
