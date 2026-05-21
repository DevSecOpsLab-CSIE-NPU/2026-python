# U02. @classmethod：多重構造器（工廠方法）
# 說明：
# 本範例示範如何使用 @classmethod 為同一個類別提供多種建構方式，
# 例如從字串、從列表或從預設值建立物件。這種做法能讓 __init__ 保持精簡，
# 並把解析不同格式的邏輯獨立到專責的工廠方法（factory methods）。


# ---------- 範例：Point 類別與多種工廠方法 ----------
class Point:
    """
    二維座標點的簡單類別，示範常見的 classmethod 工廠方法：
    - from_string: 由 'x,y' 形式的字串建立
    - from_list:   由 [x, y] 形式的序列建立
    - origin:      建立原點 (0, 0)

    注意：classmethod 的第一個參數為 cls，代表呼叫時的類別，這在繼承時特別重要。
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    @classmethod
    def from_string(cls, s):
        """從 '3,4' 這種字串建立 Point。cls 代表目前的類別（callable）。"""
        x, y = map(int, s.split(','))
        return cls(x, y)

    @classmethod
    def from_list(cls, lst):
        """從 [3, 4] 這種 list 或 tuple 建立 Point，支援序列輸入。"""
        return cls(lst[0], lst[1])

    @classmethod
    def origin(cls):
        """回傳原點 (0,0) 的工廠方法，語意比直接呼叫 Point(0,0) 更清楚。"""
        return cls(0, 0)


print("=== @classmethod 多重構造器 ===")
p1 = Point(3, 4)                   # 一般方式
p2 = Point.from_string("3,4")     # 從字串建立
p3 = Point.from_list([3, 4])      # 從 list 建立
p4 = Point.origin()               # 工廠方法
print(p1, p2, p3, p4)


# ---------- 繼承時 cls 的重要性 ----------
# 當子類繼承父類的 classmethod 時，cls 會指向「呼叫方法的類別」，
# 因此從子類呼叫工廠方法會建立出子類的實例（而非父類），這使得工廠方法在繼承體系中行為自然。
class ColoredPoint(Point):
    def __init__(self, x, y, color="black"):
        super().__init__(x, y)
        self.color = color

    def __repr__(self):
        return f"ColoredPoint({self.x}, {self.y}, color={self.color!r})"


print("\n=== 繼承時 cls 指向子類 ===")
cp = ColoredPoint.from_string("5,6")
print(cp)            # ColoredPoint(5, 6, color='black')
print(type(cp))      # <class '__main__.ColoredPoint'>，代表從子類呼叫會建立子類實例



# ---------- CPE 應用：進位制成本的 CostTable 類別 ----------
# 說明：競賽題目常會將一行數字解析成一個成本表，利用 classmethod 可以直接從字串建立 CostTable。
class CostTable:
    """儲存 36 個字元（0-9, A-Z）各自的印刷成本"""

    CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, costs):
        # costs 預期為長度 36 的整數清單，索引對應 CHARS
        self.costs = costs

    def cost_of(self, digit_index):
        return self.costs[digit_index]

    def total_cost(self, n, base):
        """計算整數 n 在 base 進位下的總印刷成本，使用整數運算取得每位的數字索引。"""
        if n == 0:
            return self.costs[0]
        total = 0
        while n > 0:
            total += self.costs[n % base]
            n //= base
        return total

    @classmethod
    def uniform(cls, cost=1):
        """快速建立一個所有字元成本相同的 CostTable（測試/預設用途）。"""
        return cls([cost] * 36)

    @classmethod
    def from_flat_string(cls, s):
        """從一行以空白分隔的 36 個整數建立成本表（方便讀入單行輸入）。"""
        values = list(map(int, s.split()))
        return cls(values)


print("\n=== CPE：進位制成本計算 ===")
table = CostTable.uniform(1)   # 每個字元成本都是 1
n = 255
for base in range(2, 11):
    c = table.total_cost(n, base)
    print(f"  255 在 {base:2d} 進位：位數 {c}")


# 記憶重點 ──────────────────────────────────────────────────
# - @classmethod 的第一個參數是 cls（類別本身），不是 self
# - 在 classmethod 中使用 cls(...) 等同於呼叫該類別的建構器，對繼承友好
# - 常見用途：替代構造器（from_string/from_list）、工廠方法、從不同格式解析資料
