# R02. 物件特殊方法
# 讓自訂的 class 表現得像 Python 內建型別
# 對應 Bloom's Taxonomy：記憶（Remember）— 背得出哪個場景用哪個方法
#
# Python 的特殊方法又稱「魔法方法（magic methods）」或「dunder methods」。
# 定義它們就能讓你的自訂類別支援補鑑符號、len()、for 迴圈等內建操作。

# ── __repr__ 和 __str__：物件的自我介紹 ──────────────────
# __repr__：給「開發者」看的（在 REPL、debug 時出現）
# __str__ ：給「使用者」看的（print() 優先用這個）

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __repr__(self):
        # repr 的輸出最好能「重建」物件，方便 debug
        return f"Student(name={self.name!r}, grade={self.grade})"

    def __str__(self):
        # str 是給一般使用者看的簡潔格式
        return f"{self.name}：{self.grade} 分"

print("=== __repr__ vs __str__ ===")
s = Student("王小明", 85)
print(repr(s))   # Student(name='王小明', grade=85)
print(str(s))    # 王小明：85 分
print(s)         # 王小明：85 分（print 優先用 __str__）

# ── __eq__：自訂「相等」的意義 ────────────────────────────
# 沒有 __eq__ 的話，兩個物件只有「同一個記憶體位置」才算相等

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        # 先檢查對方是不是 Point，不是的話回傳 NotImplemented
        # 讓 Python 轉而詢問另一方，避免預期外的 False
        if not isinstance(other, Point):
            return NotImplemented
        # 座標相同才算相等，不用管是不是同一個物件
        return self.x == other.x and self.y == other.y

print("\n=== __eq__：自訂相等條件 ===")
p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(3, 4)
print(p1 == p2)  # True（座標相同）
print(p1 == p3)  # False
print(p1 is p2)  # False（是不同的物件，記憶體位置不同）

# ── @total_ordering：自動補齊所有比較運算子 ─────────────
# 只要定義 __eq__ 和一個比較（__lt__），
# @total_ordering 會自動補出 <=, >, >= 四個

from functools import total_ordering

@total_ordering
class Score:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        # 兩者分數相同則相等
        return self.value == other.value

    def __lt__(self, other):
        # 只需定義 <，@total_ordering 會自動推導 >、<=、>=
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

print("\n=== @total_ordering：只寫兩個，自動補齊全部 ===")
a = Score(80)  — 呼叫 __lt__
print(a > b)   # False — 自動生成（由 __lt__ 推導）
print(a <= b)  # True  — 自動生成
print(a > b)   # False（自動生成）
print(a <= b)  # True（自動生成）

scores = [Score(70), Score(95), Score(60)]
print(sorted(scores))  # [Score(60), Score(70), Score(95)]

# ── __slots__：大量物件時節省記憶體 ──────────────────────
# 一般 class 每個物件都有一個 __dict__，很耗記憶體
# CPE 題目有時會建立幾十萬個小物件，__slots__ 可以大幅節省

class PointLite:
    # __slots__ = ('x', 'y') 表示這個 class 的物件「只能有 x 和 y 兩個屬性」
    # 沒有 __dict__，記憶體佔用比一般 class 小很多
    __slots__ = ('x', 'y')   # 固定只有這兩個屬性

    def __init__(self, x, y):
        self.x = x
        self.y = y

print("\n=== __slots__：固定屬性，節省記憶體 ===")
p = PointLite(3, 4)
print(p.x, p.y)   # 3 4
# p.z = 5  # 這行會 AttributeError，因為 z 不在 __slots__ 裡

# 記憶重點 ──────────────────────────────────────────────────
# __repr__  → 開發者用，要能「重現」物件
# __str__   → 使用者用，print() 呼叫
# __eq__    → 自訂 == 的意義
# @total_ordering + __lt__ → 自動補齊 <, <=, >, >=
# __slots__ → 固定屬性，大量物件時省記憶體
