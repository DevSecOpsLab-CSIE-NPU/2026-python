# U02. @classmethod：多重構造器（工廠方法）
# =============================================================================
# 什麼是 @classmethod？
#   @classmethod 是一個裝飾器，讓方法可以透過「類別本身」來呼叫，
#   而不是透過「類別的實例（物件）」。
#
# 為什麼需要？
#   一個 class 通常只有一個 __init__ 構造器。
#   但物件的來源可能有很多種：
#     - 直接給參數（一般的 __init__）
#     - 從字串解析（例如 "3,4" → Point(3, 4)）
#     - 從檔案讀取（例如 JSON、CSV）
#     - 從資料庫查詢
#     - 建立預設物件（例如原點、單位圓）
#
#   @classmethod 讓我們可以為每種來源建立一個「工廠方法」，
#   而不需要把解析邏輯塞進 __init__。
#
# 和 @staticmethod 的差別：
#   @classmethod：第一個參數是 cls（類別本身），可以呼叫 cls(...) 建立物件
#   @staticmethod：沒有 cls，就像一般的函數，只是放在 class 裡面
#
# 對應 Bloom's Taxonomy：理解（Understand）— 能解釋 cls 的作用與繼承行為
# =============================================================================


# ═════════════════════════════════════════════════════════════════════════════
# 問題：__init__ 只能有一種寫法
# ═════════════════════════════════════════════════════════════════════════════
# 假設我們要建立一個座標點 Point：
#   - 直接給 (x, y)：Point(3, 4)
#   - 從字串 "3,4" 解析
#   - 從 list [3, 4] 讀取
#   - 建立一個原點 (0, 0)
#
# 如果不使用 @classmethod，可能的作法有問題：
#   1. 全部塞進 __init__：用 type() 判斷傳入的型別
#      缺點：__init__ 會變得很複雜，難以維護
#   2. 用外部函數：parse_point_from_string(s)
#      缺點：函數不在 class 裡，語意不清
#   3. 用 @classmethod：每個工廠方法各自獨立，乾淨整潔 ✓


# ═════════════════════════════════════════════════════════════════════════════
# @classmethod 解法：每種格式一個工廠方法
# ═════════════════════════════════════════════════════════════════════════════

class Point:
    """座標點 class，支援多種建立方式

    核心概念：
        __init__ 只處理最基本的「直接給 x, y」的情況
        其他建立方式用 @classmethod 封裝成工廠方法
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    @classmethod
    def from_string(cls, s):
        """從 '3,4' 這種字串建立 Point

        參數：
            cls：目前的 class 本身（可能是 Point，也可能是子類）
            s：格式為 "x,y" 的字串

        流程：
            1. 用 split(',') 切割字串 → ['3', '4']
            2. 用 map(int, ...) 轉成整數 → [3, 4]
            3. 用 cls(x, y) 建立物件（注意是用 cls，不是 Point！）

        為什麼用 cls 而不是 Point？
            因為繼承時，cls 會自動指向「實際被呼叫的 class」
            如果用 Point，子類呼叫 from_string 時會產出錯誤的型別
        """
        x, y = map(int, s.split(','))
        return cls(x, y)

    @classmethod
    def from_list(cls, lst):
        """從 [3, 4] 這種 list 建立 Point"""
        return cls(lst[0], lst[1])

    @classmethod
    def origin(cls):
        """原點的工廠方法

        不需要任何參數，直接建立 (0, 0)
        這是一個典型的「預設值工廠」
        """
        return cls(0, 0)

print("=== @classmethod 多重構造器 ===")
p1 = Point(3, 4)                   # 一般方式：直接給 x, y
p2 = Point.from_string("3,4")     # 從字串解析
p3 = Point.from_list([3, 4])      # 從 list 讀取
p4 = Point.origin()               # 工廠方法：建立原點
print(p1, p2, p3, p4)


# ═════════════════════════════════════════════════════════════════════════════
# cls 在繼承時很重要
# ═════════════════════════════════════════════════════════════════════════════
# 這是最重要的觀念！
# 在 @classmethod 中使用 cls 而不是直接用 class 名稱的原因：
#
#   假設我們有 class Point 和 class ColoredPoint(Point)
#   如果 ColoredPoint 沒有覆寫 from_string，
#   呼叫 ColoredPoint.from_string("5,6") 時：
#
#     - cls = ColoredPoint（因為是 ColoredPoint 呼叫的）
#     - cls(x, y) = ColoredPoint(x, y) → 建立 ColoredPoint 物件
#
#   但如果 from_string 寫死成 Point(x, y)：
#     - 會建立 Point 物件，而不是 ColoredPoint 物件
#     - 型別錯誤！

class ColoredPoint(Point):
    """有顏色的點：繼承 Point，新增 color 屬性"""
    def __init__(self, x, y, color="black"):
        super().__init__(x, y)
        self.color = color

    def __repr__(self):
        return f"ColoredPoint({self.x}, {self.y}, color={self.color!r})"

print("\n=== 繼承時 cls 指向子類 ===")
cp = ColoredPoint.from_string("5,6")
print(cp)            # ColoredPoint(5, 6, color='black')
print(type(cp))      # <class '__main__.ColoredPoint'>，不是 Point！

# 如果 Point.from_string 寫的是 return Point(x, y) 而不是 cls(x, y)，
# 這裡會回傳 Point 物件，完全失去 ColoredPoint 的資訊
# 這就是為什麼 @classmethod 一定要用 cls


# ═════════════════════════════════════════════════════════════════════════════
# CPE 應用：UVA 11005 進位制物件
# ═════════════════════════════════════════════════════════════════════════════
# 題目描述：
#   給定 36 個字元（0-9, A-Z）各自的印刷成本，
#   問某個數字在不同進位下，哪個進位的成本最低。
#
# 使用 @classmethod 的好處：
#   輸入的格式可能不同：
#     1. 測試時：所有字元成本相同（方便驗證）
#     2. 正式輸入：一行 36 個整數
#   我們用不同的 @classmethod 處理不同的輸入格式

class CostTable:
    """儲存 36 個字元（0-9, A-Z）各自的印刷成本

    屬性：
        costs：長度 36 的 list，costs[i] 代表第 i 個字元的成本
        CHARS：類別變數，字元對照表
    """
    CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, costs):
        """最基本的構造器：直接接收成本 list

        參數：
            costs：長度 36 的 list
        """
        self.costs = costs

    def cost_of(self, digit_index):
        """查詢某個字元的成本

        參數：
            digit_index：字元的索引（0~35）
        回傳：
            該字元的印刷成本
        """
        return self.costs[digit_index]

    def total_cost(self, n, base):
        """計算數字 n 在 base 進位下的總印刷成本

        演算法：重複對 base 取餘數
        例如 n=255, base=16：
            255 % 16 = 15（對應字元 F）
            255 // 16 = 15
            15 % 16 = 15（對應字元 F）
            15 // 16 = 0（結束）
            所以 255 在 16 進位是 FF，成本 = costs[15] + costs[15]

        參數：
            n：要計算的數字（十進位）
            base：目標進位（2~36）
        """
        if n == 0:
            return self.costs[0]
        total = 0
        while n > 0:
            total += self.costs[n % base]
            n //= base
        return total

    @classmethod
    def uniform(cls, cost=1):
        """建立所有字元成本相同的成本表

        用途：方便測試和示範
        參數：
            cost：每個字元的成本（預設 1）
        回傳：
            CostTable 實例
        """
        return cls([cost] * 36)

    @classmethod
    def from_flat_string(cls, s):
        """從一行 36 個整數（空白分隔）建立成本表

        用途：處理正式題目的輸入
        參數：
            s：包含 36 個整數的字串，例如 "1 2 3 ... 36"
        回傳：
            CostTable 實例
        """
        values = list(map(int, s.split()))
        return cls(values)

print("\n=== CPE：進位制成本計算 ===")
table = CostTable.uniform(1)   # 每個字元成本都是 1
n = 255
for base in range(2, 11):
    c = table.total_cost(n, base)
    print(f"  255 在 {base:2d} 進位：位數 {c}")


# ═════════════════════════════════════════════════════════════════════════════
# 記憶重點
# ═════════════════════════════════════════════════════════════════════════════
# 1. @classmethod 的特性：
#    - 第一個參數是 cls（class 本身），不是 self（物件實例）
#    - 可以透過 cls(...) 建立物件
#    - 不需要實例就可以呼叫（ClassName.factory()）
#
# 2. cls vs 直接寫 ClassName：
#    - 用 cls 才能在繼承時正確建立子類的物件
#    - 寫死 ClassName 會破壞繼承行為
#    - 這是 @classmethod 最重要的設計理念
#
# 3. 常見應用：
#    - 替代構造器（從不同格式解析輸入）
#    - 工廠方法（建立預設物件、測試物件）
#    - 類別層級的查詢或計算（不需要實例）
#
# 4. @classmethod vs @staticmethod：
#    - @classmethod：有關 cls，可以建立物件
#    - @staticmethod：沒有 cls，就像普通函數
#    - 如果你的方法完全不需要 cls，用 @staticmethod
#    - 如果你的方法需要建立 cls 的實例，用 @classmethod
