# R02. 屬性封裝（8.6）
# @property / getter / setter / 唯讀屬性

# ── 基本 @property ────────────────────────────────────────
class Circle:
    def __init__(self, radius):
        # 內部通常用底線屬性保存真實資料，外部再透過 property 存取。
        self._radius = radius   # _radius：慣例上表示「受保護」，不直接存取

    @property
    def radius(self):
        # 讀取時看起來像屬性，實際上會進入這個方法。
        return self._radius

    @radius.setter
    def radius(self, value):
        # setter 可以在寫入前先檢查資料是否合法。
        if value < 0:
            raise ValueError("半徑不能為負數")
        self._radius = value

    @property
    def area(self):             # 唯讀屬性（沒有 setter）
        # 面積是根據半徑即時計算，所以不需要另外儲存。
        import math
        return math.pi * self._radius ** 2

    @property
    def diameter(self):
        # 直徑也是由半徑推算出的延伸屬性。
        return self._radius * 2


c = Circle(5)
# 存取 property 時，語法像一般屬性，但背後會執行方法。
print(c.radius)     # 5
print(c.area)       # 78.539...
print(c.diameter)   # 10

c.radius = 10       # 呼叫 setter
print(c.area)       # 314.159...

try:
    # setter 內部的檢查會攔下不合法值。
    c.radius = -1   # 觸發 ValueError
except ValueError as e:
    print(e)        # 半徑不能為負數

try:
    # 沒有 setter 的 property 預設就是唯讀。
    c.area = 100    # 唯讀屬性不能設定
except AttributeError as e:
    print(e)

# ── 用 property 做延遲計算 ────────────────────────────────
class Rectangle:
    def __init__(self, width, height):
        # 先保存寬與高，面積與周長在需要時才計算。
        self.width = width
        self.height = height

    @property
    def area(self):
        # 由目前的 width 與 height 即時計算。
        return self.width * self.height

    @property
    def perimeter(self):
        # 延遲計算的好處是資料更新後結果會自動反映。
        return 2 * (self.width + self.height)


r = Rectangle(4, 6)
# 修改寬或高後，再次讀取 property 就會得到最新結果。
print(r.area)       # 24
print(r.perimeter)  # 20
r.width = 8         # 修改後 area 自動更新
print(r.area)       # 48
