# R04. 特殊方法（8.2–8.3）
# __eq__ / __lt__ / __len__ / __contains__ / __iter__ / __getitem__ / __str__ / __bool__
#
# 特殊方法（又稱魔術方法）是 Python 類別中以雙底線開頭和結尾的方法，
# 讓自訂物件能夠使用 Python 原生的運算子與內建函式，例如：
#   len(obj)    → 實際呼叫 obj.__len__()
#   obj in xs   → 實際呼叫 xs.__contains__(obj)
#   for x in xs → 實際呼叫 iter(xs) → xs.__iter__()
#   obj[i]      → 實際呼叫 obj.__getitem__(i)
#   str(obj)    → 實際呼叫 obj.__str__()
#   bool(obj)   → 實際呼叫 obj.__bool__()

from functools import total_ordering


# ────────────────────────────────────────────────────────────
#  @total_ordering：只需定義 __eq__ 和一個比較方法
#  裝飾器會自動補齊其他比較運算子（>、<=、>=、!=）
# ────────────────────────────────────────────────────────────
@total_ordering
class Score:
    """表示一個分數，可比較大小、排序。"""

    def __init__(self, name: str, value: int) -> None:
        """
        建構子：初始化姓名與分數。
        - name:  學生姓名（字串）
        - value: 分數（整數）
        """
        self.name = name
        self.value = value

    def __repr__(self) -> str:
        """
        __repr__()：給開發者看的正式字串表示。
        使用 !r 讓 name 顯示時包含引號，方便除錯辨識。
        若未定義 __str__，print() 也會退化使用 __repr__。
        """
        return f"Score({self.name!r}, {self.value})"

    def __eq__(self, other: object) -> bool:
        """
        __eq__()：定義 == 運算行為。
        規則：
        1. 若 other 不是 Score 實例，回傳 NotImplemented，
           讓 Python 嘗試 other 端的 __eq__ 或反向比較。
        2. 否則比較 value 是否相等。
        """
        if not isinstance(other, Score):
            return NotImplemented  # 型別不符，交由 Python 處理
        return self.value == other.value

    def __lt__(self, other: object) -> bool:
        """
        __lt__()：定義 < 運算行為。
        配合 @total_ordering，Python 可自動推導出：
          __gt__（>）：  not (self < other or self == other)
          __le__（<=）： self < other or self == other
          __ge__（>=）： not (self < other)
          __ne__（!=）： not (self == other)
        """
        if not isinstance(other, Score):
            return NotImplemented
        return self.value < other.value


# 建立 Score 實例並測試比較運算子
s1 = Score("Alice", 90)
s2 = Score("Bob", 75)
s3 = Score("Carol", 90)

print("=== 比較運算子（自動推導）===")
print(f"{s1} > {s2}  => {s1 > s2}")      # True  （由 __lt__ 推導出 __gt__）
print(f"{s1} == {s3} => {s1 == s3}")     # True  （直接呼叫 __eq__）
print(f"{s1} != {s2} => {s1 != s2}")     # True  （由 __eq__ 推導出 __ne__）
print(f"排序結果：{sorted([s1, s2, s3])}")  # 升冪排列（使用 __lt__）


# ────────────────────────────────────────────────────────────
#  __len__ / __contains__ / __iter__ / __getitem__
#  __str__ / __bool__ / __repr__
#  搭配使用，讓 Classroom 就像一個內建集合型別。
# ────────────────────────────────────────────────────────────
class Classroom:
    """模擬一個班級，內部以串列儲存學生姓名。"""

    def __init__(self, name: str) -> None:
        """
        建構子：初始化班級名稱與空的學生清單。
        - name: 班級名稱（如 "資工一甲"）
        """
        self.name = name
        self._students: list[str] = []  # 底線開頭表示內部使用，不應直接存取

    def add(self, student: str) -> None:
        """將一位學生加入班級（追加到串列尾端）。"""
        self._students.append(student)

    def __len__(self) -> int:
        """
        __len__()：讓 len(cls) 回傳學生人數。
        若回傳 0，bool(cls) 預設為 False；否則為 True。
        """
        return len(self._students)

    def __contains__(self, student: str) -> bool:
        """
        __contains__()：讓 'Alice' in cls 檢查學生是否存在。
        底層使用串列的 in 運算子（線性搜尋）。
        """
        return student in self._students

    def __iter__(self):
        """
        __iter__()：讓 for student in cls 可以逐一迭代學生。
        回傳一個迭代器（此處直接借用串列的迭代器）。
        """
        return iter(self._students)

    def __getitem__(self, index: int) -> str:
        """
        __getitem__()：讓 cls[0] 支援索引存取。
        也支援切片（cls[1:3]），因為串列 __getitem__ 原生支援。
        """
        return self._students[index]

    def __str__(self) -> str:
        """
        __str__()：給使用者看的友善字串，print() 會優先呼叫它。
        若未定義 __str__，Python 會退化使用 __repr__。
        """
        return f"班級：{self.name}，共 {len(self)} 位學生"

    def __repr__(self) -> str:
        """
        __repr__()：給開發者看的正式表示，應包含重現物件所需的資訊。
        在直譯環境中直接輸入變數名稱也會呼叫此方法。
        """
        return f"Classroom({self.name!r}, {len(self)} 人)"

    def __bool__(self) -> bool:
        """
        __bool__()：定義 bool(cls) 的行為。
        若班級有學生則為 True，空班級為 False。
        若未定義 __bool__，Python 會退化使用 __len__()。
        """
        return len(self._students) > 0


# 建立 Classroom 實例並測試各種特殊方法
print("\n=== 特殊方法展示 ===")
cls = Classroom("資工一甲")

# __bool__：空班級為 False
print(f"剛建立時 bool(cls) = {bool(cls)}（空班級）")

# add / __len__
cls.add("Alice")
cls.add("Bob")
cls.add("Carol")
print(f"加入 3 人後 len(cls) = {len(cls)}")    # 3

# __bool__：有學生後為 True
print(f"加入學生後 bool(cls) = {bool(cls)}")

# __contains__
print(f"'Alice' in cls = {'Alice' in cls}")    # True
print(f"'Dave' in cls  = {'Dave' in cls}")     # False

# __getitem__（索引與切片）
print(f"cls[0]   = {cls[0]}")     # Alice
print(f"cls[-1]  = {cls[-1]}")    # Carol
print(f"cls[1:]  = {cls[1:]}")    # ['Bob', 'Carol']

# __iter__：for 迴圈
print("全班學生：")
for student in cls:
    print(f"  - {student}")

# __str__ 與 __repr__
print(f"print 顯示（__str__）： {cls}")
print(f"除錯顯示（__repr__）： {cls!r}")
