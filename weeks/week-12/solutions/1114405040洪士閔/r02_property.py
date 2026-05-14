"""R02. 屬性封裝。

這份版本示範 @property、getter、setter，以及唯讀屬性的基本概念，
並補上較完整的繁體中文註解，方便記憶和複習。
"""


# 基本 @property：用 getter / setter 包住內部資料，避免外部直接亂改。
class Circle:
    def __init__(self, radius):
        # 慣例上用底線開頭表示「內部使用」的屬性。
        self._radius = radius

    @property
    def radius(self):
        # 透過 property 對外提供讀取方式。
        return self._radius

    @radius.setter
    def radius(self, value):
        # setter 可以在賦值時先做檢查。
        if value < 0:
            raise ValueError("半徑不能為負數")
        self._radius = value

    @property
    def area(self):
        # 唯讀屬性：只提供讀取，不提供 setter。
        import math
        return math.pi * self._radius ** 2

    @property
    def diameter(self):
        # 直徑是半徑的兩倍，適合用 property 即時計算。
        return self._radius * 2


c = Circle(5)
print(c.radius)     # 5
print(c.area)       # 78.539...
print(c.diameter)   # 10

c.radius = 10       # 觸發 setter，值會重新被檢查
print(c.area)       # 314.159...

try:
    c.radius = -1   # 這裡會因為半徑不能是負數而丟出例外
except ValueError as e:
    print(e)

try:
    c.area = 100    # area 沒有 setter，所以不能被賦值
except AttributeError as e:
    print(e)


# 第二個範例：把計算屬性寫成 property，資料改了就自動反映。
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
r.width = 8         # 修改後，area 會跟著更新
print(r.area)       # 48
