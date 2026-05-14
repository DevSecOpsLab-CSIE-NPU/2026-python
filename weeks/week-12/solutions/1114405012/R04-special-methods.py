# R04. 特殊方法（8.2–8.3）
# __eq__ / __lt__ / __len__ / __contains__ / __iter__

from functools import total_ordering

# 這份示範重點：
# 1) 特殊方法如何讓自訂類別支援比較、len()、in、for
# 2) @total_ordering 如何利用 __eq__ + 一個比較方法自動補完其他比較運算
# 3) 物件如何像內建容器一樣被使用

# ── @total_ordering：只需定義 __eq__ 和一個比較方法 ──────
# total_ordering 會根據 __eq__ 和 __lt__ 自動補出其餘比較運算子
@total_ordering
class Score:
    def __init__(self, name, value):
        # name：分數所屬的人名；value：分數值
        self.name = name
        self.value = value

    def __repr__(self):
        # 讓物件在 print(list) 或除錯時有清楚的表示
        return f"Score({self.name!r}, {self.value})"

    def __eq__(self, other):
        # 比較是否相等：如果不是 Score，回傳 NotImplemented 交給 Python 處理
        if not isinstance(other, Score):
            return NotImplemented
        # 這裡只比較 value，不比較 name
        return self.value == other.value

    def __lt__(self, other):
        # 小於比較：同樣只比較分數大小
        if not isinstance(other, Score):
            return NotImplemented
        return self.value < other.value


# 建立三個 Score 物件，觀察比較結果
s1 = Score("Alice", 90)
s2 = Score("Bob", 75)
s3 = Score("Carol", 90)

# 由於定義了 __lt__，total_ordering 可以推導出 __gt__ 等其他比較
print(s1 > s2)      # True  （由 __lt__ 推導）
# 由於 __eq__ 只比較 value，所以不同名字但同分數會視為相等
print(s1 == s3)     # True
print(s1 != s2)     # True  （由 __eq__ 推導）
# sorted 會使用比較方法對物件排序
print(sorted([s1, s2, s3]))     # 升冪排列

# ── __len__ / __contains__ / __iter__ ────────────────────
# 這個類別模擬一個教室，內部用 list 存學生名單
class Classroom:
    def __init__(self, name):
        self.name = name
        self._students = []

    def add(self, student):
        # 對外提供加入學生的方法
        self._students.append(student)

    def __len__(self):
        # 讓 len(cls) 直接回傳學生數量
        return len(self._students)

    def __contains__(self, student):
        # 讓 'Alice' in cls 這種語法可用
        return student in self._students

    def __iter__(self):
        # 讓 for student in cls 可以逐一走訪學生名單
        return iter(self._students)

    def __repr__(self):
        # 顯示教室名稱與人數，方便除錯與印出
        return f"Classroom({self.name!r}, {len(self)} 人)"


# 建立一個教室物件，並加入三位學生
cls = Classroom("資工一甲")
cls.add("Alice")
cls.add("Bob")
cls.add("Carol")

# len() 會自動呼叫 __len__
print(len(cls))             # 3
# in 會自動呼叫 __contains__
print("Alice" in cls)       # True
print("Dave" in cls)        # False

# for 迴圈會自動呼叫 __iter__ 取得迭代器
for student in cls:         # __iter__ 讓 for 迴圈可用
    print(student)
