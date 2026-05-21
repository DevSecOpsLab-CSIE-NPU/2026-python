"""
R02. 物件特殊方法（Special Methods）範例

說明：展示如何透過 Python 的特殊方法讓自訂類別表現得更像內建型別，
包含 `__repr__`、`__str__`、`__eq__`、比較運算、`__slots__` 等常見用法。
每個範例皆附上繁體中文說明，方便教學或作業使用。
"""

# ── __repr__ 與 __str__：物件的自我介紹 ────────────────────
# - __repr__：提供給開發者（debug、REPL）用，理想上可用來重建物件
# - __str__ ：提供給最終使用者（print）看的可讀字串

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    """簡單的學生類別範例，示範 `__repr__` 與 `__str__` 的差別。"""

    def __repr__(self):
        """回傳可用於除錯的精確描述字串，包含類別與建構參數。

        慣例上 `__repr__` 的輸出應盡可能包含足夠資訊來重建或辨認物件。
        """
        return f"Student(name={self.name!r}, grade={self.grade})"

    def __str__(self):
        """回傳給使用者看的可讀字串，為較友善的顯示格式。"""
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
        """回傳座標的簡短描述，例如 Point(1, 2)。"""
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        """定義兩個 Point 是否視為相等：當且僅當 x 與 y 都相等。

        若 other 不是 Point，回傳 NotImplemented 讓 Python 嘗試其他比較方法。
        """
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
# @total_ordering 會自動補出 <=, >, >= 四個

from functools import total_ordering

@total_ordering
class Score:
    def __init__(self, value):
        self.value = value
    """示範可比較的類別：只需實作 `__eq__` 與一個比較方法（本文為 `__lt__`），
    `@total_ordering` 會自動補齊其他比較運算子。"""

    def __repr__(self):
        """回傳易讀的表示法，例如 Score(80)。"""
        return f"Score({self.value})"

    def __eq__(self, other):
        """判斷相等：當 value 相等時視為相等。"""
        return self.value == other.value

    def __lt__(self, other):
        """小於比較：以 value 作為比較依據。"""
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
    """輕量化的 Point 實作，透過 `__slots__` 限制可用屬性來節省記憶體。

    使用 `__slots__` 會避免每個實例建立 `__dict__`，因此在建立大量小物件時能顯著
    減少記憶體用量。但代價是不能動態新增不在 `__slots__` 中的屬性。
    """

    __slots__ = ('x', 'y')   # 僅允許這兩個屬性

    def __init__(self, x, y):
        self.x = x
        self.y = y

print("\n=== __slots__：固定屬性，節省記憶體 ===")
p = PointLite(3, 4)
print(p.x, p.y)   # 3 4
# p.z = 5  # 這行會 AttributeError，因為 z 不在 __slots__ 裡

# 記憶重點 ──────────────────────────────────────────────────
# - `__repr__`：給開發者（debug/REPL）用，應包含重建物件的資訊
# - `__str__`：給使用者看的友善字串，print() 會優先使用
# - `__eq__`：定義物件何時視為相等（預設為同一記憶體位置才相等）
# - `@total_ordering`：只要實作 `__eq__` 與一個比較（如 `__lt__`），即可自動生成其他比較運算子
# - `__slots__`：限制可用屬性並省略 `__dict__`，在大量物件時節省記憶體，但不可動態新增屬性
