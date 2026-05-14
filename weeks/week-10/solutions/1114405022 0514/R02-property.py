# R02. 屬性封裝（8.6）
# 本範例說明 `@property` 的核心用途：
# 1. 把「方法呼叫」包裝成「屬性存取」語法（`obj.x`）
# 2. 在設定屬性時加入驗證邏輯（setter）
# 3. 建立唯讀屬性（只提供 getter，不提供 setter）
# 4. 讓衍生值（例如面積）隨基礎資料改變而自動更新

# ── 基本 @property：Circle ─────────────────────────────────
class Circle:
    def __init__(self, radius):
        # 慣例：前導底線 `_radius` 表示內部屬性（不建議外部直接改）
        # 外部應透過 `radius` property 存取，以保留驗證機制
        self._radius = radius

    @property
    def radius(self):
        # getter：當你寫 `c.radius` 時會呼叫這裡
        return self._radius

    @radius.setter
    def radius(self, value):
        # setter：當你寫 `c.radius = value` 時會呼叫這裡
        # 在 setter 中做資料驗證，可避免物件進入非法狀態
        if value < 0:
            raise ValueError("半徑不能為負數")
        self._radius = value

    @property
    def area(self):
        # 唯讀屬性：只有 getter 沒有 setter，因此無法直接指定 `c.area = ...`
        # 每次存取都即時計算，確保結果永遠和當前半徑一致
        import math
        return math.pi * self._radius ** 2

    @property
    def diameter(self):
        # 另一個唯讀衍生屬性：直徑 = 半徑 * 2
        return self._radius * 2


# 使用示範：property 存取看起來像欄位，其實底層是方法
c = Circle(5)
print(c.radius)     # 5
print(c.area)       # 78.539...
print(c.diameter)   # 10

c.radius = 10       # 呼叫 setter，更新半徑
print(c.area)       # 314.159...（面積自動反映新半徑）

try:
    c.radius = -1   # 觸發 setter 驗證失敗
except ValueError as e:
    print(e)        # 半徑不能為負數

try:
    c.area = 100    # 唯讀屬性沒有 setter，會丟 AttributeError
except AttributeError as e:
    print(e)


# ── 用 property 做動態計算：Rectangle ───────────────────────
class Rectangle:
    def __init__(self, width, height):
        # 這裡先用最簡單寫法，不加驗證（教學重點放在 property）
        self.width = width
        self.height = height

    @property
    def area(self):
        # 面積是衍生值：長 * 寬
        # 每次讀取都根據最新 width/height 計算
        return self.width * self.height

    @property
    def perimeter(self):
        # 周長是衍生值：2 * (長 + 寬)
        return 2 * (self.width + self.height)


r = Rectangle(4, 6)
print(r.area)       # 24
print(r.perimeter)  # 20
r.width = 8         # 修改基礎欄位後
print(r.area)       # 48（property 會回傳新結果）
