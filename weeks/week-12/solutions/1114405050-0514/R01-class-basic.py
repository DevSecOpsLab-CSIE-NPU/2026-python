# R01. 類別基礎（8.1）
# __init__ / 方法 / __repr__ / __str__

# ── 最簡單的 class ────────────────────────────────────────
class Point:
    # __init__ 是類別的建構子（初始化方法），在建立物件時會自動被呼叫
    # self 代表物件實例本身，x 和 y 是建立物件時傳入的參數
    def __init__(self, x, y):
        self.x = x  # 將傳入的參數 x 儲存為物件的實例變數 (屬性)
        self.y = y  # 將傳入的參數 y 儲存為物件的實例變數 (屬性)

    # __repr__：給開發者看，eval() 能重建物件最理想
    # 通常用於除錯與記錄，回傳一個能代表該物件的正式字串
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    # __str__：給使用者看，print() 時呼叫
    # 回傳一個容易閱讀的字串，若沒有定義 __str__，print 時會退而求其次呼叫 __repr__
    def __str__(self):
        return f"({self.x}, {self.y})"

    # 定義一般的實例方法，第一個參數必須是 self
    def distance_to(self, other):
        # 透過 self.x, self.y 取得自己的屬性，other.x, other.y 取得另一個物件的屬性
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


# 建立 Point 類別的實例 (物件)
p1 = Point(0, 0)
p2 = Point(3, 4)

print(repr(p1))             # Point(0, 0) （呼叫 p1.__repr__()）
print(str(p2))              # (3, 4)      （呼叫 p2.__str__()）
print(p1.distance_to(p2))   # 5.0         （計算 p1 到 p2 的距離）

# ── 類別變數 vs 實例變數 ──────────────────────────────────
class Student:
    school = "國立澎湖科技大學"    # 類別變數：定義在方法之外，所有實例共用同一份資料

    def __init__(self, name, student_id):
        self.name = name            # 實例變數：綁定在 self 上，每個實例各自擁有獨立的資料
        self.student_id = student_id

    def __repr__(self):
        return f"Student({self.student_id}, {self.name})"

    def greeting(self):
        # 透過 self.school 可以取得類別變數，self.name 取得實例變數
        return f"我是 {self.school} 的 {self.name}"


# 建立兩個不同的 Student 實例
s1 = Student("王小明", "11144050001")
s2 = Student("李小華", "11144050002")

print(s1.greeting())
print(s2.school)            # 透過實例存取類別變數
print(Student.school)       # 透過類別名稱存取

# 修改類別變數影響所有尚未覆寫該變數的實例
Student.school = "NPU"
print(s1.school)            # NPU (因為類別變數被修改了)
print(s2.school)            # NPU
