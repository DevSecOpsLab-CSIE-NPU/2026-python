# R04. 特殊方法（8.2–8.3）
# __eq__ / __lt__ / __len__ / __contains__ / __iter__

from functools import total_ordering

# ── @total_ordering：只需定義 __eq__ 和一個比較方法 ──────
# 【詳解】
# 完整比較需要 6 個方法（==、!=、<、<=、>、>=），太繁瑣。
# @total_ordering 自動補全：只需定義 __eq__ 和 __lt__，
# 其他方法（__gt__, __le__ 等）自動推導。
# 比較邏輯放在 __lt__ 就好，如 self.value < other.value。
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
# 【詳解】
# 定義這些特殊方法，讓自訂類別支援：
# len(obj) → __len__
# x in obj → __contains__
# for x in obj → __iter__（需回傳 iterator）
# 這些方法讓類別像內建容器（list、dict）一樣好用。
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
