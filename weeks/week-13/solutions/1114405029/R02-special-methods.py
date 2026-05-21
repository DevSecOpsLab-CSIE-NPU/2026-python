# R02. 物件特殊方法
# 讓自訂的 class 表現得像 Python 內建型別
# 對應 Bloom's Taxonomy：記憶（Remember）— 背得出哪個場景用哪個方法
#
# 本題核心：
# Python 的 class 除了一般方法之外，還有很多「特殊方法」。
#
# 特殊方法通常長這樣：
# __方法名稱__
#
# 前後都有兩個底線，所以也常被稱為 dunder method。
# dunder 是 double underscore 的縮寫。
#
# 特殊方法的用途：
# 讓我們自己寫的物件，可以支援 Python 內建語法。
#
# 例如：
# print(物件)       會用到 __str__
# repr(物件)        會用到 __repr__
# 物件1 == 物件2    會用到 __eq__
# 物件1 < 物件2     會用到 __lt__
# sorted(串列)      會用到比較方法
#
# 也就是說：
# 特殊方法可以讓自訂 class 的使用方式更像 int、str、list 這些內建型別。

# ── __repr__ 和 __str__：物件的自我介紹 ──────────────────
# __repr__：給「開發者」看的（在 REPL、debug 時出現）
# __str__ ：給「使用者」看的（print() 優先用這個）
#
# __repr__ 和 __str__ 都是用來把物件轉成字串。
#
# 差別在於：
#
# 1. __repr__
#    偏向給程式開發者或除錯時看。
#    通常希望內容清楚、正式，甚至可以看出如何重建物件。
#
# 2. __str__
#    偏向給一般使用者看。
#    通常希望內容簡潔、好讀、適合 print 顯示。
#
# 如果 class 有寫 __str__：
# print(物件) 會優先使用 __str__。
#
# 如果 class 沒有寫 __str__，但有寫 __repr__：
# print(物件) 可能會退而使用 __repr__。

class Student:
    # Student 類別用來表示一位學生。
    #
    # 這個類別有兩個屬性：
    # name  ：學生姓名
    # grade ：學生分數

    def __init__(self, name, grade):
        # __init__ 是建構子。
        #
        # 當我們建立 Student 物件時，
        # Python 會自動呼叫 __init__。
        #
        # 例如：
        # Student("王小明", 85)
        #
        # 會把：
        # name = "王小明"
        # grade = 85
        #
        # 傳進這個方法。
        self.name = name

        # 把傳入的 grade 存成物件的屬性。
        self.grade = grade

    def __repr__(self):
        # __repr__ 是給開發者看的物件表示法。
        #
        # repr(s) 時會呼叫這個方法。
        #
        # 這裡回傳：
        # Student(name='王小明', grade=85)
        #
        # 這種格式可以清楚看出：
        # 1. 物件類別是 Student
        # 2. name 屬性是多少
        # 3. grade 屬性是多少
        #
        # !r 的意思是使用 repr() 格式表示該值。
        # 對字串來說，會自動加上引號。
        #
        # 例如：
        # self.name = "王小明"
        # {self.name!r} 會變成 '王小明'
        return f"Student(name={self.name!r}, grade={self.grade})"

    def __str__(self):
        # __str__ 是給使用者看的物件表示法。
        #
        # str(s) 或 print(s) 時會優先呼叫這個方法。
        #
        # 這裡回傳比較自然、容易閱讀的格式：
        # 王小明：85 分
        return f"{self.name}：{self.grade} 分"

# 印出區塊標題，方便觀察 __repr__ 和 __str__ 的差異。
print("=== __repr__ vs __str__ ===")

# 建立一個 Student 物件。
#
# s.name = "王小明"
# s.grade = 85
s = Student("王小明", 85)

# repr(s) 會呼叫 s.__repr__()。
#
# 這是偏開發者或除錯用的表示方式。
print(repr(s))   # Student(name='王小明', grade=85)

# str(s) 會呼叫 s.__str__()。
#
# 這是偏一般使用者閱讀的表示方式。
print(str(s))    # 王小明：85 分

# print(s) 會優先使用 __str__。
#
# 所以輸出結果會和 str(s) 相同。
print(s)         # 王小明：85 分（print 優先用 __str__）

# ── __eq__：自訂「相等」的意義 ────────────────────────────
# 沒有 __eq__ 的話，兩個物件只有「同一個記憶體位置」才算相等
#
# Python 中的 == 預設不一定會比較內容。
#
# 如果是一般自訂物件，
# 沒有寫 __eq__ 的情況下，
# Python 通常會比較兩個變數是不是指向同一個物件。
#
# 也就是說：
# p1 == p2 預設可能接近 p1 is p2。
#
# 但是我們常常希望比較「內容」。
#
# 例如：
# Point(1, 2) 和 Point(1, 2)
#
# 雖然是兩個不同物件，
# 但座標內容相同，所以可以定義成相等。
#
# 這時就可以寫 __eq__。

class Point:
    # Point 類別用來表示二維座標點。
    #
    # 每個 Point 物件有：
    # x 座標
    # y 座標

    def __init__(self, x, y):
        # 初始化 x 座標。
        self.x = x

        # 初始化 y 座標。
        self.y = y

    def __repr__(self):
        # 回傳給開發者看的 Point 表示方式。
        #
        # 例如：
        # Point(1, 2)
        #
        # 這樣在印出 list 或除錯時比較清楚。
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        # __eq__ 會在使用 == 比較時被呼叫。
        #
        # 例如：
        # p1 == p2
        #
        # 實際上會呼叫：
        # p1.__eq__(p2)
        #
        # self  代表左邊的物件 p1
        # other 代表右邊的物件 p2

        # 先確認 other 是不是 Point 類別。
        #
        # 如果 other 不是 Point，
        # 代表它不是同種類型的座標點，
        # 這時不應該直接比較 x 和 y。
        #
        # 回傳 NotImplemented 的意思是：
        # 告訴 Python 這種比較我不處理，
        # 讓 Python 嘗試其他比較方式或最後判定不支援。
        if not isinstance(other, Point):
            return NotImplemented

        # 如果 other 也是 Point，
        # 就比較兩個座標是否完全相同。
        #
        # x 相同且 y 相同，才算兩個 Point 相等。
        return self.x == other.x and self.y == other.y

# 印出區塊標題。
print("\n=== __eq__：自訂相等條件 ===")

# 建立三個 Point 物件。
#
# p1 和 p2 的座標內容一樣，都是 (1, 2)。
# p3 的座標內容是 (3, 4)。
p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(3, 4)

# 因為 Point 有定義 __eq__，
# 所以 p1 == p2 會比較座標內容。
#
# p1 和 p2 的 x、y 都相同，因此結果是 True。
print(p1 == p2)  # True（座標相同）

# p1 和 p3 的座標不同，
# 所以結果是 False。
print(p1 == p3)  # False

# is 比較的是「是不是同一個物件」。
#
# p1 和 p2 雖然座標相同，
# 但它們是分別建立出來的兩個物件，
# 記憶體位置不同，
# 所以 p1 is p2 是 False。
print(p1 is p2)  # False（是不同的物件，記憶體位置不同）

# ── @total_ordering：自動補齊所有比較運算子 ─────────────
# 只要定義 __eq__ 和一個比較（__lt__），
# @total_ordering 會自動補出 <=, >, >= 四個
#
# Python 的比較運算子包含：
# <
# <=
# >
# >=
# ==
#
# 如果全部都自己寫，會很麻煩。
#
# functools.total_ordering 可以幫我們少寫一些比較方法。
#
# 使用條件：
# 1. 類別要定義 __eq__
# 2. 類別至少要定義一個排序比較方法，例如 __lt__
#
# 其中：
# __lt__ 對應 <
# __le__ 對應 <=
# __gt__ 對應 >
# __ge__ 對應 >=
#
# 這段程式只寫 __eq__ 和 __lt__，
# 剩下的 <=、>、>= 由 @total_ordering 自動補齊。

from functools import total_ordering

# 從 functools 匯入 total_ordering。
#
# total_ordering 是一個 class decorator。
# 它會根據我們已經定義的比較方法，
# 自動補出其他比較方法。

@total_ordering
class Score:
    # Score 類別用來表示一個分數。
    #
    # 這裡希望 Score 物件可以直接用 <、>、<= 來比較大小。

    def __init__(self, value):
        # value 是實際的分數數值。
        self.value = value

    def __repr__(self):
        # 回傳開發者看的表示方式。
        #
        # 例如 Score(80)。
        #
        # 當 Score 物件放在 list 裡被印出時，
        # Python 會用 __repr__ 顯示每個元素。
        return f"Score({self.value})"

    def __eq__(self, other):
        # 定義 == 的比較方式。
        #
        # 兩個 Score 是否相等，
        # 取決於它們的 value 是否相同。
        return self.value == other.value

    def __lt__(self, other):
        # 定義 < 的比較方式。
        #
        # self.value < other.value
        # 代表分數數值較小時，Score 物件也較小。
        return self.value < other.value

# 印出區塊標題。
print("\n=== @total_ordering：只寫兩個，自動補齊全部 ===")

# 建立兩個 Score 物件。
a = Score(80)
b = Score(90)

# a < b 會呼叫 a.__lt__(b)。
#
# 因為 80 < 90，
# 所以結果是 True。
print(a < b)   # True

# a > b 沒有直接手寫 __gt__，
# 但因為使用了 @total_ordering，
# Python 會根據 __eq__ 和 __lt__ 自動推導出 >。
#
# 80 > 90 是 False。
print(a > b)   # False（自動生成）

# a <= b 也沒有直接手寫 __le__，
# 但 @total_ordering 會自動補出來。
#
# 80 <= 90 是 True。
print(a <= b)  # True（自動生成）

# 建立一個 Score 物件串列。
scores = [Score(70), Score(95), Score(60)]

# sorted(scores) 會排序這些 Score 物件。
#
# 排序時需要知道兩個 Score 物件誰比較小。
# 因為 Score 有定義 __lt__，
# 所以 sorted 可以正常排序。
#
# 排序結果會依照 value 由小到大排列。
print(sorted(scores))  # [Score(60), Score(70), Score(95)]

# ── __slots__：大量物件時節省記憶體 ──────────────────────
# 一般 class 每個物件都有一個 __dict__，很耗記憶體
# CPE 題目有時會建立幾十萬個小物件，__slots__ 可以大幅節省
#
# 一般 Python 物件通常可以動態新增屬性。
#
# 例如：
# p.name = "abc"
# p.z = 5
#
# 這是因為一般物件內部有 __dict__，
# 用 dictionary 儲存屬性名稱和屬性值。
#
# 但是 dictionary 會佔用額外記憶體。
#
# 如果我們知道一個類別只會有固定幾個屬性，
# 就可以使用 __slots__ 限制屬性名稱。
#
# 好處：
# 1. 節省記憶體
# 2. 避免不小心打錯屬性名稱
# 3. 大量建立小物件時更有效率
#
# 限制：
# 1. 不能隨便新增 __slots__ 以外的屬性
# 2. 使用上比一般 class 彈性少一點

class PointLite:
    # __slots__ 用來宣告這個類別允許的屬性。
    #
    # 這裡表示 PointLite 物件只能有：
    # x
    # y
    #
    # 兩個屬性。
    __slots__ = ('x', 'y')   # 固定只有這兩個屬性

    def __init__(self, x, y):
        # 初始化 x 屬性。
        #
        # 因為 x 有列在 __slots__ 裡，
        # 所以可以正常指定。
        self.x = x

        # 初始化 y 屬性。
        #
        # 因為 y 有列在 __slots__ 裡，
        # 所以可以正常指定。
        self.y = y

# 印出區塊標題。
print("\n=== __slots__：固定屬性，節省記憶體 ===")

# 建立 PointLite 物件。
p = PointLite(3, 4)

# 印出 p.x 和 p.y。
#
# 因為 PointLite 的 __init__ 有設定：
# self.x = 3
# self.y = 4
#
# 所以這裡會輸出：
# 3 4
print(p.x, p.y)   # 3 4

# 下面這行被註解掉，所以不會執行。
#
# 如果取消註解，會發生 AttributeError。
#
# 原因：
# PointLite 的 __slots__ 只有宣告 x 和 y，
# 沒有宣告 z。
#
# 所以 PointLite 物件不能新增 p.z 這個屬性。
# p.z = 5  # 這行會 AttributeError，因為 z 不在 __slots__ 裡

# 記憶重點 ──────────────────────────────────────────────────
# __repr__  → 開發者用，要能「重現」物件
# __str__   → 使用者用，print() 呼叫
# __eq__    → 自訂 == 的意義
# @total_ordering + __lt__ → 自動補齊 <, <=, >, >=
# __slots__ → 固定屬性，大量物件時省記憶體
#
# 補充整理：
#
# 1. __repr__
#    適合給開發者、除錯、REPL 使用。
#    通常希望資訊完整，能看出物件內容。
#
# 2. __str__
#    適合給一般使用者閱讀。
#    print(物件) 時會優先使用它。
#
# 3. __eq__
#    可以讓 == 比較物件內容，而不只是比較記憶體位置。
#
# 4. @total_ordering
#    可以少寫比較方法。
#    只要寫 __eq__ 和一個大小比較方法，就能自動補齊其他比較運算。
#
# 5. __slots__
#    適合大量建立固定欄位的小物件。
#    可以節省記憶體，也可以避免不小心新增錯誤屬性。