# R02. 物件特殊方法 (Special/Magic Methods)
# 讓自訂的類別 (class) 表現得像 Python 內建型別（如數字、字串或列表）。
# 對應 Bloom's Taxonomy：記憶 (Remember) — 能背得出在什麼場景下該使用哪個魔術方法。

# ── __repr__ 和 __str__：物件的自我介紹 ──────────────────
# __repr__：給「開發者」看的（目標是明確，常在 REPL、debug 或串列輸出時出現）。
# __str__ ：給「一般使用者」看的（目標是易讀，print() 或 str() 會優先使用）。

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __repr__(self):
        # !r 代表呼叫該屬性的 repr()，會自動加上引號
        return f"Student(name={self.name!r}, grade={self.grade})"

    def __str__(self):
        return f"{self.name}：{self.grade} 分"

print("=== __repr__ vs __str__ ===")
s = Student("王小明", 85)
print(f"repr() 結果：{repr(s)}")   # Student(name='王小明', grade=85)
print(f"str() 結果：{str(s)}")     # 王小明：85 分
print(f"直接 print：{s}")         # 王小明：85 分（print 優先使用 __str__）

# ── __eq__：自訂「相等」的意義 ────────────────────────────
# 預設情況下，兩個物件只有「位於同一個記憶體位置」才算相等 (is)。
# 透過 __eq__，我們可以定義只要「內容相同」就視為相等。

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        # 先檢查對方是不是也是 Point 類別
        if not isinstance(other, Point):
            return NotImplemented
        # 只要 x 和 y 座標都相同，就回傳 True
        return self.x == other.x and self.y == other.y

print("\n=== __eq__：自訂相等條件 ===")
p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(3, 4)
print(f"p1 == p2 ? {p1 == p2}")  # True（座標相同，邏輯上相等）
print(f"p1 == p3 ? {p1 == p3}")  # False
print(f"p1 is p2 ? {p1 is p2}")  # False（是不同的物件實例，記憶體位置不同）

# ── @total_ordering：自動補齊所有比較運算子 ─────────────
# 撰寫比較邏輯很繁瑣 (<, <=, >, >=)。
# 只要定義了 __eq__ 和其中一個比較方法（如 __lt__），
# 使用 @total_ordering 裝飾器就能自動生成其他的運算子。

from functools import total_ordering

@total_ordering
class Score:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Score({self.value})"

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        # 定義「小於」的邏輯
        return self.value < other.value

print("\n=== @total_ordering：自動補齊比較運算子 ===")
a = Score(80)
b = Score(90)
print(f"a < b  ? {a < b}")   # True
print(f"a > b  ? {a > b}")   # False（自動推導出結果）
print(f"a <= b ? {a <= b}")  # True（自動推導出結果）

# 因為定義了小於，排序功能也能直接運作
scores = [Score(70), Score(95), Score(60)]
print(f"排序結果：{sorted(scores)}")  # [Score(60), Score(70), Score(95)]

# ── __slots__：大量物件時節省記憶體 ──────────────────────
# 一般的類別會用一個字典 (__dict__) 來儲存屬性，這在物件非常多時會佔用大量記憶體。
# CPE 題目或資料處理若需要建立幾十萬個小物件，使用 __slots__ 可以大幅節省空間。

class PointLite:
    # 限制該類別只能有這兩個屬性，不再建立 __dict__
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

print("\n=== __slots__：固定屬性，效能優化 ===")
p = PointLite(3, 4)
print(f"座標：({p.x}, {p.y})")
# 注意：使用 __slots__ 後，不能再動態新增屬性
# p.z = 5  # 這行會報 AttributeError

# 記憶重點 ──────────────────────────────────────────────────
# 1. __repr__  → 開發者偵錯用，字串通常可以用來重建該物件。
# 2. __str__   → 給終端使用者看，以閱讀友善為主。
# 3. __eq__    → 定義 == 的比較邏輯。
# 4. @total_ordering + __lt__ → 輕鬆實作完整的數值比較。
# 5. __slots__ → 固定屬性，在處理巨量小型物件時是省記憶體的神器。
