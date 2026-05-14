"""
R01. 類別基礎（8.1）

本範例示範 Python 類別（class）的基本概念：
    1. 使用 __init__ 建立物件並初始化屬性
    2. 定義一般方法，讓物件具備行為
    3. 使用 __repr__ 與 __str__ 控制物件顯示方式
    4. 理解類別變數與實例變數的差異

這些概念是物件導向程式設計的基礎，後續的繼承、多型、封裝都建立在這些觀念上。
"""

# ── 最簡單的 class ────────────────────────────────────────
class Point:
    # __init__ 是建構子，當你呼叫 Point(0, 0) 時會自動執行。
    # self 代表「目前這個物件本身」，用來保存該物件的狀態。
    def __init__(self, x, y):
        # x 與 y 是實例屬性，每個 Point 物件都會各自保存自己的座標。
        self.x = x
        self.y = y

    # __repr__：給開發者看，通常應盡量提供可以清楚重建物件的表示法。
    # 理想情況下，repr() 的結果應該接近可重新建立物件的程式碼。
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    # __str__：給使用者看，print() 或 str() 時會優先使用這個方法。
    # 一般來說，__str__ 可以比 __repr__ 更簡潔、更友善。
    def __str__(self):
        return f"({self.x}, {self.y})"

    # distance_to 是物件的方法，用來計算「目前點」到另一個點的距離。
    # 這裡使用平面座標的歐幾里得距離公式：sqrt((x1-x2)^2 + (y1-y2)^2)
    def distance_to(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


# 建立兩個 Point 物件，分別代表 (0, 0) 和 (3, 4)
# 這裡的 p1、p2 都是 Point 類別的實例（instance）
p1 = Point(0, 0)
p2 = Point(3, 4)

# repr() 會呼叫 __repr__，適合用在除錯、log 或互動式環境中查看物件內容。
print(repr(p1))             # Point(0, 0)
# str() 會呼叫 __str__，通常是給人看的簡潔格式。
print(str(p2))              # (3, 4)
# distance_to() 會回傳兩點之間的距離。
print(p1.distance_to(p2))  # 5.0

# ── 類別變數 vs 實例變數 ──────────────────────────────────
class Student:
    # 類別變數屬於整個類別，而不是單一物件。
    # 所有 Student 實例都可以共用同一份 school。
    school = "國立澎湖科技大學"    # 類別變數：所有實例共用

    def __init__(self, name, student_id):
        # 實例變數屬於單一物件，每個學生物件都可以有自己的 name 與 student_id。
        self.name = name            # 實例變數：每個實例獨立
        self.student_id = student_id

    # 這裡的 __repr__ 用來清楚顯示學生資料，方便除錯與印出物件時查看。
    def __repr__(self):
        return f"Student({self.student_id}, {self.name})"

    # greeting() 是一般方法，會使用實例變數與類別變數組合出一句自我介紹。
    # 注意 self.school 若實例本身沒有 school，會往類別層級尋找。
    def greeting(self):
        return f"我是 {self.school} 的 {self.name}"


# 建立兩個學生實例，每個實例都有自己獨立的 name 和 student_id。
s1 = Student("王小明", "11144050001")
s2 = Student("李小華", "11144050002")

# greeting() 會讀取 school 與 name，組合成可讀的介紹文字。
print(s1.greeting())
# 透過實例也可以讀取類別變數；若實例沒有同名屬性，就會去類別找。
print(s2.school)            # 透過實例存取類別變數
# 也可以直接用類別名稱存取類別變數，這是最清楚的寫法。
print(Student.school)       # 透過類別名稱存取

# 修改類別變數會影響所有尚未另外覆寫同名屬性的實例。
# 這是因為 school 原本是共享的類別屬性，改掉類別上的值後，所有引用它的實例都會看到新值。
Student.school = "NPU"
print(s1.school)            # NPU
print(s2.school)            # NPU
