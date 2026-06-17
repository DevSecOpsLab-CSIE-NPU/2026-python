"""R01: class basics (__init__, methods, __repr__, __str__)."""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def distance_to(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


class Student:
    school = "NPU"

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def __repr__(self):
        return f"Student({self.student_id}, {self.name})"

    def greeting(self):
        return f"I am {self.name} from {self.school}."


if __name__ == "__main__":
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    print(repr(p1))
    print(str(p2))
    print(p1.distance_to(p2))

    s1 = Student("Alice", "11144050001")
    s2 = Student("Bob", "11144050002")
    print(s1.greeting())
    print(s2.school)
    print(Student.school)

    Student.school = "NPU-CS"
    print(s1.school)
    print(s2.school)
