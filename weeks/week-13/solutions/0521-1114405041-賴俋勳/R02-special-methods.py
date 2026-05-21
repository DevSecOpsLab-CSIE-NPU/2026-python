# ===================================================================
# R02. 物件特殊方法（Magic Methods）
# 學生：賴俋勳 1114405041
# 日期：2026-05-21
# 主題：__repr__, __str__, __eq__, @total_ordering, __slots__
# ===================================================================
# 【學習心得】
#   Python 的特殊方法（雙底線方法）讓自訂的 class 表現得像內建型別。
#   只要實作對應的方法，就能用 print()、==、<、sorted() 等語法。
#   這是「協議（Protocol）」的概念——實作介面，取得能力。
#
#   最常用的：
#   __repr__  → 給開發者看（debug 用）
#   __str__   → 給使用者看（print 用）
#   __eq__    → 定義 == 的意義
#   __lt__    → 定義 < 的意義（搭配 @total_ordering 可全部自動完成）
#   __slots__ → 固定屬性名稱，大量物件時省記憶體
# ===================================================================

# ── __repr__ 和 __str__：物件的自我介紹 ──────────────────
# __repr__：給「開發者」看的，應能重現物件（理想上可貼回去執行）
# __str__ ：給「使用者」看的，print() 時優先使用
# 若只定義 __repr__，print() 也會用它（因為 __str__ 預設呼叫 __repr__）

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __repr__(self):
        # repr 格式：能「重現」物件的字串
        # !r 表示使用 repr() 格式（字串會有引號）
        return f"Student(name={self.name!r}, grade={self.grade})"

    def __str__(self):
        # str 格式：人類好讀的字串
        return f"{self.name}：{self.grade} 分"

print("=== __repr__ vs __str__ ===")
s = Student("王小明", 85)
print(repr(s))   # Student(name='王小明', grade=85) → 開發者格式
print(str(s))    # 王小明：85 分 → 使用者格式
print(s)         # 王小明：85 分 → print() 優先用 __str__

# ── __eq__：自訂「相等」的意義 ────────────────────────────
# Python 預設的 == 比「記憶體位置」（is），而非內容。
# 定義 __eq__ 後，== 就會比「座標值」。
# 注意：isinstance 檢查確保只跟同型別比較，
#       回傳 NotImplemented 讓 Python 去問另一邊。

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        # 若對方不是 Point，回傳 NotImplemented（不是 False！）
        # 讓 Python 嘗試用對方的 __eq__ 來比
        if not isinstance(other, Point):
            return NotImplemented
        # 只有 x 和 y 都相同才算相等
        return self.x == other.x and self.y == other.y

print("\n=== __eq__：自訂相等條件 ===")
p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(3, 4)
print(p1 == p2)  # True（座標相同，但是不同的物件）
print(p1 == p3)  # False（座標不同）
print(p1 is p2)  # False（是不同的記憶體位置）

# ── @total_ordering：自動補齊所有比較運算子 ─────────────
# 只要定義 __eq__ 和 __lt__（小於），
# functools.total_ordering 裝飾器會自動生成剩下的 <=, >, >=。
# 省去手動寫4個比較方法的工夫。

from functools import total_ordering

@total_ordering      # 裝飾器：幫我補齊 <=, >, >= 三個方法
class Score:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Score({self.value})"

    def __eq__(self, other):
        # 定義「相等」：value 相同
        return self.value == other.value

    def __lt__(self, other):
        # 定義「小於」：value 較小
        # @total_ordering 會根據這個自動生成 <=, >, >=
        return self.value < other.value

print("\n=== @total_ordering：只寫兩個，自動補齊全部 ===")
a = Score(80)
b = Score(90)
print(a < b)   # True（我們定義的 __lt__）
print(a > b)   # False（@total_ordering 自動生成的 __gt__）
print(a <= b)  # True（@total_ordering 自動生成的 __le__）

# sorted() 需要 < 比較，有了 __lt__ 就能直接排序
scores = [Score(70), Score(95), Score(60)]
print(sorted(scores))  # [Score(60), Score(70), Score(95)]

# ── __slots__：大量物件時節省記憶體 ──────────────────────
# 一般 class 每個物件都有 __dict__（字典），方便但耗記憶體。
# 宣告 __slots__ 後，物件只能有指定的屬性，沒有 __dict__，
# 記憶體佔用大幅降低（約節省 40%~60%）。
# 適合：大量小物件（例如 CPE 題目建立幾十萬個節點）。

class PointLite:
    __slots__ = ('x', 'y')   # 只允許 x 和 y 兩個屬性

    def __init__(self, x, y):
        self.x = x
        self.y = y

print("\n=== __slots__：固定屬性，節省記憶體 ===")
p = PointLite(3, 4)
print(p.x, p.y)   # 3 4
# p.z = 5  # 若取消注解，會 AttributeError（z 不在 __slots__）

# ─── 記憶重點 ──────────────────────────────────────────────
# __repr__  → 開發者用，要能「重現」物件
# __str__   → 使用者用，print() 呼叫
# __eq__    → 自訂 == 的意義（不是 is！）
# @total_ordering + __lt__ → 自動補齊 <, <=, >, >=
# __slots__ → 固定屬性，大量物件時省記憶體
