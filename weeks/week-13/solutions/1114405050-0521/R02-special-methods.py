# R02. 物件特殊方法
# 讓自訂的 class 表現得像 Python 內建型別
# 對應 Bloom's Taxonomy：記憶（Remember）— 背得出哪個場景用哪個方法

# ── __repr__ 和 __str__：物件的自我介紹 ──────────────────
# __repr__：給「開發者」看的（在 REPL、debug 時出現）
# __str__ ：給「使用者」看的（print() 優先用這個）

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __repr__(self):
        """回傳一段可以「重現」這個物件狀態的字串，通常供開發者除錯用（如使用 repr()）"""
        return f"Student(name={self.name!r}, grade={self.grade})"

    def __str__(self):
        """回傳一段對人類友善、容易閱讀的字串，供 print() 或 str() 呼叫時顯示"""
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
        """自訂「相等 (==)」的比較邏輯"""
        # 如果拿來比較的對象根本不是 Point 類別，回傳 NotImplemented 讓 Python 處理
        if not isinstance(other, Point):
            return NotImplemented
        # 只要 x 和 y 座標一樣，我們就認定這兩個 Point 物件是相等的
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
        return f"Score({self.value})"

    def __eq__(self, other):
        """定義什麼情況下兩個分數會相等 (==)"""
        return self.value == other.value

    def __lt__(self, other):
        """定義什麼情況下這個分數會小於 (<) 另一個分數"""
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
# 一般 class 每個物件都有一個 __dict__，很耗記憶體
# CPE 題目有時會建立幾十萬個小物件，__slots__ 可以大幅節省

class PointLite:
    # 宣告 __slots__ 後，Python 不會為每個物件建立字典 (__dict__)，藉此大幅節省記憶體，但也限制了只能有這裡定義的屬性
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
