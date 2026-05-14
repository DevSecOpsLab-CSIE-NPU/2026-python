"""R04. 特殊方法（8.2–8.3）

說明（繁體中文詳細註解）：
- 特殊方法（magic methods / dunder methods）可讓自訂類別支援 Python 的運算子、內建函式與迭代協定。
- 例如：`__eq__` 控制 `==`，`__lt__` 控制 `<`，`__len__` 控制 `len()`，`__contains__` 控制 `in`，`__iter__` 控制 `for`。
- `functools.total_ordering` 可以在你只實作 `__eq__` 和一個比較方法（例如 `__lt__`）後，自動補齊其他比較運算。
"""

from functools import total_ordering


# total_ordering：只需定義 __eq__ 和一個比較方法，其他比較方法會自動推導
@total_ordering
class Score:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"Score({self.name!r}, {self.value})"

    def __eq__(self, other):
        # 遇到不同型別時回傳 NotImplemented，讓 Python 決定如何處理
        if not isinstance(other, Score):
            return NotImplemented
        return self.value == other.value

    def __lt__(self, other):
        if not isinstance(other, Score):
            return NotImplemented
        return self.value < other.value


s1 = Score("Alice", 90)
s2 = Score("Bob", 75)
s3 = Score("Carol", 90)

print(s1 > s2)      # True  （由 total_ordering + __lt__ 推導）
print(s1 == s3)     # True
print(s1 != s2)     # True  （由 __eq__ 推導）
print(sorted([s1, s2, s3]))     # 升冪排列


# __len__ / __contains__ / __iter__：讓自訂類別像內建容器一樣可用
class Classroom:
    def __init__(self, name):
        self.name = name
        self._students = []

    def add(self, student):
        self._students.append(student)

    def __len__(self):
        return len(self._students)

    def __contains__(self, student):
        return student in self._students

    def __iter__(self):
        # 回傳 iterator，使得 for student in cls 可以正常運作
        return iter(self._students)

    def __repr__(self):
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
