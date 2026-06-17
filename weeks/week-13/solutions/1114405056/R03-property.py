"""R03: property getter/setter patterns."""


class BadStudent:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        if not (0 <= value <= 100):
            raise ValueError(f"grade must be in [0, 100], got {value}")
        self._grade = value


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        import math

        return math.pi * self.radius**2

    @property
    def diameter(self):
        return self.radius * 2


class GradStudent(Student):
    @Student.grade.setter
    def grade(self, value):
        if not (0 <= value <= 150):
            raise ValueError(f"grad grade must be in [0, 150], got {value}")
        self._grade = value


if __name__ == "__main__":
    print("=== no guard ===")
    bad = BadStudent("Alice", 85)
    bad.grade = -100
    print(bad.name, bad.grade)

    print("\n=== guarded property ===")
    s = Student("Bob", 90)
    print(s.grade)
    s.grade = 75
    print(s.grade)
    try:
        s.grade = -10
    except ValueError as exc:
        print("error:", exc)

    print("\n=== readonly computed property ===")
    c = Circle(5)
    print(c.radius, c.diameter, f"{c.area:.2f}")
    c.radius = 10
    print(c.radius, c.diameter, f"{c.area:.2f}")

    print("\n=== override setter in subclass ===")
    g = GradStudent("Carol", 120)
    print(g.grade)
