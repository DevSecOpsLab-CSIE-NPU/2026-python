# R04. 特殊方法（8.2–8.3）
# __eq__ / __lt__ / __len__ / __contains__ / __iter__

from functools import total_ordering

# ── @total_ordering：只需定義 __eq__ 和一個比較方法 ──────
@total_ordering
class Score:
    def __init__(self, name, value):
        # 每筆成績記錄都保存名字與分數。
        self.name = name
        self.value = value

    def __repr__(self):
        # 讓物件在除錯或印出 list 時更容易辨識。
        return f"Score({self.name!r}, {self.value})"

    def __eq__(self, other):
        # __eq__ 定義「是否相等」的判斷規則。
        if not isinstance(other, Score):
            return NotImplemented
        return self.value == other.value

    def __lt__(self, other):
        # __lt__ 定義「小於」的比較方式，其他排序關係可由 total_ordering 推導。
        if not isinstance(other, Score):
            return NotImplemented
        return self.value < other.value


s1 = Score("Alice", 90)
s2 = Score("Bob", 75)
s3 = Score("Carol", 90)

# total_ordering 會根據 __eq__ 和 __lt__ 自動補齊其他比較運算。
print(s1 > s2)      # True  （由 __lt__ 推導）
print(s1 == s3)     # True
print(s1 != s2)     # True  （由 __eq__ 推導）
print(sorted([s1, s2, s3]))     # 升冪排列

# ── __len__ / __contains__ / __iter__ ────────────────────
class Classroom:
    def __init__(self, name):
        # 課堂名稱與學生清單。
        self.name = name
        self._students = []

    def add(self, student):
        # 新學生加入內部列表。
        self._students.append(student)

    def __len__(self):
        # len(obj) 會呼叫這個方法。
        return len(self._students)

    def __contains__(self, student):
        # "in" 會呼叫這個方法來判斷是否存在。
        return student in self._students

    def __iter__(self):
        # 讓物件可以直接被 for 迴圈遍歷。
        return iter(self._students)

    def __repr__(self):
        # 顯示班級名稱與目前人數。
        return f"Classroom({self.name!r}, {len(self)} 人)"


cls = Classroom("資工一甲")
cls.add("Alice")
cls.add("Bob")
cls.add("Carol")

# len / in / for 都能直接作用在這個類別上，因為對應的特殊方法已定義。
print(len(cls))             # 3
print("Alice" in cls)       # True
print("Dave" in cls)        # False

for student in cls:         # __iter__ 讓 for 迴圈可用
    # 迭代時會依序取出內部儲存的每個學生。
    print(student)
