# R04. 特殊方法（8.2–8.3）
# 本範例示範 Python 類別中的特殊方法（magic methods / dunder methods）：
# 1. __eq__ / __lt__：物件比較
# 2. __len__：讓物件可以使用 len()
# 3. __contains__：讓物件可以使用 in
# 4. __iter__：讓物件可以直接被迭代
# 5. @total_ordering：只要定義部分比較方法，就能自動補齊其他比較運算

from functools import total_ordering

# -----------------------------------------------------------------------------
# 一、@total_ordering：自動補齊比較方法
# -----------------------------------------------------------------------------
# 如果一個類別要支援排序比較，通常要定義多個方法：
# __eq__、__lt__、__le__、__gt__、__ge__
#
# total_ordering 可以幫你減少重複工作。
# 你只要實作 __eq__ 和「一個」其他比較方法（例如 __lt__），
# 它就能自動推導出剩下的比較運算。
@total_ordering
class Score:
    # 每個 Score 物件代表一個姓名與分數。
    def __init__(self, name, value):
        self.name = name
        self.value = value

    # __repr__ 提供開發者閱讀用的表示法。
    # 這裡可以清楚看出物件名稱與分數。
    def __repr__(self):
        return f"Score({self.name!r}, {self.value})"

    # __eq__ 定義「相等」的規則。
    # 這裡用分數 value 來比較，而不是 name。
    # 若比較的不是 Score 物件，回傳 NotImplemented，
    # 讓 Python 嘗試其他處理方式。
    def __eq__(self, other):
        if not isinstance(other, Score):
            return NotImplemented
        return self.value == other.value

    # __lt__ 定義「小於」的規則。
    # 這裡同樣以分數 value 作為排序依據。
    def __lt__(self, other):
        if not isinstance(other, Score):
            return NotImplemented
        return self.value < other.value


# 建立三個成績物件。
# 雖然名字不同，但比較時會以 value 分數為主。
s1 = Score("Alice", 90)
s2 = Score("Bob", 75)
s3 = Score("Carol", 90)

# 由於使用了 @total_ordering，Python 可以根據 __lt__ 與 __eq__ 推導其他比較。
print(s1 > s2)      # True  （由 __lt__ 推導）
print(s1 == s3)     # True
print(s1 != s2)     # True  （由 __eq__ 推導）
print(sorted([s1, s2, s3]))     # 升冪排列

# -----------------------------------------------------------------------------
# 二、__len__ / __contains__ / __iter__
# -----------------------------------------------------------------------------
# Classroom 類別代表一間教室，內部用 _students 儲存學生名單。
# 透過特殊方法，可以讓這個類別更像內建容器（list / set / dict）一樣使用。
class Classroom:
    def __init__(self, name):
        self.name = name
        self._students = []

    # add() 是自訂方法，用來把學生加入教室名單。
    def add(self, student):
        self._students.append(student)

    # __len__ 讓 len(cls) 可以直接取得學生人數。
    # 這樣 Classroom 物件就能像串列一樣被 len() 使用。
    def __len__(self):
        return len(self._students)

    # __contains__ 讓 "Alice" in cls 這種寫法可以成立。
    # 它會回傳某個學生是否存在於教室名單中。
    def __contains__(self, student):
        return student in self._students

    # __iter__ 讓 Classroom 物件可以被 for 迴圈逐一走訪。
    # 回傳 iter(self._students) 之後，for 迴圈就能直接迭代這個物件。
    def __iter__(self):
        return iter(self._students)

    # __repr__ 提供物件的文字表示。
    # 這裡額外顯示教室名稱與人數，方便除錯與閱讀。
    def __repr__(self):
        return f"Classroom({self.name!r}, {len(self)} 人)"


# 建立教室物件，並加入三位學生。
cls = Classroom("資工一甲")
cls.add("Alice")
cls.add("Bob")
cls.add("Carol")

# len(cls) 會呼叫 __len__，取得學生人數。
print(len(cls))             # 3

# in 運算子會呼叫 __contains__。
print("Alice" in cls)       # True
print("Dave" in cls)        # False

# for 迴圈會呼叫 __iter__，逐一取出學生名單。
for student in cls:         # __iter__ 讓 for 迴圈可用
    print(student)

# -----------------------------------------------------------------------------
# 補充說明
# -----------------------------------------------------------------------------
# __eq__：相等比較
# __lt__：小於比較
# __len__：支援 len()
# __contains__：支援 in
# __iter__：支援 for 迴圈與其他迭代機制
#
# 這些特殊方法能讓自訂類別更自然地融入 Python 語法，
# 使用起來會更接近內建型別，也更容易閱讀與維護。
