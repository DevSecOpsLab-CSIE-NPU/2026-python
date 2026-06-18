# R02. 物件特殊方法（Special Methods / Magic Methods / Dunder Methods）
# =============================================================================
# 什麼是特殊方法？
#   特殊方法是以雙底線開頭和結尾的方法（例如 __init__, __str__, __eq__），
#   讓自訂的 class 可以「表現得像 Python 內建型別」一樣自然。
#
# 為什麼重要？
#   沒有特殊方法時，自訂 class 的行為很受限：
#     - print(obj) 只會印出 "<__main__.Student object at 0x...>"
#     - obj1 == obj2 只會比較「是不是同一個記憶體位置」
#     - sorted([obj1, obj2]) 會 TypeError，因為不知道怎麼比大小
#
# 核心概念：
#   Python 的運算符（+ - == < > print() len() ...）本質上都是在
#   呼叫物件的特殊方法。例如 a == b 實際上就是 a.__eq__(b)。
#   只要自訂這些方法，你的物件就能擁有對應的行為。
#
# 對應 Bloom's Taxonomy：記憶（Remember）— 背得出哪個場景用哪個方法
# =============================================================================


# ═════════════════════════════════════════════════════════════════════════════
# __repr__ 和 __str__：物件的自我介紹
# ═════════════════════════════════════════════════════════════════════════════
# __repr__（representation）：
#   給「開發者」看的，在 REPL、debug 時會自動顯示
#   慣例：回傳的字串要能「重現」這個物件（如果可以的話）
#   例如 Student(name='王小明', grade=85)
#
# __str__（string）：
#   給「使用者」看的，print() 會優先呼叫 __str__
#   如果沒有 __str__，Python 會 fallback 到 __repr__
#   例如 王小明：85 分

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __repr__(self):
        """開發者檢視用，慣例上要能看出物件的完整狀態

        !r 的作用：用 repr() 來格式化 name
        這樣如果 name 有特殊字元，會自動加上引號和跳脫
        """
        return f"Student(name={self.name!r}, grade={self.grade})"

    def __str__(self):
        """使用者觀看用，print() 的輸出

        這裡我們只顯示簡潔的資訊，不需要可以 recreate 物件的資訊
        """
        return f"{self.name}：{self.grade} 分"

print("=== __repr__ vs __str__ ===")
s = Student("王小明", 85)
print(repr(s))   # Student(name='王小明', grade=85)
print(str(s))    # 王小明：85 分
print(s)         # 王小明：85 分（print 優先用 __str__）


# ═════════════════════════════════════════════════════════════════════════════
# __eq__：自訂「相等」的意義
# ═════════════════════════════════════════════════════════════════════════════
# 沒有 __eq__ 的情況：
#   兩個物件只有當「記憶體位置相同」時才算相等（同一個物件）
#   就算 x 和 y 都是 Point(1, 2)，p1 == p2 還是 False
#
# 實作 __eq__ 之後：
#   可以自訂「什麼條件下算相等」
#   注意：回傳 NotImplemented 表示「我不會比這個型別」
#   Python 會再去問 other 的 class 有沒有對應的 __eq__

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        """自訂相等條件：兩個點的 x 和 y 都相同就算相等

        注意：
            1. 先用 isinstance 檢查 other 是不是 Point
            2. 如果不是，回傳 NotImplemented（告訴 Python 我無法比較）
            3. 這樣可以避免跟不相干的型別比較時出錯
        """
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

print("\n=== __eq__：自訂相等條件 ===")
p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(3, 4)
print(p1 == p2)  # True（座標相同，所以相等）
print(p1 == p3)  # False（座標不同）
print(p1 is p2)  # False（是不同的物件，記憶體位置不同）


# ═════════════════════════════════════════════════════════════════════════════
# @total_ordering：自動補齊所有比較運算子
# ═════════════════════════════════════════════════════════════════════════════
# Python 的比較運算子有 6 個：<, <=, >, >=, ==, !=
# 一般來說你只需要定義 __eq__ 和 __lt__（小於），
# 然後加上 @total_ordering 裝飾器，Python 會自動推導出其他四個。
#
# @total_ordering 的邏輯：
#   a <= b  → (a < b) or (a == b)
#   a > b   → not (a < b or a == b)
#   a >= b  → not (a < b)
#   但要注意：效率上不如手寫，因為會多次呼叫 __eq__ 和 __lt__

from functools import total_ordering

@total_ordering
class Score:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Score({self.value})"

    def __eq__(self, other):
        """相等：分數相同"""
        return self.value == other.value

    def __lt__(self, other):
        """小於：分數較低

        只需要定義 __lt__，其他比較運算子會由 @total_ordering 自動補齊
        """
        return self.value < other.value

print("\n=== @total_ordering：只寫兩個，自動補齊全部 ===")
a = Score(80)
b = Score(90)
print(a < b)   # True（80 < 90）
print(a > b)   # False（自動生成，因為 80 不大於 90）
print(a <= b)  # True（自動生成，80 <= 90）

# sorted() 內部需要 < 來排序
scores = [Score(70), Score(95), Score(60)]
print(sorted(scores))  # [Score(60), Score(70), Score(95)]


# ═════════════════════════════════════════════════════════════════════════════
# __slots__：大量物件時節省記憶體
# ═════════════════════════════════════════════════════════════════════════════
# 一般 class 的行為：
#   每個物件都有自己的一個 __dict__（字典），用來存放屬性
#   __dict__ 非常靈活（可以隨時新增屬性），但也很耗記憶體
#   每個物件的 __dict__ 大約佔 100~200 bytes
#
# __slots__ 的作法：
#   在 class 中定義 __slots__ = ('x', 'y')
#   Python 就不會建立 __dict__，改用更緊湊的資料結構
#   節省大量記憶體，但代價是「不能動態新增屬性」
#
# CPE 應用：
#   某些題目需要建立幾十萬個小物件（例如圖論的節點、座標點）
#   使用 __slots__ 可以大幅減少記憶體用量，避免 MLE（Memory Limit Exceeded）

class PointLite:
    """輕量級點 class

    __slots__ 固定只能有 x 和 y 兩個屬性
    如果嘗試設定 p.z = 5，會拋出 AttributeError
    """
    __slots__ = ('x', 'y')   # 固定只有這兩個屬性

    def __init__(self, x, y):
        self.x = x
        self.y = y

print("\n=== __slots__：固定屬性，節省記憶體 ===")
p = PointLite(3, 4)
print(p.x, p.y)   # 3 4
# p.z = 5  # 這行會 AttributeError，因為 z 不在 __slots__ 裡


# ═════════════════════════════════════════════════════════════════════════════
# 記憶重點
# ═════════════════════════════════════════════════════════════════════════════
# 1. __repr__  → 開發者用，要能「重現」物件（REPL / debug）
# 2. __str__   → 使用者用，print() 呼叫（沒定義時 fallback 到 __repr__）
# 3. __eq__    → 自訂 == 的意義（記得檢查 isinstance + NotImplemented）
# 4. @total_ordering + __eq__ + __lt__ → 自動補齊 <, <=, >, >=
# 5. __slots__ → 固定屬性，大量物件時省記憶體（但失去動態新增屬性的彈性）
# 6. 其他常見特殊方法：
#    - __len__: len(obj)
#    - __getitem__: obj[key]
#    - __iter__: for x in obj
#    - __call__: obj()
#    - __hash__: hash(obj)，用在 set 和 dict key
