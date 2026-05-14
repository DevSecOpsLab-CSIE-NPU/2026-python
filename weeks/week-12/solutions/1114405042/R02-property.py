"""
R02. 屬性封裝（8.6）

本範例示範 Python 的 @property 機制，重點包括：
    1. 透過 getter / setter 將屬性封裝起來
    2. 在 setter 中加入驗證邏輯，避免物件進入不合法狀態
    3. 使用唯讀屬性保護不應直接修改的資料
    4. 以 property 實作延遲計算，讓屬性看起來像資料，實際上是即時計算

這種寫法可以讓外部使用者用「屬性」的方式存取資料，但內部仍保有控制與驗證能力。
"""

# ── 基本 @property ────────────────────────────────────────
class Circle:
    def __init__(self, radius):
        # _radius 以前導底線開頭，表示這是內部使用的屬性。
        # 這是一種 Python 慣例，不是強制限制，但提醒其他程式碼不要直接碰它。
        self._radius = radius   # _radius：慣例上表示「受保護」，不直接存取

    @property
    def radius(self):
        # getter：當你讀取 c.radius 時，實際上會進到這個方法。
        # 對外看起來像在讀取屬性，對內則可以保留控制權。
        return self._radius

    @radius.setter
    def radius(self, value):
        # setter：當你寫入 c.radius = value 時，會進到這個方法。
        # 這裡加入驗證規則，確保半徑不會被設定成負數。
        if value < 0:
            raise ValueError("半徑不能為負數")
        self._radius = value

    @property
    def area(self):             # 唯讀屬性（沒有 setter）
        # area 不是儲存好的欄位，而是根據半徑即時計算出來的結果。
        # 因為沒有 setter，所以外部只能讀取，不能直接指定 c.area = ...
        import math
        return math.pi * self._radius ** 2

    @property
    def diameter(self):
        # 直徑也是根據半徑即時計算的衍生屬性。
        # 這樣可以避免重複儲存資料，且 radius 一改，diameter 也會自動反映新值。
        return self._radius * 2


# 建立一個半徑為 5 的圓物件。
# 外部使用者不需要知道內部是用 _radius 儲存，只要透過 radius 讀寫即可。
c = Circle(5)
print(c.radius)     # 5
# area 會即時計算，不是存在物件裡的固定值。
print(c.area)       # 78.539...
# diameter 也是從 _radius 推導出來的屬性。
print(c.diameter)   # 10

# 設定 c.radius 時，實際上會呼叫 radius.setter。
# 這使得我們可以在設定時做檢查與轉換，而不是直接改內部資料。
c.radius = 10       # 呼叫 setter
# 因為半徑已經更新，所以 area 也會隨之改變。
print(c.area)       # 314.159...

try:
    # 嘗試把半徑設成負數，setter 會主動拒絕並丟出 ValueError。
    c.radius = -1   # 觸發 ValueError
except ValueError as e:
    # 這裡會印出自訂的錯誤訊息，提醒使用者輸入不合法。
    print(e)        # 半徑不能為負數

try:
    # area 是唯讀屬性，因為沒有定義 @area.setter，所以不能直接指定。
    # 這樣可以避免外部把計算結果硬塞進去，破壞資料一致性。
    c.area = 100    # 唯讀屬性不能設定
except AttributeError as e:
    # Python 會因為找不到 setter 而拋出 AttributeError。
    print(e)

# ── 用 property 做延遲計算 ────────────────────────────────
class Rectangle:
    def __init__(self, width, height):
        # 這裡先直接儲存寬與高。
        # 之後的 area / perimeter 不另外儲存，而是在需要時才計算。
        self.width = width
        self.height = height

    @property
    def area(self):
        # 面積是延遲計算的屬性：每次讀取都根據目前 width 與 height 算一次。
        # 優點是不用額外維護 area 的同步更新問題。
        return self.width * self.height

    @property
    def perimeter(self):
        # 周長同樣是派生值，直接根據現有寬高計算即可。
        return 2 * (self.width + self.height)


# 建立一個寬 4、高 6 的矩形。
# area 與 perimeter 會根據目前的 width / height 即時計算。
r = Rectangle(4, 6)
print(r.area)       # 24
print(r.perimeter)  # 20
# 修改 width 後，不需要手動更新 area；下一次讀取時就會自動反映新值。
r.width = 8         # 修改後 area 自動更新
print(r.area)       # 48
