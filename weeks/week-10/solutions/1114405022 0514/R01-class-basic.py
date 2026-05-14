# R01. 類別基礎（8.1）
# 本檔案示範 Python 類別（class）的基礎用法，包含：
# - 建構式 `__init__` 與 `self` 的概念
# - 特殊方法 `__repr__` 與 `__str__` 的差異
# - 實例方法（instance methods）與屬性存取
# - 類別變數（class variables）與實例變數（instance variables）之比較

# ── 最簡單的 class 範例 Point ─────────────────────────────────
# Point 用來表示平面上的一個點，具有 x 與 y 兩個座標
# 1. __init__(self, ...)：建構式，建立物件時會被呼叫，用來初始化實例屬性
# 2. self：指向當前實例（像 this），所有的實例屬性都透過 self.xxx 儲存
class Point:
    def __init__(self, x, y):
        # 將傳入參數儲存在實例屬性中
        self.x = x
        self.y = y

    # __repr__：給開發者看的字串表示，應盡量包含可重建物件的資訊
    # Python 交互式環境或 debug 時會使用 __repr__ 的輸出
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    # __str__：給使用者看的友善字串，會被 print() 使用
    # 若未定義 __str__，print() 會退回使用 __repr__ 的結果
    def __str__(self):
        return f"({self.x}, {self.y})"

    # 實例方法（instance method）：定義兩點間距離的計算
    def distance_to(self, other):
        # other 預期也是一個 Point 實例
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


# 使用範例：建立兩個 Point 實例並示範 __repr__/__str__ 與方法呼叫
p1 = Point(0, 0)
p2 = Point(3, 4)

print(repr(p1))             # 呼叫 __repr__，輸出: Point(0, 0)
print(str(p2))              # 呼叫 __str__，輸出: (3, 4)
print(p1.distance_to(p2))   # 使用實例方法，輸出: 5.0


# ── 類別變數 (class variables) vs 實例變數 (instance variables) ───────
# 類別變數：定義在 class 內且在任何實例之外，所有實例共同參考同一個變數
# 實例變數：透過 self.xxx 定義於 __init__ 或其他方法內，屬於每個實例獨立的資料
class Student:
    school = "國立澎湖科技大學"    # 類別變數：所有 Student 實例預設共用此值

    def __init__(self, name, student_id):
        # 實例變數：每個學生有自己的名字與學號
        self.name = name
        self.student_id = student_id

    def __repr__(self):
        return f"Student({self.student_id}, {self.name})"

    def greeting(self):
        # 存取類別變數 school（先在實例屬性查找，找不到則到類別變數）
        return f"我是 {self.school} 的 {self.name}"


s1 = Student("王小明", "11144050001")
s2 = Student("李小華", "11144050002")

print(s1.greeting())
print(s2.school)            # 透過實例也可以存取類別變數（語法允許，但實際從類別讀取）
print(Student.school)       # 透過類別名稱存取類別變數（較明確）

# 若直接修改類別變數，會影響到所有尚未覆寫該屬性的實例
Student.school = "NPU"
print(s1.school)            # NPU
print(s2.school)            # NPU
