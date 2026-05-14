# R02. 屬性封裝（8.6）
# @property / getter / setter / 唯讀屬性

# ── 基本 @property ────────────────────────────────────────
class Circle:
    def __init__(self, radius):
        # 單底線開頭的屬性名稱（如 _radius）是 Python 的命名慣例，表示這是內部使用的「受保護」變數，不建議外部直接存取
        self._radius = radius

    # @property 裝飾器可以將一個方法偽裝成屬性（getter），外部透過 c.radius 即可取得值，不需加上括號 c.radius()
    @property
    def radius(self):
        return self._radius

    # 定義屬性的 setter，當外部執行 c.radius = value 時會自動呼叫此方法
    # 這種做法的好處是可以在設定變數值之前進行邏輯驗證或檢查
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("半徑不能為負數")
        self._radius = value

    # 只有 @property 而沒有設定對應的 setter，這個屬性就會變成「唯讀屬性」
    @property
    def area(self):
        import math
        return math.pi * self._radius ** 2

    @property
    def diameter(self):
        return self._radius * 2


c = Circle(5)
print(c.radius)     # 5          （會自動呼叫 def radius(self) 取得值）
print(c.area)       # 78.539...  （會自動呼叫 def area(self) 計算並回傳值）
print(c.diameter)   # 10         （會自動呼叫 def diameter(self) 計算並回傳值）

c.radius = 10       # 呼叫 setter（會自動呼叫 @radius.setter 定義的方法）
print(c.area)       # 314.159... （因為半徑改變了，重新讀取 area 時會用新的半徑計算）

try:
    c.radius = -1   # 觸發 setter 內的驗證邏輯，拋出 ValueError
except ValueError as e:
    print(e)        # 半徑不能為負數

try:
    c.area = 100    # 因為 area 沒有定義 setter，這裡會拋出 AttributeError
except AttributeError as e:
    print(e)

# ── 用 property 做延遲計算 ────────────────────────────────
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # 使用 @property 可以實作「依賴其他變數動態計算」的屬性
    # 這樣就不用在 __init__ 裡面先算好 area，避免 width/height 改變時 area 沒有跟著更新的 bug
    @property
    def area(self):
        return self.width * self.height

    @property
    def perimeter(self):
        return 2 * (self.width + self.height)


r = Rectangle(4, 6)
print(r.area)       # 24 （即時計算 4 * 6）
print(r.perimeter)  # 20 （即時計算 2 * (4 + 6)）
r.width = 8         # 修改實例變數 width，不需要手動去更新 area
print(r.area)       # 48 （再次存取時即時計算 8 * 6，確保資料一致性）
