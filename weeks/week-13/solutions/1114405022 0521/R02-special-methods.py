# R02. 物件特殊方法
# 讓自訂的 class 表現得像 Python 內建型別
# 對應 Bloom's Taxonomy：記憶（Remember）— 背得出哪個場景用哪個方法

# ── __repr__ 和 __str__：物件的自我介紹 ──────────────────
# __repr__：給「開發者」看的（在 REPL、debug 時出現）
# __str__ ：給「使用者」看的（print() 優先用這個）

class Student:
    """示範 __repr__ 和 __str__ 的差異"""

    def __init__(self, name, grade):
        """建構子：初始化學生的姓名和成績"""
        self.name = name    # 設定姓名屬性
        self.grade = grade  # 設定成績屬性

    def __repr__(self):
        """
        正式的字串表示法（開發者導向）
        !r 表示用 repr() 來格式化 name，這樣字串會加上引號
        理想上 __repr__ 回傳的字串應該能用 eval() 重建物件
        """
        return f"Student(name={self.name!r}, grade={self.grade})"

    def __str__(self):
        """
        非正式的字串表示法（使用者導向）
        print() 和 str() 會優先呼叫這個方法
        """
        return f"{self.name}：{self.grade} 分"

print("=== __repr__ vs __str__ ===")
s = Student("王小明", 85)     # 建立 Student 物件
print(repr(s))   # 呼叫 __repr__：Student(name='王小明', grade=85)
print(str(s))    # 呼叫 __str__：王小明：85 分
print(s)         # print 優先用 __str__，所以也是：王小明：85 分

# ── __eq__：自訂「相等」的意義 ────────────────────────────
# 沒有 __eq__ 的話，兩個物件只有「同一個記憶體位置」才算相等

class Point:
    """二維座標點，示範自訂相等判斷"""

    def __init__(self, x, y):
        """建構子：初始化 x, y 座標"""
        self.x = x  # x 軸座標
        self.y = y  # y 軸座標

    def __repr__(self):
        """開發者導向的字串表示"""
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        """
        自訂 == 的判斷邏輯
        如果 other 不是 Point 類型，回傳 NotImplemented（讓 Python 處理）
        否則比較兩個點的 x 和 y 座標是否都相同
        """
        if not isinstance(other, Point):  # 檢查 other 是否為 Point 實例
            return NotImplemented          # 不是的話回傳 NotImplemented
        return self.x == other.x and self.y == other.y  # 兩個座標都要相等

print("\n=== __eq__：自訂相等條件 ===")
p1 = Point(1, 2)     # 建立點 (1, 2)
p2 = Point(1, 2)     # 另一個點 (1, 2)
p3 = Point(3, 4)     # 另一個點 (3, 4)
print(p1 == p2)      # True（座標相同，所以相等）
print(p1 == p3)      # False（座標不同）
print(p1 is p2)      # False（是不同的物件，記憶體位置不同，但 == 可以是 True）

# ── @total_ordering：自動補齊所有比較運算子 ─────────────
# 只要定義 __eq__ 和一個比較（__lt__），
# @total_ordering 會自動補出 <=, >, >= 四個

from functools import total_ordering  # 匯入自動補齊比較運算子的裝飾器

@total_ordering  # 自動根據 __eq__ 和 __lt__ 產生 __le__, __gt__, __ge__
class Score:
    """成績類別，讓成績可以互相比較大小"""

    def __init__(self, value):
        """建構子：設定成績數值"""
        self.value = value  # 儲存成績分數

    def __repr__(self):
        """開發者導向的字串表示"""
        return f"Score({self.value})"

    def __eq__(self, other):
        """判斷兩個 Score 是否相等（比較數值）"""
        return self.value == other.value

    def __lt__(self, other):
        """判斷 self 是否小於 other（小於運算子 <）"""
        return self.value < other.value

    # @total_ordering 會自動生成：
    # __le__ : <=（小於或等於）
    # __gt__ : >（大於）
    # __ge__ : >=（大於或等於）

print("\n=== @total_ordering：只寫兩個，自動補齊全部 ===")
a = Score(80)      # 建立 Score(80)
b = Score(90)      # 建立 Score(90)
print(a < b)       # True（80 < 90，使用 __lt__）
print(a > b)       # False（自動生成 __gt__，80 不大於 90）
print(a <= b)      # True（自動生成 __le__，80 小於等於 90）

scores = [Score(70), Score(95), Score(60)]  # 三個 Score 物件的列表
print(sorted(scores))  # sorted 會使用 __lt__ 來排序：[Score(60), Score(70), Score(95)]

# ── __slots__：大量物件時節省記憶體 ──────────────────────
# 一般 class 每個物件都有一個 __dict__，很耗記憶體
# CPE 題目有時會建立幾十萬個小物件，__slots__ 可以大幅節省

class PointLite:
    """
    使用 __slots__ 的輕量級座標點
    __slots__ 告訴 Python 這個 class 只有固定的屬性名稱，
    因此不需要為每個物件建立 __dict__，大幅節省記憶體
    """
    __slots__ = ('x', 'y')   # 固定只能有 x 和 y 這兩個屬性

    def __init__(self, x, y):
        self.x = x  # 設定 x 座標
        self.y = y  # 設定 y 座標

print("\n=== __slots__：固定屬性，節省記憶體 ===")
p = PointLite(3, 4)   # 建立輕量級點物件
print(p.x, p.y)       # 輸出 3 4（可以正常存取 x 和 y）
# p.z = 5  # 這行會 AttributeError，因為 z 不在 __slots__ 裡

# 記憶重點 ──────────────────────────────────────────────────
# __repr__  → 開發者用，要能「重現」物件
# __str__   → 使用者用，print() 呼叫
# __eq__    → 自訂 == 的意義
# @total_ordering + __lt__ → 自動補齊 <, <=, >, >=
# __slots__ → 固定屬性，大量物件時省記憶體
