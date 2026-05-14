"""
R04. 特殊方法（8.2–8.3）

本檔示範 Python 類別常見的特殊方法（magic / dunder methods），包括：
  - 比較相關：`__eq__`, `__lt__`（搭配 `functools.total_ordering` 可以自動補齊其他比較方法）
  - 集合/容器協議：`__len__`, `__contains__`, `__iter__`

特殊方法讓自訂類別能夠與 Python 語言的內建運算、內建函式和語法結構互動，
例如 `len(obj)`、`x in obj`、`sorted(list_of_obj)`、`for item in obj` 等。

良好實作這些方法可以讓自訂類別行為更直覺且與標準庫相容。
"""

from functools import total_ordering


# ── @total_ordering：只需定義 __eq__ 和一個比較方法即可得到完整比較能力 ──────
# 使用 total_ordering 裝飾器後，若類別至少定義了 __eq__ 與 __lt__（或其他一對比較方法），
# Python 會自動提供其餘的比較方法（如 __le__, __gt__, __ge__），減少重複實作。
@total_ordering
class Score:
    """示範可比較的自訂物件。

    每個 Score 物件含有 name（辨識用）與 value（分數），
    比較邏輯只根據 value 決定。
    """
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        # __repr__ 應該回傳一個對開發者友善的表示，方便除錯
        return f"Score({self.name!r}, {self.value})"

    def __eq__(self, other):
        # 若 other 不是同類別，回傳 NotImplemented，讓 Python 去嘗試其他比較方法
        if not isinstance(other, Score):
            return NotImplemented
        return self.value == other.value

    def __lt__(self, other):
        if not isinstance(other, Score):
            return NotImplemented
        return self.value < other.value


# 範例：建立三個 Score 物件並示範比較
s1 = Score("Alice", 90)
s2 = Score("Bob", 75)
s3 = Score("Carol", 90)

print(s1 > s2)      # True  （由 __lt__ 推導出 __gt__）
print(s1 == s3)     # True
print(s1 != s2)     # True  （由 __eq__ 推導出 != ）
print(sorted([s1, s2, s3]))     # 升冪排列（依 value）


# ── __len__ / __contains__ / __iter__：讓物件表現得像容器（list/set 等） ────────────
class Classroom:
    """示範如何讓自訂容器支援 len(), in, 以及 for 迴圈。

    設計上 Classroom 內部用 _students 儲存學生名單，並提供 add() 加入學生。
    透過實作下列特殊方法，可以讓 Classroom 的使用方式與原生容器相同：
      - __len__(self)：支援 len(cls)
      - __contains__(self, item)：支援 `item in cls`
      - __iter__(self)：支援 `for x in cls`
    """
    def __init__(self, name):
        self.name = name
        # 內部使用底線前綴表示為「私有/內部使用」的儲存容器
        self._students = []

    def add(self, student):
        # 將學生加入內部列表
        self._students.append(student)

    def __len__(self):
        # 回傳容器元素個數，讓 len(classroom) 可用
        return len(self._students)

    def __contains__(self, student):
        # 定義成員測試，讓 'Alice in classroom' 能正常運作
        return student in self._students

    def __iter__(self):
        # 回傳一個 iterator，讓 for 迴圈可以遍歷物件
        return iter(self._students)

    def __repr__(self):
        # 清楚列出教室名稱與人數，方便除錯或印出資訊
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
