# R01. 類別基礎（8.1）
# __init__ / 方法 / __repr__ / __str__
#
# 本檔示範 Python 類別最核心的語法：
# 1) class 定義與 __init__ 初始化方法
# 2) __repr__（給開發者）與 __str__（給使用者）的差別
# 3) 類別變數（所有實例共用）vs 實例變數（每個實例獨立）

# ── 最簡單的 class ────────────────────────────────────────
# class 關鍵字定義新型別，名稱慣例首字母大寫（PEP 8）
class Point:
    def __init__(self, x, y):
        # __init__ 是「初始化方法」，建立物件時自動呼叫。
        # self 代表「被建立的這個實例本身」，永遠是第一個參數。
        self.x = x   # 把傳入的 x 存成實例屬性，之後用 self.x 存取
        self.y = y   # 同上，存成實例屬性

    # __repr__：給開發者看，eval() 能重建物件最理想
    # 在互動式終端直接輸入物件名稱，或用 repr() 函式時觸發
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    # __str__：給使用者看，print() 時呼叫
    # 若沒定義 __str__，Python 會退而求其次使用 __repr__
    def __str__(self):
        return f"({self.x}, {self.y})"

    def distance_to(self, other):
        # 計算與另一個 Point 的歐幾里得距離（畢氏定理）
        # other 是另一個 Point 實例，可直接存取其 .x 和 .y
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


p1 = Point(0, 0)   # 原點
p2 = Point(3, 4)   # 與原點距離 5（3-4-5 直角三角形）

print(repr(p1))             # Point(0, 0) — 呼叫 __repr__
print(str(p2))              # (3, 4)      — 呼叫 __str__
print(p1.distance_to(p2))  # 5.0

# ── 類別變數 vs 實例變數 ──────────────────────────────────
# 類別變數：定義在 class 主體最外層（不在任何方法內），
#           所有由此類別建立的實例都共用同一份資料。
# 實例變數：在 __init__ 裡透過 self.xxx = ... 建立，
#           每個物件各自持有，互不干擾。
class Student:
    school = "國立澎湖科技大學"    # 類別變數：所有實例共用

    def __init__(self, name, student_id):
        self.name = name            # 實例變數：每個實例獨立
        self.student_id = student_id

    def __repr__(self):
        return f"Student({self.student_id}, {self.name})"

    def greeting(self):
        # 方法內可直接用 self.school 讀取類別變數
        return f"我是 {self.school} 的 {self.name}"


s1 = Student("王小明", "11144050001")
s2 = Student("李小華", "11144050002")

print(s1.greeting())
print(s2.school)            # 透過實例也可以存取類別變數
print(Student.school)       # 直接透過類別名稱存取，語意更清楚

# 透過「類別名稱」修改類別變數，會立即影響所有實例
# 注意：若改成 s1.school = "XXX" 只會在 s1 建立遮蔽用的實例變數，
# 並不會影響 s2 或未來建立的物件。
Student.school = "NPU"
print(s1.school)            # NPU
print(s2.school)            # NPU
