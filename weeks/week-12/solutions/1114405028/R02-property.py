# R02-property.py
# 完整繁體中文註釋版：示範 @property、getter、setter 與唯讀屬性

# 基本 @property 範例
class Circle:
    def __init__(self, radius):
        self._radius = radius   # 以 _ 開頭表示內部屬性，不要直接存取

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("半徑不能為負數")
        self._radius = value

    @property
    def area(self):             # 唯讀屬性，沒有 setter
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
    print(e)

try:
    c.area = 100    # 唯讀屬性不能設定
except AttributeError as e:
    print(e)

# 用 property 做延遲計算
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
r.width = 8
print(r.area)       # 48
