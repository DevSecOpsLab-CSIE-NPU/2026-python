# R01. 類別基礎（8.1）
# 主題：`__init__` / 方法定義 / `__repr__` / `__str__` 的基本使用
# 註解語言：繁體中文（臺灣 zh-TW），並補充物件導向設計重點

# ── 最簡單的 class ────────────────────────────────────────
# 定義一個 `Point` 類別，用來表示二維平面上的一個點。
# 這是最基本的物件導向程式設計示例。
class Point:
    # `__init__` 是「初始化方法」（也稱為建構函式），
    # 當你用 `Point(...)` 建立新實例時，Python 會自動呼叫這個方法。
    # 第一個參數 `self` 代表新建立的實例本身，不需要在呼叫時傳入。
    def __init__(self, x, y, label="", color="black"):
        # `self.x` 與 `self.y` 是實例變數，
        # 每個 Point 實例都有自己的 x 與 y 值。
        self.x = x
        self.y = y
        # 新增實例變數：標籤與顏色，讓 Point 物件更豐富。
        # 這些參數有預設值，因此即使不傳入也不會出錯。
        self.label = label
        self.color = color

    # `__repr__()` 方法定義物件的「正式字串表示」（representation）。
    # 用於開發者除錯；理想情況下，`eval(repr(obj))` 能重建相同物件。
    # 當你在 REPL 或 IDE 直接輸入物件名稱時，會呼叫這個方法。
    def __repr__(self):
        if self.label:
            return f"Point({self.x}, {self.y}, label='{self.label}', color='{self.color}')"
        return f"Point({self.x}, {self.y})"

    # `__str__()` 方法定義物件的「非正式字串表示」（human-readable）。
    # 專為使用者看，`print()` 或 `str()` 時會呼叫這個方法。
    # 若 `__str__` 沒有定義，Python 會改用 `__repr__`。
    def __str__(self):
        if self.label:
            return f"[{self.label}] ({self.x}, {self.y}) - {self.color}"
        return f"({self.x}, {self.y})"

    # 自訂方法：計算該點到另一個點的距離。
    # 參數 `other` 也是 Point 實例，目的是讓我們存取它的 `x` 與 `y`。
    def distance_to(self, other):
        # 使用距離公式：sqrt((x1-x2)^2 + (y1-y2)^2)
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


# 建立兩個 Point 實例
# `p1 = Point(0, 0)` 會呼叫 `__init__`，並把 `self.x=0`, `self.y=0` 設好。
p1 = Point(0, 0, label="原點")
p2 = Point(3, 4, label="頂點", color="red")

# 呼叫 `__repr__`，顯示「正式」表示法
print(repr(p1))             # Point(0, 0, label='原點', color='black')

# 呼叫 `__str__`，顯示「簡潔」表示法
print(str(p2))              # [頂點] (3, 4) - red

# 呼叫自訂方法，計算兩點距離（應該是 5.0）
print(p1.distance_to(p2))  # 5.0

# ── 圓形類別 ──────────────────────────────────────────────
# 展示另一個幾何類別，內含不同的實例變數與方法。
class Circle:
    # 圓形由圓心（中心點）與半徑定義。
    def __init__(self, center_x, center_y, radius, name=""):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
        self.name = name

    def __repr__(self):
        return f"Circle(center=({self.center_x}, {self.center_y}), radius={self.radius})"

    def __str__(self):
        return f"圓形 {self.name} - 圓心 ({self.center_x}, {self.center_y})，半徑 {self.radius}"

    # 計算圓的面積
    def area(self):
        import math
        return math.pi * self.radius ** 2

    # 計算圓的周長
    def circumference(self):
        import math
        return 2 * math.pi * self.radius

    # 判斷某個點是否在圓內
    def contains_point(self, x, y):
        dist = ((x - self.center_x) ** 2 + (y - self.center_y) ** 2) ** 0.5
        return dist <= self.radius


c1 = Circle(0, 0, 5, "C1")
print("\n" + str(c1))
print(f"面積: {c1.area():.2f}")
print(f"周長: {c1.circumference():.2f}")
print(f"(0,0) 在圓內: {c1.contains_point(0, 0)}")
print(f"(4,4) 在圓內: {c1.contains_point(4, 4)}")

# ── 矩形類別 ──────────────────────────────────────────────
# 展示第三個幾何類別，進一步示範不同的設計方式。
class Rectangle:
    # 矩形由左上角座標、寬度與高度定義。
    def __init__(self, x, y, width, height, color="white"):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def __repr__(self):
        return f"Rectangle({self.x}, {self.y}, w={self.width}, h={self.height})"

    def __str__(self):
        return f"矩形 ({self.x}, {self.y}) 大小 {self.width}x{self.height} - {self.color}"

    # 計算矩形面積
    def area(self):
        return self.width * self.height

    # 計算矩形周長
    def perimeter(self):
        return 2 * (self.width + self.height)

    # 判斷某個點是否在矩形內
    def contains_point(self, x, y):
        return (self.x <= x <= self.x + self.width and 
                self.y <= y <= self.y + self.height)


rect1 = Rectangle(0, 0, 10, 5, "blue")
print("\n" + str(rect1))
print(f"面積: {rect1.area()}")
print(f"周長: {rect1.perimeter()}")
print(f"(5,2) 在矩形內: {rect1.contains_point(5, 2)}")
print(f"(12,3) 在矩形內: {rect1.contains_point(12, 3)}")

# ── 類別變數 vs 實例變數 ──────────────────────────────────
# 這段示範一個重要的物件導向概念：
# - 「類別變數」是所有實例共享的屬性（放在 class 層級）。
# - 「實例變數」是每個實例各自擁有的屬性（通常在 `__init__` 設定）。

class Student:
    # `school` 是類別變數：所有 Student 實例都共用這個值。
    # 它定義在 class 區塊中，不在任何方法內。
    # 所有學生都就讀同一個學校，所以這是合理的設計。
    school = "國立澎湖科技大學"

    def __init__(self, name, student_id):
        # `self.name` 與 `self.student_id` 是實例變數。
        # 每個學生有不同的名字和學號，因此放在 `__init__` 裡初始化。
        self.name = name
        self.student_id = student_id

    # `__repr__` 方法，用來表示每個學生實例
    def __repr__(self):
        return f"Student({self.student_id}, {self.name})"

    # 自訂方法：問候語
    # 這個方法同時使用了類別變數 `self.school` 與實例變數 `self.name`。
    def greeting(self):
        return f"我是 {self.school} 的 {self.name}"


# 建立兩個 Student 實例
s1 = Student("王小明", "11144050001")
s2 = Student("李小華", "11144050002")

# 呼叫問候方法
print(s1.greeting())

# 透過實例存取類別變數
# 雖然 `school` 是類別變數，但你可以用 `實例.school` 來存取。
print(s2.school)            # 國立澎湖科技大學

# 透過類別名稱直接存取類別變數（這是更明確的做法）
print(Student.school)       # 國立澎湖科技大學

# 修改類別變數會影響所有實例
# 這展示為什麼理解類別變數與實例變數的區別很重要。
Student.school = "NPU"
print(s1.school)            # NPU（s1 看到了變更）
print(s2.school)            # NPU（s2 也看到了變更）

# ── 常見提醒 ─────────────────────────────────────────────
# - `__init__` 負責初始化實例，`self` 代表正在建立的實例。
# - `__repr__` 給開發者看（除錯時用），`__str__` 給使用者看（print 時用）。
# - 方法內總是第一個參數是 `self`，代表呼叫該方法的實例本身。
# - 類別變數適合存放「所有實例都共同擁有」的資料；大多情況用實例變數更彈性。
# - `__repr__` 和 `__str__` 預設實現會給出類似 `<Point object at 0x...>` 的冗長訊息；
#   通常建議自訂這些方法來提供有意義的字串表示。
