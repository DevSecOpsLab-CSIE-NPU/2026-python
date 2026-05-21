# R02. 物件特殊方法（Special Methods）
# 本檔說明常見的特殊方法，讓自訂類別在除錯、比較、排序與記憶體優化時行為更直觀。


# ---------- __repr__ 與 __str__：物件的字串表示 ----------
# - __repr__：給開發者看的（REPL、log）；通常應能以該輸出重建物件（或至少提供完整資訊）。
# - __str__：給使用者看的（print 使用），應該是較友善且易讀的格式。
class Student:
    """
    範例 Student 類別，示範 __repr__ 與 __str__ 的差別與用途。

    - __repr__ 應包含建構物件的必要資訊，方便除錯。
    - __str__ 提供對終端使用者較易讀的輸出格式。
    """

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __repr__(self):
        # 使用 !r 可以讓 name 以 repr 形式呈現（例如包含引號），有助於除錯
        return f"Student(name={self.name!r}, grade={self.grade})"

    def __str__(self):
        # 友善輸出，適合在介面或報表中顯示
        return f"{self.name}：{self.grade} 分"


print("=== __repr__ vs __str__ ===")
s = Student("王小明", 85)
print(repr(s))   # Student(name='王小明', grade=85)
print(str(s))    # 王小明：85 分
print(s)         # print 優先用 __str__


# ---------- __eq__：定義物件相等的語意 ----------
# 若不實作 __eq__，預設比較是物件位址（is）；實作後可定義更合理的相等判斷
class Point:
    """
    二維座標點範例，示範如何為物件定義相等性（==）。

    注意：若 other 不是同一型別，回傳 NotImplemented 是慣例，
    讓 Python 有機會嘗試其他對稱方法或回報 False。
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        # 只有當 x 與 y 都相等時，才視為相等
        return self.x == other.x and self.y == other.y


print("\n=== __eq__：自訂相等條件 ===")
p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(3, 4)
print(p1 == p2)  # True（座標相同）
print(p1 == p3)  # False
print(p1 is p2)  # False（不同物件實例）


# ---------- 使用 @total_ordering 自動補齊比較方法 ----------
# 定義 __eq__ 與 __lt__ 即可由 functools.total_ordering 幫忙產生其他比較方法
from functools import total_ordering


@total_ordering
class Score:
    """
    以數值作為比較依據的簡單類別範例。

    - 實作 __eq__ 與 __lt__ 後，@total_ordering 會提供 __le__, __gt__, __ge__。
    - 這對於排序與比較非常方便，避免手動實作多個方法時出錯。
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
print(sorted(scores))  # 會以 value 排序


# ---------- __slots__：在大量物件時節省記憶體 ----------
# 預設情況下，每個物件都有 __dict__，儲存屬性名稱與值，會佔較多記憶體。
# 若物件屬性固定且數量不多，可以透過 __slots__ 限制屬性集合並節省記憶體。
class PointLite:
    __slots__ = ('x', 'y')   # 限定該類別只允許 x, y 兩個屬性

    def __init__(self, x, y):
        self.x = x
        self.y = y


print("\n=== __slots__：固定屬性，節省記憶體 ===")
p = PointLite(3, 4)
print(p.x, p.y)   # 3 4
# 如果嘗試設定不在 __slots__ 的屬性，會得到 AttributeError
# p.z = 5  # 會拋出 AttributeError


# 記憶重點（快速參考）
# - __repr__  → 開發者用，應包含完整資訊以利除錯和重建物件
# - __str__   → 使用者用，較友善的字串表示
# - __eq__    → 自訂 == 的語意（對不同型別回傳 NotImplemented）
# - @total_ordering + __lt__ → 自動補齊其他比較運算子
# - __slots__ → 固定屬性清單，在建立大量物件時可以省下記憶體
