# R01. 類別基礎（8.1）
# __init__ / 方法 / __repr__ / __str__
#
# 這個範例示範 Python 類別的最基本概念：
# 1. 使用 __init__ 建立物件時初始化資料。
# 2. 定義一般方法來描述物件行為。
# 3. 實作 __repr__ 與 __str__，控制物件被印出時的顯示方式。
# 4. 區分類別變數與實例變數。

# ── 最簡單的 class ────────────────────────────────────────
class Point:
    def __init__(self, x, y):
        # __init__ 是初始化方法，當你建立物件時會自動執行。
        # 這裡把傳入的 x、y 存成實例屬性，讓每個 Point 物件都能記住自己的座標。
        self.x = x
        self.y = y

    # __repr__：給開發者看，eval() 能重建物件最理想
    # __repr__ 盡量回傳一個「明確、可重建」的字串。
    # 開發時在除錯、互動式環境、容器輸出時，Python 通常會優先顯示這個表示法。
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    # __str__：給使用者看，print() 時呼叫
    # __str__ 是比較友善、適合直接展示給使用者看的字串形式。
    # 當你對物件使用 print() 或 str() 時，通常會走這個方法。
    def __str__(self):
        return f"({self.x}, {self.y})"

    def distance_to(self, other):
        # 這裡計算兩點之間的歐式距離。
        # 公式是 sqrt((x1-x2)^2 + (y1-y2)^2)，也就是平面上的直線距離。
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


# 建立兩個 Point 物件，分別代表 (0, 0) 與 (3, 4)。
# 建立物件時會自動呼叫 __init__，把座標存進各自的實例屬性中。
p1 = Point(0, 0)
p2 = Point(3, 4)

# repr(p1) 會呼叫 __repr__，適合看開發者模式下的物件表示法。
print(repr(p1))             # Point(0, 0)
# str(p2) 會呼叫 __str__，這裡回傳較簡潔、容易閱讀的格式。
print(str(p2))              # (3, 4)
# distance_to() 會用 p1 和 p2 的座標計算距離。
print(p1.distance_to(p2))  # 5.0

# ── 類別變數 vs 實例變數 ──────────────────────────────────
class Student:
    # 類別變數屬於整個 class，所有實例都共用同一份值。
    # 只要 Student.school 被修改，所有透過類別或實例存取到的值都會一起變。
    school = "國立澎湖科技大學"    # 類別變數：所有實例共用

    def __init__(self, name, student_id):
        # 實例變數屬於單一物件，每個 Student 物件都會有自己的 name 與 student_id。
        self.name = name            # 實例變數：每個實例獨立
        self.student_id = student_id

    def __repr__(self):
        # 這裡的 repr 會把學號與姓名組合成清楚的除錯字串。
        return f"Student({self.student_id}, {self.name})"

    def greeting(self):
        # 方法可以直接存取 self.name 與 self.school。
        # 這裡示範實例變數與類別變數一起出現在同一個方法中。
        return f"我是 {self.school} 的 {self.name}"


# 建立兩位學生物件，兩者共用同一個 school 類別變數。
s1 = Student("王小明", "11144050001")
s2 = Student("李小華", "11144050002")

# greeting() 會根據各自的 name 回傳不同訊息，但 school 目前相同。
print(s1.greeting())
# 實例也可以直接讀取類別變數，Python 會先找實例本身，找不到時再往類別找。
print(s2.school)            # 透過實例存取類別變數
# 直接透過類別名稱存取，是更清楚、也更常見的寫法。
print(Student.school)       # 透過類別名稱存取

# 修改類別變數影響所有實例
# 這裡把 Student.school 改成 NPU，所有還沒自己定義 school 的實例都會看到新值。
Student.school = "NPU"
# 因為 s1、s2 都沒有自己的 school 實例屬性，所以會讀到更新後的類別變數。
print(s1.school)            # NPU
print(s2.school)            # NPU
