"""R01. 類別基礎（8.1）"""

from __future__ import annotations


class Point:
    """最簡單的二維點類別。"""

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        """給開發者看，理想上應能清楚重建物件狀態。"""
        return f"Point({self.x}, {self.y})"

    def __str__(self) -> str:
        """給一般使用者看，格式更簡短。"""
        return f"({self.x}, {self.y})"

    def distance_to(self, other: "Point") -> float:
        """計算自己到另一個點的歐式距離。"""
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


class Student:
    """示範類別變數與實例變數的差異。"""

    school = "國立澎湖科技大學"

    def __init__(self, name: str, student_id: str):
        self.name = name
        self.student_id = student_id

    def __repr__(self) -> str:
        return f"Student({self.student_id}, {self.name})"

    def greeting(self) -> str:
        return f"我是 {self.school} 的 {self.name}"


def main() -> None:
    """印出課堂上示範的類別基礎結果。"""
    point_a = Point(0, 0)
    point_b = Point(3, 4)

    print(repr(point_a))
    print(str(point_b))
    print(point_a.distance_to(point_b))

    student_a = Student("王小明", "11144050001")
    student_b = Student("李小華", "11144050002")

    print(student_a.greeting())
    print(student_b.school)
    print(Student.school)

    Student.school = "NPU"
    print(student_a.school)
    print(student_b.school)


if __name__ == "__main__":
    main()
