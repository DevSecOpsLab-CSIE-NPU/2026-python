# U02. @classmethod：多重構造器（工廠方法）
# 讓 class 可以用「不同格式的資料」建立物件，不只是靠 __init__
# 對應 Bloom's Taxonomy：理解（Understand）— 能解釋 cls 的作用與繼承行為
#
# 本題核心：
# @classmethod 可以讓 class 本身呼叫某個方法，
# 而不是一定要先建立物件才能呼叫。
#
# 一般物件方法的第一個參數是 self：
# self 代表「目前這個物件」。
#
# classmethod 的第一個參數是 cls：
# cls 代表「目前這個 class」。
#
# @classmethod 常用來做「替代構造器」或「工廠方法」。
#
# 簡單說：
# __init__ 通常負責最基本的建立方式。
# @classmethod 可以提供其他建立物件的方式。
#
# 例如：
# Point(3, 4)                 → 直接用 x, y 建立
# Point.from_string("3,4")    → 從字串建立
# Point.from_list([3, 4])     → 從 list 建立
# Point.origin()              → 建立原點
#
# 這樣可以讓 __init__ 保持簡單，
# 不用把所有格式解析都塞進 __init__ 裡。

# ── 問題：__init__ 只能有一種寫法 ────────────────────────
# 座標點可能來自不同地方：
#   - 直接給 (x, y)
#   - 從字串 "3,4" 解析
#   - 從 list [3, 4] 讀取
# 三種都用 __init__ 處理，會讓 __init__ 變得很複雜
#
# 如果硬把所有情況都寫進 __init__，
# 可能會變成：
# 1. 判斷傳入的是 int 還是 str
# 2. 判斷傳入的是 list 還是 tuple
# 3. 判斷是否要建立原點
#
# 這樣 __init__ 會變得難讀、難維護。
#
# 所以比較好的做法是：
# __init__ 只處理最基本、最乾淨的資料格式。
# 其他格式交給不同的 classmethod 來轉換。

# ── @classmethod 解法：每種格式一個工廠方法 ─────────────
class Point:
    # Point 類別用來表示二維座標點。
    #
    # 它最基本的資料是：
    # x 座標
    # y 座標
    #
    # 這個 class 的 __init__ 只負責接收已經整理好的 x 和 y。
    # 至於字串、list 或其他格式，
    # 則交給 classmethod 先轉換後再建立物件。

    def __init__(self, x, y):
        # __init__ 是建構子。
        #
        # 當執行 Point(3, 4) 時，
        # Python 會建立一個 Point 物件，
        # 然後自動呼叫 __init__。
        #
        # self 代表目前這個新建立出來的物件。
        # x 和 y 是外部傳入的座標值。
        self.x = x

        # 將 y 座標存進物件屬性。
        self.y = y

    def __repr__(self):
        # __repr__ 是物件的開發者表示法。
        #
        # 當我們直接印出 Point 物件，
        # 或在 list 裡顯示 Point 物件時，
        # 這個方法可以讓結果更清楚。
        #
        # 例如：
        # Point(3, 4)
        return f"Point({self.x}, {self.y})"

    @classmethod
    def from_string(cls, s):
        """從 '3,4' 這種字串建立 Point"""

        # @classmethod 讓這個方法可以直接用 class 呼叫：
        # Point.from_string("3,4")
        #
        # cls 就是「目前呼叫這個方法的 class」。
        #
        # 如果是 Point.from_string("3,4")，
        # cls 就是 Point。
        #
        # 如果是子類 ColoredPoint.from_string("5,6")，
        # cls 就會是 ColoredPoint。
        #
        # 這是 classmethod 在繼承時很重要的地方。
        # cls 就是「目前的 class 本身」，等於 Point

        # s.split(',') 會把字串按照逗號切開。
        #
        # 例如：
        # "3,4".split(',')
        # 會得到：
        # ["3", "4"]
        #
        # map(int, ...) 會把每個字串轉成整數。
        #
        # 所以：
        # map(int, ["3", "4"])
        # 會得到 3 和 4。
        #
        # 最後用 x, y 接收這兩個值。
        x, y = map(int, s.split(','))

        # return cls(x, y) 代表建立目前這個 class 的物件。
        #
        # 如果 cls 是 Point：
        # return Point(x, y)
        #
        # 如果 cls 是 ColoredPoint：
        # return ColoredPoint(x, y)
        #
        # 這比直接寫 Point(x, y) 更有彈性，
        # 因為它可以支援繼承。
        return cls(x, y)

    @classmethod
    def from_list(cls, lst):
        """從 [3, 4] 這種 list 建立 Point"""

        # 這個 classmethod 用來處理 list 格式的資料。
        #
        # 例如：
        # lst = [3, 4]
        #
        # lst[0] 是 x 座標。
        # lst[1] 是 y 座標。
        #
        # 一樣使用 cls(...) 建立物件，
        # 讓子類別呼叫時也可以建立子類別物件。
        return cls(lst[0], lst[1])

    @classmethod
    def origin(cls):
        """原點的工廠方法"""

        # 原點的座標固定是 (0, 0)。
        #
        # 這個方法讓外部可以寫：
        # Point.origin()
        #
        # 語意上比 Point(0, 0) 更清楚，
        # 因為它明確表示「我要建立原點」。
        #
        # 使用 cls(0, 0) 一樣是為了支援繼承。
        return cls(0, 0)

# 印出區塊標題，方便觀察 @classmethod 的多重構造器效果。
print("=== @classmethod 多重構造器 ===")

# 一般建立物件方式。
#
# 直接呼叫 Point(3, 4)，
# 會執行 Point.__init__(self, 3, 4)。
p1 = Point(3, 4)                   # 一般方式

# 使用 classmethod 從字串建立物件。
#
# Point.from_string("3,4") 會：
# 1. 把 "3,4" 切成 ["3", "4"]
# 2. 轉成整數 3 和 4
# 3. 呼叫 cls(3, 4)，也就是 Point(3, 4)
p2 = Point.from_string("3,4")     # 從字串

# 使用 classmethod 從 list 建立物件。
#
# Point.from_list([3, 4]) 會取：
# lst[0] = 3
# lst[1] = 4
#
# 然後呼叫 Point(3, 4) 建立物件。
p3 = Point.from_list([3, 4])      # 從 list

# 使用工廠方法建立原點。
#
# Point.origin() 會回傳 Point(0, 0)。
p4 = Point.origin()               # 工廠方法

# 印出四個 Point 物件。
#
# 因為 Point 有定義 __repr__，
# 所以印出時會顯示成 Point(x, y) 的格式。
print(p1, p2, p3, p4)

# ── cls 在繼承時很重要 ────────────────────────────────────
# from_string 繼承自 Point，但 cls 會指向「實際呼叫的 class」
#
# 這是 @classmethod 和直接寫 class 名稱最大的差異。
#
# 如果 from_string 裡面寫死：
# return Point(x, y)
#
# 那就算是 ColoredPoint.from_string("5,6")，
# 最後也只會建立 Point 物件。
#
# 但如果寫：
# return cls(x, y)
#
# 那 ColoredPoint.from_string("5,6") 呼叫時，
# cls 會是 ColoredPoint，
# 所以最後會建立 ColoredPoint 物件。

class ColoredPoint(Point):
    # ColoredPoint 繼承 Point。
    #
    # 它除了 x、y 座標之外，
    # 還多了一個 color 屬性。
    #
    # 因為它繼承 Point，
    # 所以可以使用 Point 裡面的 from_string、from_list、origin 等 classmethod。

    def __init__(self, x, y, color="black"):
        # ColoredPoint 的 __init__ 接收：
        # x
        # y
        # color
        #
        # color 有預設值 "black"。
        #
        # 如果建立 ColoredPoint 時只給 x 和 y，
        # color 就會自動使用 "black"。
        super().__init__(x, y)

        # super().__init__(x, y) 會呼叫父類別 Point 的 __init__，
        # 幫忙設定 self.x 和 self.y。
        #
        # 這樣不用重複寫：
        # self.x = x
        # self.y = y

        # 設定 ColoredPoint 額外的 color 屬性。
        self.color = color

    def __repr__(self):
        # 覆寫 __repr__。
        #
        # 因為 ColoredPoint 比 Point 多了 color，
        # 所以顯示時也要把 color 顯示出來。
        #
        # {self.color!r} 會用 repr 格式顯示 color，
        # 對字串來說會包含引號。
        return f"ColoredPoint({self.x}, {self.y}, color={self.color!r})"

# 印出繼承示範標題。
print("\n=== 繼承時 cls 指向子類 ===")

# ColoredPoint 沒有自己寫 from_string。
#
# 但是它繼承了 Point.from_string。
#
# 呼叫 ColoredPoint.from_string("5,6") 時：
# cls 會是 ColoredPoint，
# 不是 Point。
#
# 所以 from_string 裡的 return cls(x, y)
# 會變成 return ColoredPoint(5, 6)。
#
# 因為 ColoredPoint 的 color 有預設值 "black"，
# 所以可以只傳 x 和 y。
cp = ColoredPoint.from_string("5,6")

# 印出 cp。
#
# 因為 cp 是 ColoredPoint 物件，
# 所以會使用 ColoredPoint.__repr__。
print(cp)            # ColoredPoint(5, 6, color='black')

# 印出 cp 的型別。
#
# 可以確認 cp 不是 Point，
# 而是 ColoredPoint。
print(type(cp))      # <class '__main__.ColoredPoint'>，不是 Point！

# ── CPE 應用：UVA 11005 進位制物件 ──────────────────────
# 題目的輸入是一串成本值，可以用 classmethod 從字串建立
#
# UVA 11005 題目概念：
# 題目會給 36 個符號的成本。
#
# 這 36 個符號通常是：
# 0~9 和 A~Z。
#
# 每個符號都有一個印刷成本。
#
# 接著題目會給一些數字，
# 要計算這些數字在 2 進位到 36 進位下，
# 哪些進位的總印刷成本最低。
#
# 這裡用 CostTable class 管理成本表，
# 並示範如何用 classmethod 建立不同來源的成本表。

class CostTable:
    """儲存 36 個字元（0-9, A-Z）各自的印刷成本"""

    # CHARS 是類別屬性。
    #
    # 它屬於 CostTable 這個 class，
    # 不是某一個特定物件獨有。
    #
    # 這裡列出 36 進位可能用到的所有符號。
    CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, costs):
        # costs 是一個 list。
        #
        # 理論上長度應該是 36，
        # 分別代表：
        # 數字 0 的成本
        # 數字 1 的成本
        # ...
        # 數字 9 的成本
        # A 的成本
        # ...
        # Z 的成本
        self.costs = costs   # list，長度 36

    def cost_of(self, digit_index):
        # cost_of() 用來查詢某個數字符號的成本。
        #
        # digit_index 是數字符號的索引。
        #
        # 例如：
        # digit_index = 0 代表符號 0
        # digit_index = 10 代表符號 A
        # digit_index = 35 代表符號 Z
        #
        # self.costs[digit_index] 就是對應的成本。
        return self.costs[digit_index]

    def total_cost(self, n, base):
        """計算數字 n 在 base 進位下的總印刷成本"""

        # total_cost() 用來計算：
        # 整數 n 在 base 進位表示時，
        # 每一位數字的印刷成本總和。
        #
        # 例如：
        # n = 255, base = 16
        # 255 的 16 進位是 FF。
        # F 對應的 digit_index 是 15。
        # 所以總成本是 costs[15] + costs[15]。

        # 特別處理 n == 0。
        #
        # 數字 0 在任何進位下都表示成單一位數 0。
        # 所以成本就是 self.costs[0]。
        if n == 0:
            return self.costs[0]

        # total 用來累加每一位數字的成本。
        total = 0

        # 用短除法概念取得 n 在 base 進位下的每一位。
        #
        # n % base 會取得目前最低位的數字。
        # n //= base 會把最低位移除，繼續處理下一位。
        #
        # 例如 n = 255, base = 10：
        # 255 % 10 = 5
        # 255 // 10 = 25
        # 25 % 10 = 5
        # 25 // 10 = 2
        # 2 % 10 = 2
        # 2 // 10 = 0
        #
        # 所以 255 的各位數是 5、5、2。
        while n > 0:
            # n % base 是目前位數的 digit index。
            #
            # 例如 base=16 時，
            # 可能取得 0~15。
            #
            # 再用 self.costs[...] 查出該位數字的成本，
            # 並加到 total。
            total += self.costs[n % base]

            # 移除目前最低位。
            #
            # 讓下一輪處理更高一位。
            n //= base

        # 回傳總成本。
        return total

    @classmethod
    def uniform(cls, cost=1):
        """建立所有字元成本相同的表（方便測試）"""

        # uniform() 是工廠方法。
        #
        # 它用來快速建立「所有符號成本都一樣」的 CostTable。
        #
        # cost=1 表示如果沒有指定成本，
        # 預設每個符號的成本都是 1。
        #
        # [cost] * 36 會建立長度為 36 的 list，
        # 每個位置都是 cost。
        #
        # 使用 cls(...) 建立物件，
        # 讓未來如果有 CostTable 的子類別，
        # 也可以正確建立子類別物件。
        return cls([cost] * 36)

    @classmethod
    def from_flat_string(cls, s):
        """從一行 36 個整數（空白分隔）建立成本表"""

        # from_flat_string() 用來把輸入字串轉成成本表。
        #
        # 例如：
        # "1 2 3 4 ... "
        #
        # s.split() 會根據空白切割字串，
        # 得到一個字串 list。
        #
        # map(int, s.split()) 會把每個字串轉成整數。
        #
        # list(...) 則把 map 物件轉成真正的 list。
        values = list(map(int, s.split()))

        # 用解析後的 values 建立 CostTable 物件。
        #
        # 理論上 values 長度應該是 36。
        return cls(values)

# 印出 CPE 應用區塊標題。
print("\n=== CPE：進位制成本計算 ===")

# 建立一張所有字元成本都等於 1 的成本表。
#
# CostTable.uniform(1) 會呼叫 classmethod uniform。
#
# 回傳的 table 是 CostTable 物件，
# 且 table.costs 是 36 個 1。
table = CostTable.uniform(1)   # 每個字元成本都是 1

# 設定要測試的數字 n。
n = 255

# 測試 base 從 2 到 10。
#
# range(2, 11) 會產生：
# 2, 3, 4, 5, 6, 7, 8, 9, 10
for base in range(2, 11):
    # 計算 n 在目前 base 進位下的成本。
    #
    # 因為每個字元成本都是 1，
    # 所以這裡的成本其實等同於：
    # n 在該進位下需要幾個位數。
    c = table.total_cost(n, base)

    # 印出結果。
    #
    # {base:2d} 表示整數 base 至少佔 2 格寬度，
    # 可以讓輸出排列比較整齊。
    print(f"  255 在 {base:2d} 進位：位數 {c}")

# 記憶重點 ──────────────────────────────────────────────────
# @classmethod 的第一個參數是 cls（class 本身），不是 self（物件）
# cls(...)  等於  ClassName(...)，但繼承時會自動用子類
# 常用於：替代構造器、工廠方法、從不同格式解析資料
#
# 補充整理：
#
# 1. self
#    代表目前這個物件。
#    一般實例方法會用 self。
#
# 2. cls
#    代表目前呼叫方法的 class。
#    classmethod 會用 cls。
#
# 3. @classmethod
#    可以用 ClassName.method() 呼叫。
#    常用來提供不同的建立物件方式。
#
# 4. 工廠方法
#    指的是一個方法負責幫你建立物件。
#    它可以先解析資料、整理格式，再呼叫 cls(...)。
#
# 5. classmethod 的繼承優勢
#    如果子類別呼叫父類別的 classmethod，
#    cls 會是子類別，而不是固定父類別。
#
# 6. 使用 cls(...) 通常比寫死 ClassName(...) 更有彈性，
#    因為它比較支援繼承與擴充。