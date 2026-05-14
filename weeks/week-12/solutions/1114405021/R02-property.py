# R02. 屬性封裝（8.6）
# 本範例示範 Python 的 property 機制：
# 1. @property：把方法包裝成像屬性一樣使用
# 2. @xxx.setter：為屬性加上設定邏輯
# 3. 唯讀屬性：只允許讀取，不允許指定
# 4. 用 property 做延遲計算，讓屬性值能隨物件狀態自動更新

# -----------------------------------------------------------------------------
# 一、基本 @property：Circle
# -----------------------------------------------------------------------------
# 在 Python 中，如果你想控制屬性被存取的方式，可以使用 property。
# 這樣做的好處是：
# - 外部看起來像在讀寫一般屬性
# - 內部其實可以加入檢查、轉換或自動計算
# - 未來如果實作改變，外部呼叫方式也不用跟著改
class Circle:
    def __init__(self, radius):
        # _radius 前面加底線，是一種慣例，表示這個屬性不建議直接從外部操作。
        # 真正對外公開的介面會透過 radius property 來控制。
        self._radius = radius   # _radius：慣例上表示「受保護」，不直接存取

    # @property 會把 radius 方法變成「可讀屬性」
    # 外部可以直接用 c.radius 讀取，而不是 c.radius()
    @property
    def radius(self):
        return self._radius

    # @radius.setter 代表當外部執行 c.radius = value 時，會進到這個方法。
    # 這裡可以先檢查資料是否合法，再決定要不要真的寫入。
    @radius.setter
    def radius(self, value):
        # 半徑不應該是負數，所以先做驗證。
        if value < 0:
            raise ValueError("半徑不能為負數")
        self._radius = value

    # area 也是 property，但只有 getter，沒有 setter。
    # 這表示它是唯讀屬性，外部只能讀，不能直接指定。
    # area 不是存下來的資料，而是根據 _radius 即時計算出來。
    @property
    def area(self):             # 唯讀屬性（沒有 setter）
        import math
        return math.pi * self._radius ** 2

    # diameter 也是由 _radius 即時計算出來的屬性。
    # 用 property 表達這類「看起來像資料、實際上是計算結果」的值，最自然。
    @property
    def diameter(self):
        return self._radius * 2


# 建立一個半徑為 5 的圓。
# 這時候 __init__ 直接把值存進 _radius。
c = Circle(5)

# 讀取 radius：實際上會呼叫 @property 的 getter。
print(c.radius)     # 5

# 讀取 area：會根據目前半徑即時計算面積。
print(c.area)       # 78.539...

# 讀取 diameter：會根據目前半徑即時計算直徑。
print(c.diameter)   # 10

# 指定 c.radius = 10 時，會進入 setter，先檢查再更新資料。
c.radius = 10       # 呼叫 setter
print(c.area)       # 314.159...

# -----------------------------------------------------------------------------
# 二、setter 驗證：避免不合法的資料
# -----------------------------------------------------------------------------
# 如果有人嘗試設定負半徑，setter 會主動丟出 ValueError。
# 這比事後才發現資料錯誤更安全，也能把規則集中在類別內管理。
try:
    c.radius = -1   # 觸發 ValueError
except ValueError as e:
    print(e)        # 半徑不能為負數

# area 沒有 setter，所以它是唯讀屬性。
# 如果嘗試直接指定，Python 會丟出 AttributeError。
try:
    c.area = 100    # 唯讀屬性不能設定
except AttributeError as e:
    print(e)

# -----------------------------------------------------------------------------
# 三、用 property 做延遲計算：Rectangle
# -----------------------------------------------------------------------------
# 有些屬性不需要另外存起來，只要在被讀取時即時計算即可。
# 這種做法稱為「延遲計算」或「計算型屬性」。
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # area 不是固定值，而是根據 width 與 height 計算出來。
    # 每次讀取 r.area 都會重新算，所以當 width 或 height 改變時，
    # area 也會跟著改變，完全不需要手動同步。
    @property
    def area(self):
        return self.width * self.height

    # perimeter（周長）也是即時計算，不需要另外保存。
    @property
    def perimeter(self):
        return 2 * (self.width + self.height)


# 建立一個寬 4、高 6 的矩形。
r = Rectangle(4, 6)
print(r.area)       # 24
print(r.perimeter)  # 20

# 修改 width 後，再次讀取 area，結果會自動更新。
# 這就是 property 的優點：讓「看起來像屬性」的值保持即時正確。
r.width = 8         # 修改後 area 自動更新
print(r.area)       # 48

# -----------------------------------------------------------------------------
# 補充說明
# -----------------------------------------------------------------------------
# property 常用於：
# - 封裝內部資料
# - 驗證輸入值
# - 把計算結果表現成屬性
# - 保留對外 API 的穩定性
#
# 實務上常見模式是：先用一般屬性儲存資料，再用 property 控制讀寫方式，
# 讓物件更安全、也更容易維護。
