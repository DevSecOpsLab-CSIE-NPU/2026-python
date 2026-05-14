# R01. 類別基礎（8.1）
# __init__ / 方法 / __repr__ / __str__

# ── 最簡單的 class ────────────────────────────────────────
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # __repr__：給開發者看，eval() 能重建物件最理想
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    # __str__：給使用者看，print() 時呼叫
    def __str__(self):
        return f"({self.x}, {self.y})"

    def distance_to(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


p1 = Point(0, 0)
p2 = Point(3, 4)

print(repr(p1))             # Point(0, 0)
print(str(p2))              # (3, 4)
print(p1.distance_to(p2))  # 5.0

# ── 類別變數 vs 實例變數 ──────────────────────────────────
class Student:
    school = "國立澎湖科技大學"    # 類別變數：所有實例共用

    def __init__(self, name, student_id):
        self.name = name            # 實例變數：每個實例獨立
        self.student_id = student_id

    def __repr__(self):
        return f"Student({self.student_id}, {self.name})"

    def greeting(self):
        return f"我是 {self.school} 的 {self.name}"


s1 = Student("王小明", "11144050001")
s2 = Student("李小華", "11144050002")

print(s1.greeting())
print(s2.school)            # 透過實例存取類別變數
print(Student.school)       # 透過類別名稱存取

# 修改類別變數影響所有實例
Student.school = "NPU"
print(s1.school)            # NPU
print(s2.school)            # NPU
