# U02. @classmethod：多重構造器（工廠方法）
# 讓類別 (class) 可以根據「不同格式的來源資料」建立物件，而不僅僅依賴 __init__。
# 對應 Bloom's Taxonomy：理解 (Understand) — 能解釋 cls 的作用，並理解繼承時的行為差異。

# ── 問題情境：__init__ 的限制 ────────────────────────
# 一個座標點物件 Point(x, y) 可能來自多種輸入：
#   - 直接傳入整數 (x, y)
#   - 從字串 "3,4" 解析而來
#   - 從串列 [3, 4] 讀取而來
# 如果全部邏輯都塞在 __init__ 裡，會讓初始化程式碼變得臃腫且難以維護。

# ── @classmethod 解法：為每種格式提供專屬的「工廠方法」 ─────────────
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    @classmethod
    def from_string(cls, s):
        """從 '3,4' 這種字串格式建立 Point 物件"""
        # cls 代表「目前的類別本身」，在此處等同於 Point
        # 優點：即使類別名稱修改了，這段程式碼也不用動
        x, y = map(int, s.split(','))
        return cls(x, y)

    @classmethod
    def from_list(cls, lst):
        """從 [3, 4] 這種串列格式建立 Point 物件"""
        return cls(lst[0], lst[1])

    @classmethod
    def origin(cls):
        """快速建立一個位於原點 (0, 0) 的 Point 物件"""
        return cls(0, 0)

print("=== @classmethod 多重構造器展示 ===")
p1 = Point(3, 4)                   # 標準初始化
p2 = Point.from_string("3,4")     # 透過字串工廠
p3 = Point.from_list([3, 4])      # 透過串列工廠
p4 = Point.origin()               # 透過預設值工廠
print(f"p1: {p1}, p2: {p2}, p3: {p3}, p4: {p4}")

# ── 為什麼要用 cls 而不是直接寫 Point？（繼承的重要性） ───────────────
# 當子類繼承父類時，cls 會自動指向「實際呼叫的子類」，確保回傳正確型別。

class ColoredPoint(Point):
    def __init__(self, x, y, color="black"):
        super().__init__(x, y)
        self.color = color

    def __repr__(self):
        return f"ColoredPoint({self.x}, {self.y}, color={self.color!r})"

print("\n=== 繼承時 cls 會動態指向子類 ===")
# 呼叫父類的 from_string，但因為是用 ColoredPoint 呼叫，cls 會是 ColoredPoint
cp = ColoredPoint.from_string("5,6")
print(f"物件內容：{cp}")
print(f"物件型別：{type(cp)}")      # 輸出為 <class '__main__.ColoredPoint'>，符合預期

# ── CPE 實務應用：UVA 11005 進位制成本計算 ──────────────────
# 題目的輸入通常是連在一起的數據，可以用 classmethod 封裝解析邏輯。

class CostTable:
    """儲存 36 個進位字元 (0-9, A-Z) 各自的印刷成本"""

    CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, costs):
        self.costs = costs   # 儲存 36 個整數的成本清單

    def total_cost(self, n, base):
        """計算數字 n 在 base 進位制下的總成本"""
        if n == 0:
            return self.costs[0]
        total = 0
        while n > 0:
            total += self.costs[n % base]
            n //= base
        return total

    @classmethod
    def uniform(cls, cost=1):
        """快速建立一個「所有字元成本均相同」的表格（便於測試）"""
        return cls([cost] * 36)

    @classmethod
    def from_flat_string(cls, s):
        """從一行由空白分隔的 36 個整數字串建立成本表"""
        values = list(map(int, s.split()))
        return cls(values)

print("\n=== CPE 模擬：進位制成本計算 ===")
# 模擬題目輸入格式
raw_input = "10 8 12 13 15 13 13 13 13 13 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10"
table = CostTable.from_flat_string(raw_input)

n = 255
print(f"數字 {n} 在不同進位下的成本：")
for base in [2, 10, 16]:
    c = table.total_cost(n, base)
    print(f"  {base:2d} 進位：成本為 {c}")

# 記憶重點 ──────────────────────────────────────────────────
# 1. @classmethod 的第一個參數是 cls (類別本身)，而非 self (物件實體)。
# 2. 核心用途：提供「替代建構子」，支援從多元格式 (JSON, CSV, DB) 初始化。
# 3. 繼承優勢：使用 cls(...) 而非類別名(...)，可確保子類調用時回傳子類實例。
# 4. 語意化：比起複雜的 __init__ 判斷，Point.from_string() 讓程式意圖更清晰。
