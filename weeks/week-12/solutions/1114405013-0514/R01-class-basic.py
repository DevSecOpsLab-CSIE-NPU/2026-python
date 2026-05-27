# R01. 類別基礎（8.1）
# __init__ / 方法 / __repr__ / __str__ / 類別變數

from __future__ import annotations

# ------------------------------------------------------------
# 最簡單的 class 範例：Point
# ------------------------------------------------------------
class Point:
    def __init__(self, x: float, y: float) -> None:
        # 實例變數：每個 Point 物件都有自己的 x 與 y
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        # __repr__：給開發者看的表示方式，理想情況下可用於重建物件
        return f"Point({self.x}, {self.y})"

    def __str__(self) -> str:
        # __str__：給使用者看的表示方式，print() 時呼叫
        return f"({self.x}, {self.y})"

    def distance_to(self, other: Point) -> float:
        # 方法：計算目前這個點與另一個點之間的距離
        dx = self.x - other.x
        dy = self.y - other.y
        return (dx ** 2 + dy ** 2) ** 0.5


# 建立兩個 Point 實例
p1 = Point(0, 0)
p2 = Point(3, 4)

print(repr(p1))             # Point(0, 0)
print(str(p2))              # (3, 4)
print(p1.distance_to(p2))   # 5.0

# ------------------------------------------------------------
# 類別變數 vs 實例變數
# ------------------------------------------------------------
class Student:
    school = "國立澎湖科技大學"    # 類別變數：所有實例共用，同一個名稱對應同一個值

    def __init__(self, name: str, student_id: str) -> None:
        # 實例變數：每個 Student 物件各自持有自己的 name 與 student_id
        self.name = name
        self.student_id = student_id

    def __repr__(self) -> str:
        return f"Student({self.student_id}, {self.name})"

    def greeting(self) -> str:
        # 使用類別變數 self.school：先從實例查找，再回退到類別層級
        return f"我是 {self.school} 的 {self.name}"


s1 = Student("王小明", "11144050001")
s2 = Student("李小華", "11144050002")

print(s1.greeting())        # 我是 國立澎湖科技大學 的 王小明
print(s2.school)            # 透過實例存取類別變數
print(Student.school)       # 透過類別名稱存取類別變數

# 修改類別變數會影響所有實例（因為它們都參考同一個類別屬性）
Student.school = "NPU"
print(s1.school)            # NPU
print(s2.school)            # NPU

# ------------------------------------------------------------
# 類別與實例屬性查找順序
# ------------------------------------------------------------
# 如果某個實例自己定義了同名屬性，會遮蔽類別變數
s2.school = "個人學院"
print(s2.school)            # 個人學院（實例屬性遮蔽類別屬性）
print(Student.school)       # NPU（類別屬性仍舊是 NPU）
print(s1.school)            # NPU（s1 沒有自己的 school 屬性，使用類別屬性）
