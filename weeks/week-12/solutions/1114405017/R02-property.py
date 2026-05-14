# R02. 屬性封裝（8.6）
# @property / getter / setter / 唯讀屬性

# ── 基本 @property ────────────────────────────────────────
# 定義一個Circle類別，示範屬性封裝和驗證
class Circle:
    # 建構函式：初始化私有屬性_radius
    def __init__(self, radius):
        self._radius = radius   # _radius：慣例上表示「受保護」，不應直接存取

    # @property裝飾器：將方法轉換為屬性getter
    @property
    def radius(self):
        """取得圓的半徑"""
        return self._radius

    # @radius.setter：定義radius屬性的setter，允許設定值並進行驗證
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("半徑不能為負數")  # 拋出異常防止無效值
        self._radius = value

    # 唯讀屬性：只有getter，沒有setter
    @property
    def area(self):             # 計算圓面積
        import math
        return math.pi * self._radius ** 2

    # 另一個唯讀屬性：計算圓直徑
    @property
    def diameter(self):
        return self._radius * 2


# 建立Circle實例，初始半徑為5
c = Circle(5)
print(c.radius)     # 取得半徑：5
print(c.area)       # 計算面積：78.539...
print(c.diameter)   # 計算直徑：10

# 修改半徑，觀察面積自動更新
c.radius = 10       # 呼叫setter設定新半徑
print(c.area)       # 面積自動重新計算：314.159...

# 示範錯誤處理：嘗試設定負數半徑
try:
    c.radius = -1   # 這會觸發ValueError
except ValueError as e:
    print(e)        # 輸出錯誤訊息：半徑不能為負數

# 示範唯讀屬性不能被設定
try:
    c.area = 100    # 嘗試設定唯讀屬性
except AttributeError as e:
    print(e)        # 輸出錯誤訊息

# ── 用 property 做延遲計算 ────────────────────────────────
# property的另一個用途：將計算結果作為屬性，提供延遲計算的效果
class Rectangle:
    # 建構函式：初始化寬度和高度
    def __init__(self, width, height):
        self.width = width    # 寬度屬性
        self.height = height  # 高度屬性

    # 面積屬性：每次存取時重新計算
    @property
    def area(self):
        return self.width * self.height

    # 周長屬性：每次存取時重新計算
    @property
    def perimeter(self):
        return 2 * (self.width + self.height)


# 建立Rectangle實例
r = Rectangle(4, 6)
print(r.area)       # 計算面積：24
print(r.perimeter)  # 計算周長：20

# 修改寬度後，面積和周長會自動基於新值重新計算
r.width = 8         # 修改寬度為8
print(r.area)       # 面積自動更新：48
