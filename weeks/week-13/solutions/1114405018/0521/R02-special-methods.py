# R02. 物件特殊方法
# 讓自訂的 class 表現得像 Python 內建型別，
# 例如可以直接 print、比較大小、排序，甚至節省記憶體。
# 對應 Bloom's Taxonomy：記憶（Remember）— 背得出哪個場景用哪個方法

# ── __repr__ 和 __str__：物件的自我介紹 ──────────────────
# __repr__：給「開發者」看的（在 REPL、debug 時出現）
# __str__ ：給「使用者」看的（print() 優先用這個）

class Student:
    def __init__(self, name, grade):
        # 建立學生物件時把名字與分數存進去
        self.name = name
        self.grade = grade

    def __repr__(self):
        # 給開發者看的版本，最好能看出如何重建這個物件
        return f"Student(name={self.name!r}, grade={self.grade})"

    def __str__(self):
        # 給使用者看的版本，通常要簡短、友善、易讀
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
        # Point 只負責記錄座標，不做額外邏輯
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        # 不是 Point 就交回 NotImplemented，讓 Python 決定後續比較行為
        if not isinstance(other, Point):
            return NotImplemented
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
# @total_ordering 就能自動補出 <=, >, >= 四個比較運算子。

from functools import total_ordering

@total_ordering
class Score:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Score({self.value})"

    def __eq__(self, other):
        # 這裡示範以分數值判斷相等
        return self.value == other.value

    def __lt__(self, other):
        # 只要能比較小於，其他比較就可由 total_ordering 補出來
        return self.value < other.value

print("\n=== @total_ordering：只寫兩個，自動補齊全部 ===")
a = Score(80)
b = Score(90)
print(a < b)   # True
print(a > b)   # False（自動生成）
print(a <= b)  # True（自動生成）

scores = [Score(70), Score(95), Score(60)]
print(sorted(scores))  # [Score(60), Score(70), Score(95)]

# ── __slots__：大量物件時節省記憶體 ──────────────────────
# 一般 class 每個物件都有一個 __dict__，會額外占用記憶體。
# CPE 題目有時會建立幾十萬個小物件，__slots__ 可以大幅節省空間。

class PointLite:
    # 限制這個類別只能有 x、y 兩個屬性，避免多開 __dict__
    __slots__ = ('x', 'y')

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
