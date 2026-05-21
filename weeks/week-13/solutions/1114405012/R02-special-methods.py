# R02. 物件特殊方法
#
# 本範例說明如何實作與使用 Python 的特殊方法（magic / dunder methods），以讓自訂
# 類別在印出、比較、排序或大量建立時表現得更像內建型別。重點包含：
#  - `__repr__` / `__str__`：物件的字串表示
#  - `__eq__`：自訂相等性判斷
#  - `@total_ordering`：只需實作部分比較方法即可自動補齊其他比較運算子
#  - `__slots__`：在大量物件時節省記憶體

# ── __repr__ 和 __str__：物件的自我介紹 ──────────────────
# __repr__：給「開發者」看的（在 REPL、debug 時出現）
# __str__ ：給「使用者」看的（print() 優先用這個）

class Student:
    """簡單的學生類別，示範 `__repr__` 與 `__str__` 的差別。

    - `__repr__` 應回傳對開發者友好的字串（通常可用於重建物件）；
    - `__str__` 提供給終端使用者更易讀的描述，`print()` 會優先使用 `__str__`。
    """

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __repr__(self):
        # 可用於 debug 或 REPL，建議輸出能幫助重建物件的資訊
        return f"Student(name={self.name!r}, grade={self.grade})"

    def __str__(self):
        # 提供用戶友好的顯示文字
        return f"{self.name}：{self.grade} 分"

print("=== __repr__ vs __str__ ===")
s = Student("王小明", 85)
print(repr(s))   # Student(name='王小明', grade=85)
print(str(s))    # 王小明：85 分
print(s)         # 王小明：85 分（print 優先用 __str__）

# ── __eq__：自訂「相等」的意義 ────────────────────────────
# 沒有 __eq__ 的話，兩個物件只有「同一個記憶體位置」才算相等

class Point:
    """二維座標點，示範自訂 `__eq__` 以改變 == 的語意。

    注意：若其他物件不是 Point，應回傳 `NotImplemented`，讓 Python 去嘗試反向比較或回傳 False。
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
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
    """示範使用 `@total_ordering`：只需定義 `__eq__` 與一個比較運算（例如 `__lt__`），
    decorators 會自動補齊其他比較方法（`__le__`, `__gt__`, `__ge__`）。
    """

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Score({self.value})"

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
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
    """使用 `__slots__` 的精簡座標物件：

    - 一般 Python 物件會有 `__dict__`，可動態新增屬性，但會佔用較多記憶體；
    - 當物件數量很多（例如數十萬個小物件）且屬性固定時，使用 `__slots__` 可大幅節省記憶體。
    """
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
