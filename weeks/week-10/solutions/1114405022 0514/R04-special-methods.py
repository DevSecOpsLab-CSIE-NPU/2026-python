# R04. 特殊方法（8.2–8.3）
# 本範例示範「魔術方法」（dunder methods）如何讓自訂類別行為更像內建型別：
# - 比較運算：`__eq__`、`__lt__`
# - 容器協議：`__len__`、`__contains__`、`__iter__`
# 這些方法會被 Python 自動呼叫，讓你可使用 `==`, `<`, `in`, `len()`, `for` 等語法。

from functools import total_ordering


# ── @total_ordering：只需定義 __eq__ + 一個大小比較 ─────────────
# `@total_ordering` 是標準庫裝飾器：
# 若你提供 `__eq__` 和其中一個排序方法（如 `__lt__`），
# 它會自動補上 `__le__`、`__gt__`、`__ge__` 等其餘比較方法。
@total_ordering
class Score:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        # `!r` 會使用 repr() 呈現字串，適合 debug
        return f"Score({self.name!r}, {self.value})"

    def __eq__(self, other):
        # 比較前先做型別檢查：
        # 若不是 Score，回傳 NotImplemented，交由 Python 嘗試反向比較
        if not isinstance(other, Score):
            return NotImplemented
        # 此範例以分數 value 作為相等標準（name 不納入）
        return self.value == other.value

    def __lt__(self, other):
        if not isinstance(other, Score):
            return NotImplemented
        # 小於比較：僅比 value
        return self.value < other.value


# 建立三個成績物件
s1 = Score("Alice", 90)
s2 = Score("Bob", 75)
s3 = Score("Carol", 90)

# `s1 > s2` 會由 total_ordering 根據 __lt__/__eq__ 推導
print(s1 > s2)      # True
print(s1 == s3)     # True（value 同為 90）
print(s1 != s2)     # True（由 __eq__ 推導）
print(sorted([s1, s2, s3]))     # 依 value 升冪排列


# ── 容器協議：__len__ / __contains__ / __iter__ ─────────────
class Classroom:
    def __init__(self, name):
        self.name = name
        self._students = []

    def add(self, student):
        # 封裝新增操作，避免外部直接改內部 list
        self._students.append(student)

    def __len__(self):
        # 讓 len(classroom) 可用
        return len(self._students)

    def __contains__(self, student):
        # 讓 "Alice" in classroom 可用
        return student in self._students

    def __iter__(self):
        # 讓 for student in classroom 可用
        # 回傳一個 iterator（此處直接使用 list 的 iterator）
        return iter(self._students)

    def __repr__(self):
        # 使用 len(self) 可重用 __len__ 邏輯
        return f"Classroom({self.name!r}, {len(self)} 人)"


cls = Classroom("資工一甲")
cls.add("Alice")
cls.add("Bob")
cls.add("Carol")

print(len(cls))             # 3
print("Alice" in cls)       # True
print("Dave" in cls)        # False

for student in cls:         # __iter__ 讓 for 迴圈可用
    print(student)
