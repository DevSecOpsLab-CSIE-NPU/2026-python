# R02. 屬性封裝（8.6）
# @property / getter / setter / 唯讀屬性

# ── 基本 @property ───────────────────────────────────────
# 【詳解】
# @property 將方法包裝成「屬性」，讓你用 obj.attr 的語法呼叫方法。
# 好處：可在 setter 加入驗證，防止非法值；可實現唯讀屬性；可延遲計算。
# _radius：前置底線表示「受保護」，慣例上不直接存取。
class Circle:
    def __init__(self, radius):
        self._radius = radius # _radius：慣例上表示「受保護」，不直接存取

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("半徑不能為負數")
        self._radius = value

    @property
    def area(self): # 唯讀屬性（沒有 setter）
        import math
        return math.pi * self._radius ** 2

    @property
    def diameter(self):
        return self._radius * 2


c = Circle(5)
print(c.radius) # 5
print(c.area) # 78.539...
print(c.diameter) # 10

c.radius = 10 # 呼叫 setter
print(c.area) # 314.159...

try:
    c.radius = -1 # 觸發 ValueError
except ValueError as e:
    print(e) # 半徑不能為負數

try:
    c.area = 100 # 唯讀屬性不能設定
except AttributeError as e:
    print(e)

# ── 用 property 做延遲計算 ───────────────────────────────
# 【詳解】
# 「延遲計算」（lazy evaluation）：不預先儲存計算結果，
# 而是每次存取時才計算。若資料經常改動，這很有用。
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
print(r.area) # 24
print(r.perimeter) # 20

r.width = 8 # 修改後 area 自動更新
print(r.area) # 48
