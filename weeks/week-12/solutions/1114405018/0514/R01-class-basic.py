"""R01. 類別基礎（8.1）

說明（繁體中文詳細註解）：
- 本檔示範 Python 類別（class）的基本寫法，包括建構子 `__init__`、實例方法、以及常用的特殊方法 `__repr__` 與 `__str__`。
- `__repr__` 偏向給開發者（debug）看的字串形式，理想情況下可用來重建物件；`__str__` 則是給使用者看的友善字串（print 使用）。

使用情境與提醒：
- 類別變數（class attribute）會被所有實例共用；實例變數（instance attribute）則屬於某個實例。
- 若要可比較或序列化物件，適當實作 `__repr__`, `__eq__` 等特殊方法會很有幫助。
"""


# ── 最簡單的 class 範例 ─────────────────────────────────────
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

# ── 類別變數 vs 實例變數（示範）───────────────────────────
class Student:
    # 類別變數：在類別定義上宣告，所有實例預設共用此值
    school = "國立澎湖科技大學"

    def __init__(self, name, student_id):
        # 實例變數：存在於每個具體的實例中
        self.name = name
        self.student_id = student_id

    def __repr__(self):
        return f"Student({self.student_id}, {self.name})"

    def greeting(self):
        # 透過 self.school 仍然可以取得類別變數（除非被覆寫）
        return f"我是 {self.school} 的 {self.name}"


s1 = Student("王小明", "11144050001")
s2 = Student("李小華", "11144050002")

print(s1.greeting())
print(s2.school)            # 透過實例存取類別變數
print(Student.school)       # 透過類別名稱存取

# 修改類別變數會影響所有尚未覆寫此值的實例
Student.school = "NPU"
print(s1.school)            # NPU
print(s2.school)            # NPU
