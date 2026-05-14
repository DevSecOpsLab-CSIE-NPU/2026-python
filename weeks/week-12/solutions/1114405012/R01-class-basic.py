# R01. 類別基礎（8.1）
# __init__ / 方法 / __repr__ / __str__

# 這份示範重點：
# 1) 類別的基本構成：__init__、方法、self
# 2) __repr__ 與 __str__ 的區別
# 3) 類別變數 vs 實例變數
# 4) 如何透過實例或類別名稱存取類別變數

# ── 最簡單的 class ────────────────────────────────────────
# 類別是物件導向的基本單位，把資料和方法組合在一起
class Point:
    # __init__ 是創建物件時執行的初始化方法（構造方法）
    # self 代表當前建立中的物件實例（使用慣例就是這個詞彙）
    def __init__(self, x, y):
        # 設定實例變數
        self.x = x
        self.y = y

    # __repr__：給開發者看，eval() 能重建物件最理想
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    # __str__：給使用者看，print() 時呼叫，通常更簡潔
    def __str__(self):
        return f"({self.x}, {self.y})"

    # 實例方法：需要 self 為第一引數
    # 計算這個物件到另一個 Point 的距離（歐式距離）
    def distance_to(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


# 創建兩個 Point 實體，每個物件有自己的 x, y 實例變數
p1 = Point(0, 0)
p2 = Point(3, 4)

# repr(p1) 會執行 __repr__，回傳 "Point(0, 0)"
print(repr(p1))             # Point(0, 0)
# str(p2) 會執行 __str__，回傳 "(3, 4)"
print(str(p2))              # (3, 4)
# 計算 p1 到 p2 的距離（歐式距離）
print(p1.distance_to(p2))  # 5.0

# ── 類別變數 vs 實例變數 ──────────────────────────────────
# 類別變數：封定在整個類別裡，所有實體共用
# 實例變數：定義在 __init__ 或方法中，每個實體獨立
class Student:
    # 類別變數：所有 Student 實體會共用這個變數
    school = "國立澎湖科技大學"    # 類別變數：所有實例共用

    def __init__(self, name, student_id):
        # 實例變數：每個實例有各自的值
        self.name = name            # 實例變數：每個實例獨立
        self.student_id = student_id

    def __repr__(self):
        return f"Student({self.student_id}, {self.name})"

    # 實例方法中可以存取類別變數 self.school
    def greeting(self):
        return f"我是 {self.school} 的 {self.name}"


# 創建兩個 Student 實體。每個實體有自己的 name 和 student_id
# 但他們共用同一個 school 類別變數
s1 = Student("王小明", "11144050001")
s2 = Student("李小華", "11144050002")

# 執行實例方法 greeting()
print(s1.greeting())
# 方式 1：透過實例存取類別變數。如果實體沒有同名屬性，Python 會自動往上找
print(s2.school)            # 國立澎湖科技大學
# 方式 2：直接透過類別名稱存取類別變數
print(Student.school)       # 國立澎湖科技大學

# 修改類別變數會影響所有實例。所以不建議在 __init__ 中修改類別變數
Student.school = "NPU"
print(s1.school)            # NPU（即使 s1 沒有自己的 school，也會取得最新的類別變數）
print(s2.school)            # NPU
