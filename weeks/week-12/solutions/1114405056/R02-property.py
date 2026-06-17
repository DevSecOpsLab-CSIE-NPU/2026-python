"""R02: property encapsulation examples."""


class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("radius cannot be negative")
        self._radius = value

    @property
    def area(self):
        import math

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


if __name__ == "__main__":
    c = Circle(5)
    print(c.radius)
    print(c.area)
    print(c.diameter)

    c.radius = 10
    print(c.area)

    try:
        c.radius = -1
    except ValueError as e:
        print(e)

    try:
        c.area = 100
    except AttributeError as e:
        print(e)

    r = Rectangle(4, 6)
    print(r.area)
    print(r.perimeter)
    r.width = 8
    print(r.area)
