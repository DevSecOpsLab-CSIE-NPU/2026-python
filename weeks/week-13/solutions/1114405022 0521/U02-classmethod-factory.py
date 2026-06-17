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
    """二維座標點，示範多種構造方式"""

    def __init__(self, x, y):
        """基本的建構子：直接接受 x, y 兩個座標"""
        self.x = x  # x 軸座標
        self.y = y  # y 軸座標

    def __repr__(self):
        """開發者導向的字串表示"""
        return f"Point({self.x}, {self.y})"

    @classmethod
    def from_string(cls, s):
        """
        從字串建立 Point 的工廠方法
        cls：就是 Point 這個 class 本身（或繼承 Point 的子類）
        s：格式為 "x,y" 的字串，例如 "3,4"
        """
        # 用 split(',') 將字串以逗號分割，再用 map(int, ...) 轉成整數
        x, y = map(int, s.split(','))
        return cls(x, y)   # 相當於 Point(x, y)，但使用 cls 以支援繼承

    @classmethod
    def from_list(cls, lst):
        """
        從 list 建立 Point 的工廠方法
        lst：兩個元素的列表，例如 [3, 4]
        """
        return cls(lst[0], lst[1])  # 取出列表的第一、二個元素作為 x, y

    @classmethod
    def origin(cls):
        """
        建立原點 (0, 0) 的工廠方法
        不需要任何參數，固定建立 (0, 0)
        """
        return cls(0, 0)   # 建立並回傳原點

print("=== @classmethod 多重構造器 ===")
p1 = Point(3, 4)                   # 一般方式：直接給 x, y
p2 = Point.from_string("3,4")     # 從字串 "3,4" 解析出 x=3, y=4
p3 = Point.from_list([3, 4])      # 從列表 [3, 4] 讀取
p4 = Point.origin()               # 工廠方法：直接得到 (0, 0)
print(p1, p2, p3, p4)             # 全部都是 Point(3, 4)，但 p4 是 Point(0, 0)

# ── cls 在繼承時很重要 ────────────────────────────────────
# from_string 繼承自 Point，但 cls 會指向「實際呼叫的 class」

class ColoredPoint(Point):
    """有顏色的座標點，繼承 Point 並新增 color 屬性"""

    def __init__(self, x, y, color="black"):
        """
        建構子：除了 x, y 之外還有顏色
        color 預設為 "black"
        """
        super().__init__(x, y)    # 呼叫父類別 Point 的 __init__ 設定 x, y
        self.color = color        # 設定顏色屬性

    def __repr__(self):
        """覆寫 __repr__，加入顏色資訊"""
        return f"ColoredPoint({self.x}, {self.y}, color={self.color!r})"

print("\n=== 繼承時 cls 指向子類 ===")
# 透過 ColoredPoint 呼叫 from_string（繼承自 Point）
cp = ColoredPoint.from_string("5,6")
# 注意！因為 cls 會自動帶入 ColoredPoint，所以 cls(5,6) 實際上是 ColoredPoint(5,6)
print(cp)            # ColoredPoint(5, 6, color='black')
print(type(cp))      # <class '__main__.ColoredPoint'>，不是 Point！
# 如果 from_string 裡面寫的是 Point(x, y) 而不是 cls(x, y)，
# 那麼 cp 就會是 Point 而不是 ColoredPoint，且 color 屬性也不會被建立

# ── CPE 應用：UVA 11005 進位制物件 ──────────────────────
# 題目的輸入是一串成本值，可以用 classmethod 從字串建立

class CostTable:
    """儲存 36 個字元（0-9, A-Z）各自的印刷成本"""

    # 類別常數：36 個字元的字串，下標對應進位制中的位數值
    CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, costs):
        """
        建構子：接受成本列表
        costs：長度 36 的整數列表，每個元素對應一個字元的成本
        """
        self.costs = costs   # list，長度 36

    def cost_of(self, digit_index):
        """取得指定位數索引的字元成本"""
        return self.costs[digit_index]  # 直接從列表中取出

    def total_cost(self, n, base):
        """
        計算數字 n 在 base 進位下的總印刷成本
        n：要計算的數字
        base：進位制（2～36）
        """
        if n == 0:              # 如果 n 是 0
            return self.costs[0]  # 直接回傳字元 '0' 的成本
        total = 0               # 初始化總成本為 0
        while n > 0:            # 當 n 還大於 0 時持續迴圈
            total += self.costs[n % base]  # 取餘數得到最低位數，加上該字元的成本
            n //= base          # 整數除法去掉最低位，繼續處理下一位
        return total            # 回傳總成本

    @classmethod
    def uniform(cls, cost=1):
        """
        工廠方法：建立所有字元成本相同的表
        cost：每個字元的成本（預設為 1）
        方便測試時快速建立成本表
        """
        return cls([cost] * 36)   # 建立長度 36、全部都是 cost 的列表

    @classmethod
    def from_flat_string(cls, s):
        """
        工廠方法：從一行 36 個整數（空白分隔）建立成本表
        s：例如 "1 2 3 ... 36" 這樣的字串
        """
        values = list(map(int, s.split()))  # 以空白分割字串並轉成整數列表
        return cls(values)                  # 用此列表建立 CostTable 物件

print("\n=== CPE：進位制成本計算 ===")
table = CostTable.uniform(1)   # 建立每個字元成本都是 1 的成本表
n = 255                        # 測試數字 255
for base in range(2, 11):      # 計算 2 進位到 10 進位
    c = table.total_cost(n, base)  # 計算 n 在該進位下的總成本
    print(f"  255 在 {base:2d} 進位：位數 {c}")

# 記憶重點 ──────────────────────────────────────────────────
# @classmethod 的第一個參數是 cls（class 本身），不是 self（物件）
# cls(...)  等於  ClassName(...)，但繼承時會自動用子類
# 常用於：替代構造器、工廠方法、從不同格式解析資料
