# U02. @classmethod：多重構造器（工廠方法）
# 讓 class 可以用「不同格式的資料」建立物件，不只是靠 __init__
# 對應 Bloom's Taxonomy：理解（Understand）— 能解釋 cls 的作用與繼承行為

# ── 問題：__init__ 只能有一種寫法 ────────────────────────
# 座標點可能來自不同地方：
#   - 直接給 (x, y)
#   - 從字串 "3,4" 解析
#   - 從 list [3, 4] 讀取
# 三種都用 __init__ 處理，會讓 __init__ 變得很複雜

# ── @classmethod 解法：每種格式一個工廠方法 ─────────────
class Point:
    def __init__(self, x, y):
        # 這是標準的初始化方法，只能接受 x 和 y 兩個明確的數值
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    @classmethod
    def from_string(cls, s):
        """從 '3,4' 這種字串建立 Point"""
        # cls 就是「目前的 class 本身」，等於 Point
        # 透過 split 將字串切開，再用 map 將其轉換為整數
        x, y = map(int, s.split(','))
        # return cls(x, y) 相當於 return Point(x, y)，負責把物件建出來
        return cls(x, y)

    @classmethod
    def from_list(cls, lst):
        """從 [3, 4] 這種 list 建立 Point"""
        # 直接提取 list 的第 0 項和第 1 項來當作 x 與 y 建立物件
        return cls(lst[0], lst[1])

    @classmethod
    def origin(cls):
        """原點的工廠方法"""
        # 不需要任何參數，直接回傳一個座標為 (0, 0) 的物件
        return cls(0, 0)

print("=== @classmethod 多重構造器 ===")
p1 = Point(3, 4)                   # 一般方式
p2 = Point.from_string("3,4")     # 從字串
p3 = Point.from_list([3, 4])      # 從 list
p4 = Point.origin()               # 工廠方法
print(p1, p2, p3, p4)

# ── cls 在繼承時很重要 ────────────────────────────────────
# from_string 繼承自 Point，但 cls 會指向「實際呼叫的 class」

class ColoredPoint(Point):
    def __init__(self, x, y, color="black"):
        # 先呼叫父類 (Point) 的 __init__ 來處理 x 和 y 的賦值
        super().__init__(x, y)
        self.color = color

    def __repr__(self):
        return f"ColoredPoint({self.x}, {self.y}, color={self.color!r})"

print("\n=== 繼承時 cls 指向子類 ===")
# 這裡呼叫的是從 Point 繼承來的 from_string，但因為是透過 ColoredPoint 呼叫的，
# 所以 from_string 裡面的 cls 會自動變成 ColoredPoint，回傳的也會是 ColoredPoint 物件！
# (注意：這裡能成功運作也是因為 ColoredPoint 的 __init__ 第三個參數 color 有預設值，所以 cls(x, y) 不會缺少參數報錯)
cp = ColoredPoint.from_string("5,6")
print(cp)            # ColoredPoint(5, 6, color='black')
print(type(cp))      # <class '__main__.ColoredPoint'>，不是 Point！

# ── CPE 應用：UVA 11005 進位制物件 ──────────────────────
# 題目的輸入是一串成本值，可以用 classmethod 從字串建立

class CostTable:
    """儲存 36 個字元（0-9, A-Z）各自的印刷成本"""

    CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, costs):
        self.costs = costs   # list，長度 36

    def cost_of(self, digit_index):
        return self.costs[digit_index]

    def total_cost(self, n, base):
        """計算數字 n 在 base 進位下的總印刷成本"""
        if n == 0:
            return self.costs[0]
        total = 0
        while n > 0:
            total += self.costs[n % base]
            n //= base
        return total

    @classmethod
    def uniform(cls, cost=1):
        """建立所有字元成本相同的表（方便測試）"""
        # 快速產生一個長度為 36 且內容全是 cost 的 list，並傳給 __init__
        return cls([cost] * 36)

    @classmethod
    def from_flat_string(cls, s):
        """從一行 36 個整數（空白分隔）建立成本表"""
        # 在解題時常遇到資料是由空白分隔的字串，這裡可以直接解析並建立出 CostTable 物件
        values = list(map(int, s.split()))
        return cls(values)

print("\n=== CPE：進位制成本計算 ===")
table = CostTable.uniform(1)   # 每個字元成本都是 1
n = 255
for base in range(2, 11):
    c = table.total_cost(n, base)
    print(f"  255 在 {base:2d} 進位：位數 {c}")

# 記憶重點 ──────────────────────────────────────────────────
# @classmethod 的第一個參數是 cls（class 本身），不是 self（物件）
# cls(...)  等於  ClassName(...)，但繼承時會自動用子類
# 常用於：替代構造器、工廠方法、從不同格式解析資料
