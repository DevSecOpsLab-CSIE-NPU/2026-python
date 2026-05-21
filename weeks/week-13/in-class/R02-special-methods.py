# R02. 物件特殊方法（Special Methods / Dunder Methods）
# 範例與說明（繁體中文）：
# Python 的許多內建運作（印出、比較、排序、取長度、成員檢查）都靠特殊方法（以 __ 開頭與結尾），
# 實作這些方法可以讓自訂 class 行為更貼近內建型別，並改善除錯可讀性與 API 體驗。
# 常見用途：
# - __repr__/__str__：物件的文字描述（開發者 vs 使用者）
# - __eq__/比較：自訂相等與排序邏輯
# - __slots__：大量小物件時節省記憶體
# 本檔示範典型方法與設計建議。

# ── __repr__ 和 __str__：物件的自我介紹 ──────────────────
# __repr__：給「開發者」看的（在 REPL、debug 時出現）
# __str__ ：給「使用者」看的（print() 優先用這個）

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __repr__(self):
        # __repr__ 應該回傳一個「可重現」(or 明確) 的字串，方便開發與 debug。
        # 使用 !r 可以呼叫屬性的 repr，讓字串更精確（例如在 name 中有特殊字元時）。
        return f"Student(name={self.name!r}, grade={self.grade})"

    def __str__(self):
        # __str__ 提供給使用者閱讀的友善字串，通常較簡潔。
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
        # 若 other 不是 Point，回傳 NotImplemented，
        # 讓 Python 有機會嘗試對方的 __eq__ 或回退到預設行為。
        if not isinstance(other, Point):
            return NotImplemented
        # 若型別相同，逐欄位比較以定義「相等」的語意
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
        # 簡單示範：假設 other 也是 Score，直接比較 value
        if not isinstance(other, Score):
            return NotImplemented
        return self.value == other.value

    def __lt__(self, other):
        if not isinstance(other, Score):
            return NotImplemented
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
    __slots__ = ('x', 'y')   # 固定只有這兩個屬性

    def __init__(self, x, y):
        self.x = x
        self.y = y

print("\n=== __slots__：固定屬性，節省記憶體 ===")
p = PointLite(3, 4)
print(p.x, p.y)   # 3 4
# p.z = 5  # 這行會 AttributeError，因為 z 不在 __slots__ 裡

# 記憶重點 ──────────────────────────────────────────────────
# - __repr__  → 開發者用，應該盡可能提供可重建或精確資訊（方便 debug）
# - __str__   → 使用者用，提供友善易讀的格式，print() 優先使用
# - __eq__    → 定義相等語意；對不同型別回傳 NotImplemented 是良好習慣
# - 實作比較時：先檢查型別再回傳 NotImplemented，可避免不合理比較結果
# - @total_ordering：只要定義 __eq__ 和 任一比較（例如 __lt__），會自動補齊其餘比較運算
# - __slots__ → 限制物件可用屬性、移除 __dict__，在建立大量小物件時可節省記憶體
# - 設計建議：實作特殊方法時要考量型別安全（isinstance 檢查）與對稱性（返回 NotImplemented），
#   並盡量以可讀性與預期語意為主，避免把副作用或大量計算放進 __repr__/__str__。
