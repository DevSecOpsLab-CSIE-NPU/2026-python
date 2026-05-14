# R01. 類別基礎（8.1）
# __init__ / 方法 / __repr__ / __str__

# ── 最簡單的 class ────────────────────────────────────────

# class Point：
# 定義一個名為 Point 的類別（class）

# class 是 Python 的物件導向（OOP）核心概念
# 可以把 class 想成：
# 「建立物件的藍圖」

# Point 類別用來表示：
# 二維平面上的一個點
class Point:

    # __init__()：
    # 建構子（constructor）

    # 當建立物件時會自動呼叫
    # 例如：
    # p1 = Point(0, 0)

    # self：
    # 代表目前建立的物件本身

    # x、y：
    # 建立物件時傳入的參數
    def __init__(self, x, y):

        # self.x：
        # 物件自己的 x 座標

        # self.y：
        # 物件自己的 y 座標

        # 這些稱為：
        # 「實例變數（instance variable）」
        self.x = x
        self.y = y

    # __repr__：給開發者看，eval() 能重建物件最理想

    # __repr__()：
    # 當使用：
    # repr(obj)
    # 或直接在互動模式輸入物件時呼叫

    # 主要用途：
    # 給開發者除錯使用

    # 理想情況：
    # repr 的結果可以重新建立相同物件
    def __repr__(self):

        # f-string 格式化輸出
        # 回傳：
        # Point(0, 0)
        return f"Point({self.x}, {self.y})"

    # __str__：給使用者看，print() 時呼叫

    # __str__()：
    # 當使用：
    # print(obj)
    # str(obj)

    # 主要用途：
    # 提供人類容易閱讀的格式
    def __str__(self):

        # 回傳較簡潔格式
        # 例如：
        # (3, 4)
        return f"({self.x}, {self.y})"

    # distance_to()：
    # Point 類別的方法（method）

    # method：
    # 定義在 class 裡面的函式

    # other：
    # 另一個 Point 物件
    def distance_to(self, other):

        # 計算兩點距離

        # 使用距離公式：
        # √((x1-x2)^2 + (y1-y2)^2)

        # ** 2：
        # 平方

        # ** 0.5：
        # 開根號
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


# 建立 Point 物件

# p1：
# x=0, y=0
p1 = Point(0, 0)

# p2：
# x=3, y=4
p2 = Point(3, 4)

# repr(p1)：
# 呼叫 __repr__()
print(repr(p1))             # Point(0, 0)

# str(p2)：
# 呼叫 __str__()
print(str(p2))              # (3, 4)

# 計算 p1 到 p2 的距離
# 結果：
# 5.0
print(p1.distance_to(p2))  # 5.0

# ── 類別變數 vs 實例變數 ──────────────────────────────────

# Student 類別
class Student:

    # school：
    # 類別變數（class variable）

    # 所有 Student 物件共用同一份資料
    school = "國立澎湖科技大學"    # 類別變數：所有實例共用

    # 建構子
    def __init__(self, name, student_id):

        # self.name：
        # 每個學生自己的名字

        # self.student_id：
        # 每個學生自己的學號

        # 這些是：
        # 實例變數（instance variable）

        # 每個物件都會有自己獨立的值
        self.name = name            # 實例變數：每個實例獨立
        self.student_id = student_id

    # __repr__()：
    # 開發者用的物件表示方式
    def __repr__(self):

        # 回傳：
        # Student(11144050001, 王小明)
        return f"Student({self.student_id}, {self.name})"

    # greeting()：
    # Student 類別的方法
    def greeting(self):

        # self.school：
        # 先找實例變數

        # 如果沒有：
        # 再找類別變數

        # 這裡 school 是類別變數
        return f"我是 {self.school} 的 {self.name}"


# 建立 Student 物件
s1 = Student("王小明", "11144050001")
s2 = Student("李小華", "11144050002")

# 呼叫 greeting() 方法
print(s1.greeting())

# 透過實例存取類別變數
# Python 會自動到 class 找 school
print(s2.school)            # 透過實例存取類別變數

# 直接透過類別名稱存取類別變數
print(Student.school)       # 透過類別名稱存取

# 修改類別變數影響所有實例

# 修改 Student 類別的 school
Student.school = "NPU"

# 因為是共用的類別變數
# 所以所有物件都會改變
print(s1.school)            # NPU
print(s2.school)            # NPU