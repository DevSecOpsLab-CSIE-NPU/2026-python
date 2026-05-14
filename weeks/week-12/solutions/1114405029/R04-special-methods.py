# R04. 特殊方法（8.2–8.3）
# __eq__ / __lt__ / __len__ / __contains__ / __iter__

# 從 functools 模組匯入 total_ordering
# total_ordering 是一個裝飾器（decorator）
# 它可以幫我們自動補齊比較運算方法
from functools import total_ordering

# ── @total_ordering：只需定義 __eq__ 和一個比較方法 ──────

# @total_ordering：
# 只要類別中定義：
# 1. __eq__()
# 2. 其中一個大小比較方法，例如 __lt__()
#
# Python 就可以自動推導出其他比較方法：
# >、<=、>=、!=
@total_ordering
class Score:

    # __init__()：
    # 建構子，建立 Score 物件時會自動呼叫
    def __init__(self, name, value):

        # self.name：
        # 儲存學生姓名
        self.name = name

        # self.value：
        # 儲存分數
        self.value = value

    # __repr__()：
    # 提供開發者查看物件時使用的字串表示方式
    def __repr__(self):

        # !r：
        # 代表使用 repr() 格式輸出 name
        # 字串會包含引號
        return f"Score({self.name!r}, {self.value})"

    # __eq__()：
    # 定義 == 的比較規則
    def __eq__(self, other):

        # isinstance(other, Score)：
        # 檢查 other 是否為 Score 類別的物件

        # 如果 other 不是 Score：
        # 回傳 NotImplemented
        # 代表目前這個類別不知道如何比較
        if not isinstance(other, Score):
            return NotImplemented

        # 如果兩個 Score 的 value 相同
        # 就視為相等
        return self.value == other.value

    # __lt__()：
    # 定義 < 的比較規則
    #
    # lt 是 less than 的縮寫
    def __lt__(self, other):

        # 如果 other 不是 Score：
        # 回傳 NotImplemented
        if not isinstance(other, Score):
            return NotImplemented

        # 分數較小者，視為比較小
        return self.value < other.value


# 建立三個 Score 物件
s1 = Score("Alice", 90)
s2 = Score("Bob", 75)
s3 = Score("Carol", 90)

# s1 > s2：
# 因為有 @total_ordering
# 所以 > 可以由 __lt__ 和 __eq__ 推導出來
print(s1 > s2)      # True  （由 __lt__ 推導）

# s1 == s3：
# 會呼叫 __eq__()
# 因為兩者 value 都是 90
# 所以結果為 True
print(s1 == s3)     # True

# s1 != s2：
# 會根據 __eq__ 推導出來
# 因為 90 != 75
# 所以結果為 True
print(s1 != s2)     # True  （由 __eq__ 推導）

# sorted()：
# 會使用物件的比較方法進行排序
# 這裡會根據 value 由小到大排列
print(sorted([s1, s2, s3]))     # 升冪排列

# ── __len__ / __contains__ / __iter__ ────────────────────

# Classroom 類別
# 用來表示一個班級
class Classroom:

    # __init__()：
    # 建立 Classroom 物件時呼叫
    def __init__(self, name):

        # self.name：
        # 儲存班級名稱
        self.name = name

        # self._students：
        # 儲存學生名單
        #
        # 前面加底線 _：
        # 表示這個變數主要供類別內部使用
        # 不建議外部直接操作
        self._students = []

    # add()：
    # 自訂方法，用來新增學生
    def add(self, student):

        # append()：
        # 將 student 加入學生名單 list 的最後面
        self._students.append(student)

    # __len__()：
    # 定義 len(obj) 的行為
    def __len__(self):

        # 回傳學生數量
        return len(self._students)

    # __contains__()：
    # 定義 in 的行為
    #
    # 例如：
    # "Alice" in cls
    def __contains__(self, student):

        # 檢查 student 是否存在於學生名單中
        return student in self._students

    # __iter__()：
    # 定義物件是否可以被迭代
    #
    # 例如：
    # for student in cls:
    def __iter__(self):

        # iter(self._students)：
        # 回傳學生名單 list 的迭代器
        #
        # 這樣 Classroom 物件就可以直接用 for 迴圈走訪
        return iter(self._students)

    # __repr__()：
    # 提供開發者查看 Classroom 物件時的表示方式
    def __repr__(self):

        # len(self)：
        # 會自動呼叫 __len__()
        #
        # 例如：
        # Classroom('資工一甲', 3 人)
        return f"Classroom({self.name!r}, {len(self)} 人)"


# 建立 Classroom 物件
cls = Classroom("資工一甲")

# 新增學生 Alice
cls.add("Alice")

# 新增學生 Bob
cls.add("Bob")

# 新增學生 Carol
cls.add("Carol")

# len(cls)：
# 會呼叫 cls.__len__()
# 回傳學生人數 3
print(len(cls))             # 3

# "Alice" in cls：
# 會呼叫 cls.__contains__("Alice")
print("Alice" in cls)       # True

# "Dave" in cls：
# Dave 不在學生名單中
print("Dave" in cls)        # False

# for student in cls：
# 會呼叫 cls.__iter__()
# 讓 Classroom 物件可以被 for 迴圈走訪
for student in cls:         # __iter__ 讓 for 迴圈可用

    # 逐一印出學生姓名
    print(student)