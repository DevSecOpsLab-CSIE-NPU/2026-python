# R02. 屬性封裝（8.6）
# @property / getter / setter / 唯讀屬性

from __future__ import annotations

# ------------------------------------------------------------
# 基本 @property 範例：Circle
# ------------------------------------------------------------
class Circle:
    def __init__(self, radius: float) -> None:
        # 慣例上使用 _radius 表示私有/受保護欄位，不要直接從外部存取
        self._radius = radius

    @property
    def radius(self) -> float:
        # getter：將受保護欄位包裝成公開屬性
        return self._radius

    @radius.setter
    def radius(self, value: float) -> None:
        # setter：設定前可以加上驗證邏輯，確保資料有效性
        if value < 0:
            raise ValueError("半徑不能為負數")
        self._radius = value

    @property
    def area(self) -> float:
        # 唯讀屬性：沒有對應 setter，外部無法直接指定
        import math
        return math.pi * self._radius ** 2

    @property
    def diameter(self) -> float:
        # 由 radius 計算而來，設定 radius 會自動影響 diameter
        return self._radius * 2


# Circle 使用示範
c = Circle(5)
print(c.radius)     # 5
print(c.area)       # 78.539...，使用 property 讀取時像欄位一樣
print(c.diameter)   # 10

c.radius = 10       # 呼叫 setter，會觸發驗證邏輯
print(c.area)       # 314.159...

try:
    c.radius = -1   # 觸發 ValueError
except ValueError as e:
    print(e)        # 半徑不能為負數

try:
    c.area = 100    # 嘗試設定唯讀屬性
except AttributeError as e:
    print(e)        # 不能設定 attribute


# ------------------------------------------------------------
# 用 property 做延遲計算：Rectangle
# ------------------------------------------------------------
class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    @property
    def area(self) -> float:
        # 每次存取皆重新計算，保持資料一致
        return self.width * self.height

    @property
    def perimeter(self) -> float:
        # 另一個延遲計算的屬性
        return 2 * (self.width + self.height)


# Rectangle 使用示範
r = Rectangle(4, 6)
print(r.area)       # 24
print(r.perimeter)  # 20
r.width = 8         # 修改後，area 會自動更新為最新值
print(r.area)       # 48
