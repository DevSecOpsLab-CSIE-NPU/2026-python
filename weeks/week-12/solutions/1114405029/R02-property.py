# R02. 屬性封裝（8.6）
# @property / getter / setter / 唯讀屬性

# ── 基本 @property ────────────────────────────────────────

# Circle 類別
# 用來表示圓形
class Circle:

    # __init__()：
    # 建構子，建立物件時自動呼叫
    def __init__(self, radius):

        # self._radius：
        # 真正儲存半徑的實例變數

        # 前面的底線 _：
        # 是 Python 慣例

        # 表示：
        # 「內部使用」
        # 「受保護（protected）」
        # 不建議直接從外部修改

        # 並不是強制 private
        # 只是提醒開發者：
        # 應該透過 property 存取
        self._radius = radius   # _radius：慣例上表示「受保護」，不直接存取

    # @property：
    # 將方法變成「屬性」

    # 使用者可以：
    # c.radius

    # 而不用：
    # c.radius()

    # 這種寫法稱為 getter
    @property
    def radius(self):

        # 回傳目前半徑
        return self._radius

    # @radius.setter：
    # 設定 radius 屬性的 setter 方法

    # 當執行：
    # c.radius = 10

    # Python 會自動呼叫這個 setter
    @radius.setter
    def radius(self, value):

        # 檢查輸入是否合法

        # 如果半徑小於 0：
        # 主動拋出 ValueError
        if value < 0:
            raise ValueError("半徑不能為負數")

        # 通過檢查後才真正修改值
        self._radius = value

    # @property：
    # area 是一個唯讀屬性

    # 沒有 setter
    # 所以不能：
    # c.area = 100
    @property
    def area(self):             # 唯讀屬性（沒有 setter）

        # 匯入 math 模組
        # 使用 math.pi
        import math

        # 圓面積公式：
        # πr²
        return math.pi * self._radius ** 2

    # diameter：
    # 直徑屬性
    @property
    def diameter(self):

        # 直徑 = 半徑 × 2
        return self._radius * 2


# 建立 Circle 物件
# 半徑為 5
c = Circle(5)

# 存取 radius property
# 實際上會呼叫 getter
print(c.radius)     # 5

# 存取 area property
print(c.area)       # 78.539...

# 存取 diameter property
print(c.diameter)   # 10

# 修改 radius

# 這不是直接改變變數
# 而是呼叫 setter
c.radius = 10       # 呼叫 setter

# 半徑變成 10
# area 也會重新計算
print(c.area)       # 314.159...

# try-except：
# 用來捕捉例外（exception）

try:

    # radius.setter 內會檢查 value < 0
    # 因此這裡會拋出 ValueError
    c.radius = -1   # 觸發 ValueError

# 捕捉 ValueError
except ValueError as e:

    # 印出錯誤訊息
    print(e)        # 半徑不能為負數

try:

    # area 是唯讀 property
    # 沒有 setter

    # 因此不能指定新值
    c.area = 100    # 唯讀屬性不能設定

# Python 會拋出 AttributeError
except AttributeError as e:

    # 印出錯誤訊息
    print(e)

# ── 用 property 做延遲計算 ────────────────────────────────

# Rectangle 類別
# 用來表示矩形
class Rectangle:

    # 建構子
    def __init__(self, width, height):

        # 儲存寬度與高度
        self.width = width
        self.height = height

    # area property
    @property
    def area(self):

        # 面積公式：
        # 寬 × 高

        # 每次存取時才重新計算
        # 這種方式稱為：
        # 「延遲計算」
        return self.width * self.height

    # perimeter property
    @property
    def perimeter(self):

        # 周長公式：
        # 2 × (寬 + 高)
        return 2 * (self.width + self.height)


# 建立 Rectangle 物件
r = Rectangle(4, 6)

# area：
# 4 × 6 = 24
print(r.area)       # 24

# perimeter：
# 2 × (4 + 6) = 20
print(r.perimeter)  # 20

# 修改 width
r.width = 8         # 修改後 area 自動更新

# area 不需要手動更新
# 因為 property 每次都重新計算
# 8 × 6 = 48
print(r.area)       # 48