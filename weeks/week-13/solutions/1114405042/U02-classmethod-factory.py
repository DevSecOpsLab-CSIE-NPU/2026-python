"""
U02. @classmethod：多重構造器（工廠方法）

說明：示範如何用 `@classmethod` 實作多種建構方式（工廠方法），
讓類別可以接受不同格式的輸入（例如字串、list），並說明 `cls` 在
繼承時會指向呼叫的實際類別（讓工廠方法可被子類正確繼承）。
"""


# ── 例子：Point 類別搭配多個 classmethod 工廠方法 ─────────────
class Point:
    """簡單的座標點類別，示範 `@classmethod` 的多重構造器用法。"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    @classmethod
    def from_string(cls, s):
        """從 "3,4" 這種字串建立 Point。

        參數：
        - cls: 呼叫該方法的 class（不是實例），可用來在繼承時建立子類物件
        - s: 逗號分隔的數字字串
        """
        x, y = map(int, s.split(','))
        return cls(x, y)

    @classmethod
    def from_list(cls, lst):
        """從 [3, 4] 這種 list 建立 Point（直接取前兩個元素）。"""
        return cls(lst[0], lst[1])

    @classmethod
    def origin(cls):
        """回傳原點 (0,0) 的工廠方法。"""
        return cls(0, 0)

print("=== @classmethod 多重構造器 ===")
p1 = Point(3, 4)                   # 一般建構
p2 = Point.from_string("3,4")     # 從字串
p3 = Point.from_list([3, 4])      # 從 list
p4 = Point.origin()               # 工廠方法
print(p1, p2, p3, p4)


# ── 繼承時 cls 的重要性：工廠方法會回傳呼叫方的類別實例 ─────────
class ColoredPoint(Point):
    """帶顏色的點，示範子類繼承自 Point 的工廠方法仍建立子類實例。"""

    def __init__(self, x, y, color="black"):
        super().__init__(x, y)
        self.color = color

    def __repr__(self):
        return f"ColoredPoint({self.x}, {self.y}, color={self.color!r})"

print("\n=== 繼承時 cls 指向子類 ===")
cp = ColoredPoint.from_string("5,6")
print(cp)            # ColoredPoint(5, 6, color='black')
print(type(cp))      # <class '__main__.ColoredPoint'>，不是 Point！


# ── CPE 應用：以 classmethod 解析進位成本輸入（UVA 11005 範例）────
class CostTable:
    """儲存 36 個字元（0-9, A-Z）各自的印刷成本，並提供計算方法。"""

    CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, costs):
        # costs 應為長度 36 的 list，index 對應到 CHARS 的位置
        self.costs = costs

    def cost_of(self, digit_index):
        """回傳指定索引（數字/字元）對應的成本。"""
        return self.costs[digit_index]

    def total_cost(self, n, base):
        """計算整數 n 在 base 進位下的總印刷成本。

        若 n 為 0，回傳 costs[0]；否則逐位取餘累加成本。
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
        """建立所有字元成本相同的 CostTable（方便測試）。"""
        return cls([cost] * 36)

    @classmethod
    def from_flat_string(cls, s):
        """從一行 36 個整數（以空白分隔）建立成本表。

        範例輸入："1 2 3 ..."（共 36 個數字）
        """
        values = list(map(int, s.split()))
        return cls(values)

print("=== CPE：進位制成本計算 ===")
table = CostTable.uniform(1)   # 每個字元成本都是 1
n = 255
for base in range(2, 11):
    c = table.total_cost(n, base)
    print(f"  255 在 {base:2d} 進位：位數 {c}")


# 記憶重點 ──────────────────────────────────────────────────
# - @classmethod 的第一個參數是 cls（代表 class 本身），不是 self（實例）
# - 在 classmethod 內用 cls(...) 建立新物件，可確保在繼承時回傳子類實例
# - 常見用途：替代構造器、工廠方法、從不同格式解析資料
