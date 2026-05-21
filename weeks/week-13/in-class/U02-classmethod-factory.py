# U02. @classmethod：多重構造器（工廠方法）
# 範例與詳細說明（繁體中文）：
# 背景：當需要從不同來源或不同格式建立物件時，若把所有解析邏輯塞進 `__init__`，會讓建構子過於複雜。
# 解法：把不同來源的解析邏輯拆成多個 `@classmethod`（工廠方法），讓 `__init__` 保持單一職責（只負責初始化內部狀態）。
# 要點：
# - `@classmethod` 的第一個參數是 `cls`（指向類別本身），使用 `cls(...)` 建立物件能在繼承時保持多態性，
#   也就是子類呼叫父類的 classmethod 時會回傳子類的實例。
# - 與 `@staticmethod` 不同：`classmethod` 接收 class（可用來建立或存取 class 屬性）；`staticmethod` 則不接收任何隱藏參數。
# - 設計建議：把資料解析/驗證寫在 classmethod 工廠內，`__init__` 僅接收已驗證的原始參數。

# ── 問題：__init__ 只能有一種寫法 ────────────────────────
# 座標點可能來自不同地方：
#   - 直接給 (x, y)
#   - 從字串 "3,4" 解析
#   - 從 list [3, 4] 讀取
# 三種都用 __init__ 處理，會讓 __init__ 變得很複雜

# ── @classmethod 解法：每種格式一個工廠方法 ─────────────
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    @classmethod
    def from_string(cls, s):
        """從 '3,4' 這種字串建立 `Point`。

        範例說明：傳入字串 "3,4"，此方法會解析並回傳 `cls(x, y)`。
        使用 `cls` 而非直接呼叫 `Point` 可以讓此工廠方法在子類被呼叫時回傳子類的實例，
        保持在繼承情境下的多態性。
        """
        # cls 就是「目前的 class 本身」，在子類呼叫時會是子類
        x, y = map(int, s.split(','))
        return cls(x, y)

    @classmethod
    def from_list(cls, lst):
        """從 [3, 4] 這種 list 建立 `Point`。

        備註：若 list 長度或型別可能不正確，建議在此處加入驗證並拋出適當的例外。
        """
        return cls(lst[0], lst[1])

    @classmethod
    def origin(cls):
        """回傳原點 (0,0) 的工廠方法。

        用途：當需要一個語意化的建構子（例如 `Point.origin()`）時，可以提高程式可讀性。
        """
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
        super().__init__(x, y)
        self.color = color

    def __repr__(self):
        return f"ColoredPoint({self.x}, {self.y}, color={self.color!r})"

print("\n=== 繼承時 cls 指向子類 ===")
cp = ColoredPoint.from_string("5,6")
print(cp)            # ColoredPoint(5, 6, color='black')
print(type(cp))      # <class '__main__.ColoredPoint'>，不是 Point！

# 補充說明：
# - 如果 `from_string` 內部直接寫成 `return Point(x, y)`，那麼子類 `ColoredPoint.from_string`
#   呼叫時也會回傳 `Point` 實例，導致多態性喪失。
# - 使用 `cls(...)` 可以確保工廠方法在繼承時仍會回傳正確的類別實例，對於需要被繼承的 API 設計非常重要。

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
        """計算整數 n 在 base（2..36）進位下，每一位數字的總印刷成本。"""
        if n == 0:
            return self.costs[0]
        total = 0
        while n > 0:
            total += self.costs[n % base]
            n //= base
        return total

    @classmethod
    def uniform(cls, cost=1):
        """建立所有字元成本相同的表（方便測試）。

        範例用途：在單元測試或示範時，快速建立成本一致的 `CostTable`。
        """
        return cls([cost] * 36)

    @classmethod
    def from_flat_string(cls, s):
        """從一行包含 36 個整數的字串建立成本表（每個整數以空白分隔）。

        回傳 `CostTable` 實例，適合將題目的輸入直接傳給此方法解析。建議在呼叫前
        檢查字串是否包含足夠的整數，或在此處加入驗證與錯誤處理。
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
# - @classmethod 的第一個參數是 cls（class 本身），用 cls(...) 建立物件能保持繼承的多態性
# - 與 @staticmethod 的差別：classmethod 會接收 class（可建立實例或存取 class 屬性），staticmethod 不接收任何隱藏參數
# - 常見用途：替代構造器（如 from_string/from_list）、工廠方法、從不同格式解析資料
# - 設計建議：將資料解析與驗證邏輯放在 classmethod，可讓 __init__ 保持簡潔且易於測試
# - 設計建議：將資料解析與驗證邏輯放在 `classmethod`，可讓 `__init__` 保持簡潔且易於測試
# - 補充建議：若工廠方法接收外部輸入（例如字串），務必在工廠方法中做輸入驗證並回傳明確的錯誤資訊，
#   這樣比在 `__init__` 中混合解析與初始化更容易除錯與單元測試。
