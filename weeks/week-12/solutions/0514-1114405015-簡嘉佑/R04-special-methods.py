# R04. 特殊方法（8.2–8.3）
# __eq__ / __lt__ / __len__ / __contains__ / __iter__
#
# Python 的「魔法方法（magic methods）」又稱 dunder（double underscore）方法。
# 定義它們就能讓自訂類別支援補鑑符號、len()、for 迴圈等內建操作。

from functools import total_ordering

# ── @total_ordering：只需定義 __eq__ 和一個比較方法 ──────────
# @total_ordering 裝飾器會自動由 __eq__ 與 __lt__
# 推導出其餘四個比較方法（__gt__、__le__、__ge__、__ne__），大幅少寫重複程式碼。
@total_ordering
class Score:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"Score({self.name!r}, {self.value})"

    def __eq__(self, other):
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

print(s1 > s2)      # True  （由 __lt__ 推導）
print(s1 == s3)     # True
print(s1 != s2)     # True  （由 __eq__ 推導）
print(sorted([s1, s2, s3]))     # 升冪排列

# ── __len__ / __contains__ / __iter__ ────────────────────
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
