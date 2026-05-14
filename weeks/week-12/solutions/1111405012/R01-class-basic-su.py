"""R01 類別基礎簡化版。"""


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
    school = "國立澎湖科技大學"

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def greeting(self):
        return f"我是 {self.school} 的 {self.name}"


def main():
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    print(repr(p1))
    print(str(p2))
    print(p1.distance_to(p2))

    s1 = Student("王小明", "11144050001")
    s2 = Student("李小華", "11144050002")
    print(s1.greeting())
    print(s2.school)
    Student.school = "NPU"
    print(s1.school)
    print(s2.school)


if __name__ == "__main__":
    main()
