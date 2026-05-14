# R04. 特殊方法（8.2–8.3）
# __eq__ / __lt__ / __len__ / __contains__ / __iter__

# 匯入functools模組的total_ordering裝飾器
from functools import total_ordering

# ── @total_ordering：只需定義 __eq__ 和一個比較方法 ──────
# @total_ordering裝飾器可以自動產生其他比較方法
@total_ordering
class Score:
    # 建構函式：初始化學生姓名和分數
    def __init__(self, name, value):
        self.name = name
        self.value = value

    # __repr__方法：定義物件的字串表示
    def __repr__(self):
        return f"Score({self.name!r}, {self.value})"

    # __eq__方法：定義相等比較
    def __eq__(self, other):
        if not isinstance(other, Score):
            return NotImplemented  # 如果不是Score實例，返回NotImplemented
        return self.value == other.value  # 比較分數是否相等

    # __lt__方法：定義小於比較
    def __lt__(self, other):
        if not isinstance(other, Score):
            return NotImplemented  # 如果不是Score實例，返回NotImplemented
        return self.value < other.value  # 比較分數大小


# 建立Score實例進行測試
s1 = Score("Alice", 90)
s2 = Score("Bob", 75)
s3 = Score("Carol", 90)

# 測試比較運算子（由@total_ordering自動產生）
print(s1 > s2)      # True：s1的分數(90)大於s2(75)
print(s1 == s3)     # True：s1和s3的分數都是90
print(s1 != s2)     # True：s1和s2的分數不同（由__eq__推導）
print(sorted([s1, s2, s3]))     # 根據分數升冪排列

# ── __len__ / __contains__ / __iter__ ────────────────────
# 定義一個Classroom類別，示範容器型別的特殊方法
class Classroom:
    # 建構函式：初始化班級名稱和空的學生列表
    def __init__(self, name):
        self.name = name
        self._students = []  # 私有屬性儲存學生列表

    # add方法：新增學生到班級
    def add(self, student):
        self._students.append(student)

    # __len__方法：讓len()函式可以用於此物件
    def __len__(self):
        return len(self._students)  # 返回學生數量

    # __contains__方法：讓in運算子可以用於此物件
    def __contains__(self, student):
        return student in self._students  # 檢查學生是否在班級中

    # __iter__方法：讓物件可以被迭代
    def __iter__(self):
        return iter(self._students)  # 返回學生列表的迭代器

    # __repr__方法：定義物件的字串表示
    def __repr__(self):
        return f"Classroom({self.name!r}, {len(self)} 人)"


# 建立Classroom實例並新增學生
cls = Classroom("資工一甲")
cls.add("Alice")
cls.add("Bob")
cls.add("Carol")

# 測試容器方法
print(len(cls))             # 3：使用__len__方法
print("Alice" in cls)       # True：使用__contains__方法
print("Dave" in cls)        # False：Dave不在班級中

# 使用for迴圈遍歷學生（使用__iter__方法）
for student in cls:         # __iter__讓for迴圈可用
    print(student)          # 輸出每個學生的名字
