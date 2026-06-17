"""R02: special methods on custom classes."""

from functools import total_ordering


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __repr__(self):
        return f"Student(name={self.name!r}, grade={self.grade})"

    def __str__(self):
        return f"{self.name}: {self.grade}"


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y


@total_ordering
class Score:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Score({self.value})"

    def __eq__(self, other):
        if not isinstance(other, Score):
            return NotImplemented
        return self.value == other.value

    def __lt__(self, other):
        if not isinstance(other, Score):
            return NotImplemented
        return self.value < other.value


class PointLite:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == "__main__":
    print("=== __repr__ / __str__ ===")
    s = Student("Alice", 85)
    print(repr(s))
    print(str(s))
    print(s)

    print("\n=== __eq__ ===")
    p1 = Point(1, 2)
    p2 = Point(1, 2)
    p3 = Point(3, 4)
    print(p1 == p2)
    print(p1 == p3)
    print(p1 is p2)

    print("\n=== total_ordering ===")
    a = Score(80)
    b = Score(90)
    print(a < b)
    print(a > b)
    print(a <= b)
    print(sorted([Score(70), Score(95), Score(60)]))

    print("\n=== __slots__ ===")
    p = PointLite(3, 4)
    print(p.x, p.y)
