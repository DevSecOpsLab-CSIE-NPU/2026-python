"""R02. 屬性封裝（8.6）"""

from __future__ import annotations

import math


class Circle:
    """示範 getter、setter 與唯讀屬性。"""

    def __init__(self, radius: float):
        # 初始化也走 setter，才能沿用同一套驗證規則。
        self.radius = radius

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float) -> None:
        if value < 0:
            raise ValueError("半徑不能為負數")
        self._radius = value

    @property
    def area(self) -> float:
        """唯讀屬性：面積由半徑計算而來，不應手動指定。"""
        return math.pi * self._radius**2

    @property
    def diameter(self) -> float:
        return self._radius * 2


class Rectangle:
    """示範根據目前屬性動態計算面積與周長。"""

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    @property
    def area(self) -> float:
        return self.width * self.height

    @property
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


def main() -> None:
    """印出課堂上示範的 property 行為。"""
    circle = Circle(5)
    print(circle.radius)
    print(circle.area)
    print(circle.diameter)

    circle.radius = 10
    print(circle.area)

    try:
        circle.radius = -1
    except ValueError as error:
        print(error)

    try:
        circle.area = 100
    except AttributeError as error:
        print(error)

    rectangle = Rectangle(4, 6)
    print(rectangle.area)
    print(rectangle.perimeter)
    rectangle.width = 8
    print(rectangle.area)


if __name__ == "__main__":
    main()
