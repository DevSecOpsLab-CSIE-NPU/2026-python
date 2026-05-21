# ===================================================================
# U02. @classmethod：多重構造器（工廠方法）
# 學生：賴俋勳 1114405041
# 日期：2026-05-21
# 主題：@classmethod — 讓 class 支援多種資料格式的建立方式
# ===================================================================
# 【學習心得】
#   @classmethod 的第一個參數是 cls（class 本身），不是 self（物件）。
#   呼叫時用 ClassName.method()，不需要先建立物件。
#   最常用於「工廠方法（Factory Method）」模式：
#   當資料可能從不同格式（字串、list、dict）傳入時，
#   各自定義一個 classmethod，保持 __init__ 的簡單。
#   
#   與 @staticmethod 的差異：
#   @classmethod  → 第一個參數是 cls，繼承時自動用子類
#   @staticmethod → 沒有 cls，只是放在 class 裡的普通函數
# ===================================================================

# ── 問題：__init__ 只能有一種簽章 ────────────────────────
# 座標點可能來自不同地方：直接給 (x, y) / 從字串 "3,4" / 從 list [3, 4]。
# 如果全塞在 __init__ 裡，程式碼會很複雜。
# @classmethod 讓每種格式都有自己清晰的入口。

class Point:
    def __init__(self, x, y):
        """基本構造器：直接給 x, y 座標"""
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    @classmethod
    def from_string(cls, s):
        """
        工廠方法：從 '3,4' 這種字串建立 Point。
        cls → 就是 Point 這個 class，等於 Point(x, y)。
        繼承時 cls 會是子類，所以 cls(x, y) 建立的是子類物件。
        """
        x, y = map(int, s.split(','))   # '3,4' → [3, 4] → x=3, y=4
        return cls(x, y)               # 等同於 Point(3, 4)

    @classmethod
    def from_list(cls, lst):
        """工廠方法：從 [3, 4] 這種 list 建立 Point"""
        return cls(lst[0], lst[1])

    @classmethod
    def origin(cls):
        """工廠方法：建立原點 (0, 0)"""
        return cls(0, 0)

print("=== @classmethod 多重構造器 ===")
p1 = Point(3, 4)                   # 一般 __init__
p2 = Point.from_string("3,4")     # 從字串格式
p3 = Point.from_list([3, 4])      # 從 list 格式
p4 = Point.origin()               # 特殊工廠方法
print(p1, p2, p3, p4)             # Point(3, 4) Point(3, 4) Point(3, 4) Point(0, 0)

# ── cls 在繼承時很重要 ─────────────────────────────────────
# 若 from_string 裡用 Point(x, y)（硬編碼），
# 子類呼叫時會建立 Point 物件，而不是子類物件。
# 用 cls(x, y) 就能讓繼承時自動建立子類物件。

class ColoredPoint(Point):
    def __init__(self, x, y, color="black"):
        super().__init__(x, y)   # 呼叫父類 __init__ 設定 x, y
        self.color = color

    def __repr__(self):
        return f"ColoredPoint({self.x}, {self.y}, color={self.color!r})"

print("\n=== 繼承時 cls 指向子類 ===")
# 呼叫的是 ColoredPoint.from_string（繼承自 Point）
# from_string 裡的 cls = ColoredPoint
# 所以 cls("5,6") 實際上是 ColoredPoint(5, 6)
cp = ColoredPoint.from_string("5,6")
print(cp)            # ColoredPoint(5, 6, color='black')
print(type(cp))      # <class '__main__.ColoredPoint'>，不是 Point！

# ── CPE 應用：UVA 11005 進位制物件 ──────────────────────
# 題目輸入是一串成本值，用 classmethod 從字串直接建立物件。

class CostTable:
    """儲存 36 個字元（0-9, A-Z）各自的印刷成本"""

    CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, costs):
        """costs：長度為 36 的 list，對應 0-9 A-Z 的成本"""
        self.costs = costs

    def cost_of(self, digit_index):
        """回傳第 digit_index 個字元的成本"""
        return self.costs[digit_index]

    def total_cost(self, n, base):
        """
        計算整數 n 在 base 進位制下的總印刷成本。
        做法：不斷取 n % base（最低位），查成本表加總，再右移一位。
        """
        if n == 0:
            return self.costs[0]   # 0 只有一個位數：字元 '0'
        total = 0
        while n > 0:
            total += self.costs[n % base]  # 最低位字元的成本
            n //= base                     # 去掉最低位（右移）
        return total

    @classmethod
    def uniform(cls, cost=1):
        """
        工廠方法：建立所有字元成本相同的表（測試用）。
        cls 是 CostTable，所以 cls([cost]*36) = CostTable([cost]*36)。
        """
        return cls([cost] * 36)

    @classmethod
    def from_flat_string(cls, s):
        """
        工廠方法：從一行 36 個整數（空白分隔）建立成本表。
        實際 UVA 11005 題目的輸入格式就是這樣。
        """
        values = list(map(int, s.split()))
        return cls(values)

print("\n=== CPE：進位制成本計算 ===")
table = CostTable.uniform(1)   # 每個字元成本都是 1（測試用）
n = 255
for base in range(2, 11):
    c = table.total_cost(n, base)
    print(f"  255 在 {base:2d} 進位：總成本 {c}")

# ─── 記憶重點 ──────────────────────────────────────────────
# @classmethod 的第一個參數是 cls（class 本身），不是 self（物件）
# cls(...)  等於  ClassName(...)，但繼承時會自動用子類
# 常用於：替代構造器、工廠方法、從不同格式解析資料
# @staticmethod 沒有 cls，只是放在 class 裡的普通函數
