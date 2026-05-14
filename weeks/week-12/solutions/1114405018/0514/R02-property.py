"""R02. 屬性封裝（8.6）

說明（繁體中文詳細註解）：
- 使用 `@property` 可以把方法包裝成屬性（attribute-like），讓呼叫端以 `obj.attr` 的形式存取，
  但在內部可以做驗證或延遲計算。
- 同時可以搭配 `@<prop>.setter` 與 `@<prop>.deleter` 定義 setter 與 deleter，達到封裝與資料驗證的效果。
"""


# 基本 @property 範例：定義 radius 屬性並加入驗證
class Circle:
    def __init__(self, radius):
        # 使用慣例 _radius 表示內部欄位，不要直接從外部改動
        self._radius = radius

    @property
    def radius(self):
        # getter：直接回傳內部欄位
        return self._radius

    @radius.setter
    def radius(self, value):
        # setter：做輸入驗證，避免不合法值
        if value < 0:
            raise ValueError("半徑不能為負數")
        self._radius = value

    @property
    def area(self):             # 唯讀屬性（沒有 setter）
        import math
        return math.pi * self._radius ** 2

    @property
    def diameter(self):
        return self._radius * 2


c = Circle(5)
print(c.radius)     # 5
print(c.area)       # 78.539...
print(c.diameter)   # 10

c.radius = 10       # 呼叫 setter
print(c.area)       # 314.159...

try:
    c.radius = -1   # 觸發 ValueError
except ValueError as e:
    print(e)        # 半徑不能為負數

try:
    c.area = 100    # 唯讀屬性不能設定，會產生 AttributeError
except AttributeError as e:
    print(e)


# 用 property 做延遲計算：只有在存取時才會計算，避免不必要的更新
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    @property
    def perimeter(self):
        return 2 * (self.width + self.height)


r = Rectangle(4, 6)
print(r.area)       # 24
print(r.perimeter)  # 20
r.width = 8         # 修改後 area 自動更新
print(r.area)       # 48
