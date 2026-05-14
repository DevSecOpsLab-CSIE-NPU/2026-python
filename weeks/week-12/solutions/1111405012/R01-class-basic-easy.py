"""R01 類別基礎詳細註解版。"""


class Point:
    def __init__(self, x, y):
        # 每個 Point 物件都記住自己的 x 與 y。
        self.x = x
        self.y = y

    def __repr__(self):
        # repr 通常給開發者看，會盡量清楚顯示物件內容。
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        # str 通常給使用者看，格式可以更簡短。
        return f"({self.x}, {self.y})"

    def distance_to(self, other):
        # 兩點距離公式：
        # sqrt((x1-x2)^2 + (y1-y2)^2)
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


class Student:
    # 類別變數：所有 Student 物件共用同一份資料。
    school = "國立澎湖科技大學"

    def __init__(self, name, student_id):
        # 實例變數：每個學生自己的資料。
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

    # 修改類別變數後，所有實例都會看到更新後的值。
    Student.school = "NPU"
    print(s1.school)
    print(s2.school)


if __name__ == "__main__":
    main()
