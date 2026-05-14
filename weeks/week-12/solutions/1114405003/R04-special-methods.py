# R04. 特殊方法（8.2–8.3）
# 主題：`__eq__` / `__lt__` / `__len__` / `__contains__` / `__iter__`
# 註解語言：繁體中文（臺灣 zh-TW），並把第一個範例改成 Point 類別

from functools import total_ordering

# ── @total_ordering：只需定義 `__eq__` 和一個比較方法 ──────
# 這個裝飾器可以幫我們補齊其餘比較運算子，像是 `>`, `>=`, `<=`。
# 只要我們定義好 `__eq__` 與 `__lt__`，Python 就能推導出其他比較結果。
@total_ordering
class Point:
    # 這裡把原本的 Score 改成 Point，讓 `other` 參數也明確是另一個 Point 物件。
    # 同時加入更多實例變數，例如 label 與 color，讓物件更完整。
    def __init__(self, x, y, label="", color="black"):
        self.x = x
        self.y = y
        self.label = label
        self.color = color

    # `__repr__` 主要給開發者看，理想情況下要足夠完整，能看出物件內容。
    def __repr__(self):
        return f"Point({self.x}, {self.y}, label={self.label!r}, color={self.color!r})"

    # `__str__` 主要給使用者看，格式可以比較簡潔、易讀。
    def __str__(self):
        if self.label:
            return f"[{self.label}] ({self.x}, {self.y}) - {self.color}"
        return f"({self.x}, {self.y})"

    # `__eq__`：定義「是否相等」
    # 這裡我們比較座標與標籤，代表兩個 Point 只有在位置與標籤都一致時才算相等。
    # 如果 `other` 不是 Point，就回傳 NotImplemented，讓 Python 交給其他機制處理。
    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return (self.x, self.y, self.label, self.color) == (other.x, other.y, other.label, other.color)

    # `__lt__`：定義「小於」
    # 這裡採用「先比 x，再比 y」的排序規則。
    # `other` 是另一個 Point 物件，因此這正符合你要的「other 是 Point class」。
    def __lt__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return (self.x, self.y) < (other.x, other.y)

    # 這裡補一個常見的實例方法：計算兩點距離。
    def distance_to(self, other):
        if not isinstance(other, Point):
            raise TypeError("other 必須是 Point 類別")
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


# 建立幾個 Point 實例
p1 = Point(0, 0, label="原點", color="black")
p2 = Point(3, 4, label="A 點", color="red")
p3 = Point(3, 4, label="A 點", color="red")
p4 = Point(1, 8, label="B 點", color="blue")

print("=== Point 範例 ===")
print(repr(p1))
print(str(p2))
print(p1.distance_to(p2))

# 比較運算示範
print("\n=== 比較運算 ===")
print(p2 == p3)      # True
print(p1 == p2)      # False
print(p1 < p2)       # True
print(p2 > p1)       # True（由 @total_ordering 推導）
print(sorted([p2, p4, p1, p3]))

# ── __len__ / __contains__ / __iter__ ────────────────────
# 第二段保留原本的容器型特殊方法示範。
# 這裡把容器改成存放 Point 物件，剛好可以和前面的 Point 類別串在一起。
class Classroom:
    def __init__(self, name):
        self.name = name
        self._students = []

    def add(self, student):
        # 這裡允許加入字串或 Point 物件，方便展示 `__contains__` 與 `__iter__`。
        self._students.append(student)

    def __len__(self):
        return len(self._students)

    def __contains__(self, student):
        return student in self._students

    def __iter__(self):
        return iter(self._students)

    def __repr__(self):
        return f"Classroom({self.name!r}, {len(self)} 人)"


cls = Classroom("資工一甲")
cls.add(p1)
cls.add(p2)
cls.add(p4)

print("\n=== Classroom 範例 ===")
print(len(cls))             # 3
print(p2 in cls)            # True
print(Point(9, 9) in cls)   # False

for point in cls:           # `__iter__` 讓 for 迴圈可用
    print(point)

# ── 常見提醒 ─────────────────────────────────────────────
# - `__eq__` 與 `__lt__` 的 `other`，通常就是「同一類別的另一個物件」。
# - 如果 `other` 不是同類別，回傳 `NotImplemented` 比直接回傳 False 更符合 Python 慣例。
# - `@total_ordering` 很適合只想寫少數比較方法，但仍希望支援完整排序的情境。
# - `__len__` 讓 `len(obj)` 可用，`__contains__` 讓 `x in obj` 可用，`__iter__` 讓 `for x in obj` 可用。
# - 這些特殊方法能讓自訂類別「更像內建型別」，使用起來更直覺。
