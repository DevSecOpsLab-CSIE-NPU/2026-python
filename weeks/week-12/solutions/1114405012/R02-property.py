# R02. 屬性封裝（8.6）
# @property / getter / setter / 唯讀屬性

# 這份示範重點：
# 1) @property 如何實現屬性的 getter 與驗證
# 2) @屬性名.setter 如何實現 setter，以及驗證資料
# 3) 唯讀屬性（只有 getter，沒有 setter）
# 4) 延遲計算：屬性值根據其他欄位動態計算

# ── 基本 @property ────────────────────────────────────────
# @property 讓我們像存取屬性一樣呼叫方法，並可在中間加入驗證邏輯
class Circle:
    def __init__(self, radius):
        # _radius：慣例上下劃線表示「受保護」，表示不應直接存取
        # 而是透過 @property 方法來存取和驗證
        self._radius = radius   # _radius：慣例上表示「受保護」，不直接存取

    # @property：把方法變成屬性，讓外部可以像讀屬性一樣呼叫
    # 這就是 getter，當執行 c.radius 時會執行這個方法
    @property
    def radius(self):
        return self._radius

    # @radius.setter：定義 setter，當執行 c.radius = 10 時執行
    # 在這裡可以加入驗證邏輯，確保資料合法
    @radius.setter
    def radius(self, value):
        # 驗證：半徑不能為負數
        if value < 0:
            raise ValueError("半徑不能為負數")
        self._radius = value

    # 唯讀屬性：只有 @property getter，沒有 setter
    # 這代表外部可以讀但不能寫，嘗試設定會拋出 AttributeError
    @property
    def area(self):             # 唯讀屬性（沒有 setter）
        import math
        return math.pi * self._radius ** 2

    # 另一個唯讀屬性：計算直徑
    @property
    def diameter(self):
        return self._radius * 2


# 創建一個 Circle 物件，半徑為 5
c = Circle(5)
# 透過 @property getter 讀取（自動呼叫 radius() 方法）
print(c.radius)     # 5
# 透過 @property getter 讀取面積（自動計算）
print(c.area)       # 78.539...
# 透過 @property getter 讀取直徑（自動計算）
print(c.diameter)   # 10

# 透過 @property setter 設定新半徑（自動呼叫 radius(value) 方法）
c.radius = 10       # 呼叫 setter，會觸發驗證邏輯
print(c.area)       # 314.159...（面積自動更新）

# 嘗試設定無效的半徑，會觸發驗證拋出 ValueError
try:
    c.radius = -1   # 觸發 ValueError
except ValueError as e:
    print(e)        # 半徑不能為負數

# 嘗試設定唯讀屬性，會拋出 AttributeError
try:
    c.area = 100    # 唯讀屬性不能設定
except AttributeError as e:
    print(e)

# ── 用 @property 做延遲計算 ────────────────────────────────
# 延遲計算：屬性值根據其他欄位動態計算，而不是預先存儲
# 好處：節省記憶體、資料總是最新的
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # 面積是根據寬和高動態計算，不需要每次修改都更新
    @property
    def area(self):
        return self.width * self.height

    # 周長也是動態計算
    @property
    def perimeter(self):
        return 2 * (self.width + self.height)


# 創建一個 Rectangle 物件
r = Rectangle(4, 6)
# 透過 @property 讀取面積（自動計算）
print(r.area)       # 24
# 透過 @property 讀取周長（自動計算）
print(r.perimeter)  # 20
# 修改寬度
r.width = 8         # 修改後 area 自動更新
# 重新讀取面積，會根據新的 width 自動計算
print(r.area)       # 48（因為 area 是動態計算的）
