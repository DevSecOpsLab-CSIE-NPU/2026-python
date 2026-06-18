# R02. 屬性封裝示範
# 這個範例說明 @property 的用法：getter、setter、唯讀屬性，以及動態計算屬性。

class Circle:
    def __init__(self, radius):
        self._radius = radius  # 底線開頭代表內部私有屬性，不應直接對外存取

    @property
    def radius(self):
        # 讀取 radius 時會呼叫這個方法
        return self._radius

    @radius.setter
    def radius(self, value):
        # 設定 radius 時會先驗證數值，再更新內部屬性
        if value < 0:
            raise ValueError("半徑不能為負數")
        self._radius = value

    @property
    def area(self):
        # 沒有 setter，因此 area 是唯讀屬性
        import math
        return math.pi * self._radius ** 2

    @property
    def diameter(self):
        # 直徑可以根據半徑動態計算
        return self._radius * 2


c = Circle(5)
print(c.radius)     # 5
print(c.area)       # 78.539...
print(c.diameter)   # 10

c.radius = 10       # 透過 setter 修改 radius
print(c.area)       # 314.159...

try:
    c.radius = -1   # 觸發驗證錯誤
except ValueError as e:
    print(e)

try:
    c.area = 100    # 嘗試設定唯讀屬性會失敗
except AttributeError as e:
    print(e)


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        # 寬高變動時，area 自動重新計算
        return self.width * self.height

    @property
    def perimeter(self):
        return 2 * (self.width + self.height)


r = Rectangle(4, 6)
print(r.area)       # 24
print(r.perimeter)  # 20
r.width = 8         # 變更屬性後，area 與 perimeter 自動反映新值
print(r.area)       # 48
