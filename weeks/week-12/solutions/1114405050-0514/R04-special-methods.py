# R04. 特殊方法（8.2–8.3）
# __eq__ / __lt__ / __len__ / __contains__ / __iter__

from functools import total_ordering

# ── @total_ordering：只需定義 __eq__ 和一個比較方法 ──────
# @total_ordering 是一個類別裝飾器，只要定義了 __eq__ 以及 __lt__, __le__, __gt__, __ge__ 其中之一，
# 它就會自動幫我們補齊其他的比較方法（例如大於、大於等於等），減少重複寫類似的程式碼。
@total_ordering
class Score:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"Score({self.name!r}, {self.value})"

    # __eq__ (equal) 定義當使用 == 運算符時的比較行為
    def __eq__(self, other):
        if not isinstance(other, Score):
            # 回傳 NotImplemented 代表「不知道怎麼跟這個型別比較」，Python 會嘗試其他方式或報錯
            return NotImplemented
        return self.value == other.value

    # __lt__ (less than) 定義當使用 < 運算符時的比較行為
    def __lt__(self, other):
        if not isinstance(other, Score):
            return NotImplemented
        return self.value < other.value


s1 = Score("Alice", 90)
s2 = Score("Bob", 75)
s3 = Score("Carol", 90)

print(s1 > s2)                  # True  （即使沒寫 __gt__，@total_ordering 也會用 __lt__ 推導出來）
print(s1 == s3)                 # True  （呼叫 __eq__）
print(s1 != s2)                 # True  （由 __eq__ 推導）
print(sorted([s1, s2, s3]))     # 升冪排列 （sorted 內部會依賴 < 來進行排序）

# ── __len__ / __contains__ / __iter__ ────────────────────
# 這些特殊方法可以讓自訂類別具備像串列 (list) 或字典 (dict) 般的容器行為
class Classroom:
    def __init__(self, name):
        self.name = name
        self._students = []

    def add(self, student):
        self._students.append(student)

    # 定義 len(obj) 的行為
    def __len__(self):
        return len(self._students)

    # 定義 item in obj 的行為
    def __contains__(self, student):
        return student in self._students

    # 定義物件如何被迭代（例如：可以使用 for student in cls）
    def __iter__(self):
        return iter(self._students)

    def __repr__(self):
        return f"Classroom({self.name!r}, {len(self)} 人)"


cls = Classroom("資工一甲")
cls.add("Alice")
cls.add("Bob")
cls.add("Carol")

print(len(cls))             # 3          （呼叫 cls.__len__()）
print("Alice" in cls)       # True       （呼叫 cls.__contains__("Alice")）
print("Dave" in cls)        # False

for student in cls:         # 因為有定義 __iter__，所以可以作為 for 迴圈的迭代對象
    print(student)
