# R02. 屬性封裝（8.6）
# @property / getter / setter / 唯讀屬性
#
# 封裝（Encapsulation）是物件導向的核心概念之一：
# 把「資料」與「驗證邏輯」包在一起，避免外部直接存取原始變數。
# Python 用 @property 裝飾器，讓方法可以像屬性一樣存取，
# 不必改外部的呼叫語法就能在存取時加入驗證或計算。

# ── 基本 @property ────────────────────────────────────────
class Circle:
    def __init__(self, radius):
        # 前置底線 _radius 是 Python 慣例，代表「受保護」屬性，
        # 表示外部程式碼不應直接存取；應透過 property 存取。
        self._radius = radius

    @property
    def radius(self):
        # getter：外部讀取 c.radius 時觸發此方法
        return self._radius

    @radius.setter
    def radius(self, value):
        # setter：外部寫入 c.radius = xxx 時觸發此方法
        # 在這裡加入驗證邏輯，防止非法值進入物件
        if value < 0:
            raise ValueError("半徑不能為負數")
        self._radius = value

    @property
    def area(self):             # 唯讀屬性：只有 getter，沒有 setter
        # 面積是由半徑「推導」而來，外部不應直接設定，
        # 因此不定義 setter，讓 Python 把賦值視為錯誤。
        import math
        return math.pi * self._radius ** 2

    @property
    def diameter(self):
        # 直徑同樣是推導值，隨半徑自動更新
        return self._radius * 2


c = Circle(5)
print(c.radius)     # 5  — 呼叫 getter
print(c.area)       # 78.539...
print(c.diameter)   # 10

c.radius = 10       # 呼叫 setter，內部驗證通過後才存入
print(c.area)       # 314.159...  — 面積隨半徑自動更新

try:
    c.radius = -1   # setter 驗證失敗，丟出 ValueError
except ValueError as e:
    print(e)        # 半徑不能為負數

try:
    c.area = 100    # 沒有定義 setter，丟出 AttributeError
except AttributeError as e:
    print(e)        # can't set attribute

# ── 用 property 做延遲計算 ────────────────────────────────
# 「延遲計算」：不在 __init__ 裡預先算好，
# 而是在每次存取時才根據當前的 width/height 重新計算。
# 好處是修改 width 或 height 後，area 和 perimeter 自動反映最新值。
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        # 每次存取時即時計算，不快取
        return self.width * self.height

    @property
    def perimeter(self):
        return 2 * (self.width + self.height)


r = Rectangle(4, 6)
print(r.area)       # 24
print(r.perimeter)  # 20
r.width = 8         # 直接修改 width，area 下次讀取時會自動更新
print(r.area)       # 48
