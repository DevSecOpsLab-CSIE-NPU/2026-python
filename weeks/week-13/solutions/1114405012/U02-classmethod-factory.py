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
    """二維座標點，示範使用 `@classmethod` 實作多重構造器（工廠方法）。

    設計動機：`__init__` 的簽章固定，但資料來源可能多樣（字串、list、tuple 等），
    使用 classmethod 可以為每種來源定義一個語意清晰的建構器，例如 `from_string`、`from_list`。
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    @classmethod
    def from_string(cls, s):
        """從字串 'x,y' 解析並建立一個 Point 實例。

        範例：Point.from_string('3,4') -> Point(3, 4)
        """
        # cls 就是「目前的 class 本身」，在直接呼叫時為 Point，但若在子類被呼叫則為子類
        x, y = map(int, s.split(','))
        return cls(x, y)

    @classmethod
    def from_list(cls, lst):
        """從長度至少為 2 的序列（list/tuple）建立 Point。"""
        return cls(lst[0], lst[1])

    @classmethod
    def origin(cls):
        """回傳原點 (0,0) 的工廠方法。語意清楚且易讀。"""
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
    """示範子類：加入 color 屬性，但仍能使用父類的 classmethod 來建立实例。

    重點是：當呼叫 `ColoredPoint.from_string(...)` 時，`cls` 會指向 `ColoredPoint`，
    因此回傳的會是 `ColoredPoint` 實例，而非 `Point`。
    """

    def __init__(self, x, y, color="black"):
        super().__init__(x, y)
        self.color = color

    def __repr__(self):
        return f"ColoredPoint({self.x}, {self.y}, color={self.color!r})"

print("\n=== 繼承時 cls 指向子類 ===")
cp = ColoredPoint.from_string("5,6")
print(cp)            # ColoredPoint(5, 6, color='black')
print(type(cp))      # <class '__main__.ColoredPoint'>，不是 Point！

# ── CPE 應用：UVA 11005 進位制物件 ──────────────────────
# 題目的輸入是一串成本值，可以用 classmethod 從字串建立

class CostTable:
    """儲存 36 個字元（0-9, A-Z）各自的印刷成本，示範 classmethod 在解析輸入時的應用。

    通常在競程題目中會把成本或一長串數值輸入為字串，使用 classmethod 來解析並建立 CostTable
    可讓主程式保持乾淨（解析邏輯封裝在類別內）。
    """

    CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, costs):
        # costs: list，長度應為 36，對應 CHARS 的每個字元成本
        self.costs = costs

    def cost_of(self, digit_index):
        return self.costs[digit_index]

    def total_cost(self, n, base):
        """計算整數 n 在指定 base 下的總印刷成本。

        以 n % base 取得最低位數，累加對應的成本，直到 n 為 0。
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
        """建立一個所有字元成本皆相同的 CostTable（測試或簡化情境用）。"""
        return cls([cost] * 36)

    @classmethod
    def from_flat_string(cls, s):
        """從一行由空白分隔的 36 個整數建立 CostTable。

        範例輸入："1 2 3 ..."（共 36 個值）
        """
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
