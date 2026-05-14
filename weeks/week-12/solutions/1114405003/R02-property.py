# R02. 屬性封裝（8.6）
# 主題：`@property` / `getter` / `setter` / 唯讀屬性的進階應用
# 註解語言：繁體中文（臺灣 zh-TW），並展示如何搭配多個實例變數

# ── 基本 @property ────────────────────────────────────────
# @property 裝飾器讓你可以像存取屬性一樣呼叫方法，
# 實現「受保護屬性」的模式：
# - 使用 `_name` 慣例表示「受保護」的內部變數
# - 透過 @property 提供「讀取」介面
# - 透過 @name.setter 提供「設定」介面，可加入驗證邏輯

class Circle:
    # `__init__` 初始化圓形的各項屬性
    def __init__(self, radius, label="", color="blue"):
        # `_radius` 慣例上表示「受保護」，不直接在外部修改
        self._radius = radius
        # 新增實例變數：標籤與顏色
        self._label = label
        self._color = color

    # ── radius 屬性：具有驗證的 getter 與 setter ──
    @property
    def radius(self):
        """回傳圓的半徑"""
        return self._radius

    @radius.setter
    def radius(self, value):
        """設定圓的半徑，並檢查是否為正數"""
        if value < 0:
            raise ValueError("半徑不能為負數")
        self._radius = value

    # ── label 屬性：簡單的 getter 與 setter ──
    @property
    def label(self):
        """回傳圓的標籤"""
        return self._label

    @label.setter
    def label(self, value):
        """設定圓的標籤"""
        self._label = value

    # ── color 屬性：簡單的 getter 與 setter ──
    @property
    def color(self):
        """回傳圓的顏色"""
        return self._color

    @color.setter
    def color(self, value):
        """設定圓的顏色"""
        self._color = value

    # ── area 屬性：唯讀（沒有 setter） ──
    @property
    def area(self):
        """計算圓的面積（唯讀屬性）"""
        import math
        return math.pi * self._radius ** 2

    # ── diameter 屬性：唯讀（沒有 setter） ──
    @property
    def diameter(self):
        """計算圓的直徑（唯讀屬性）"""
        return self._radius * 2

    def __str__(self):
        """提供人性化的字串表示"""
        return f"[{self._label}] 圓形（半徑 {self._radius}，顏色 {self._color}）"


# 使用 Circle 類別
c = Circle(5, label="C1", color="red")
print("圓形 1:", c)
print(f"半徑: {c.radius}")     # 5
print(f"面積: {c.area:.2f}")       # 78.539...
print(f"直徑: {c.diameter}")   # 10

# 透過 setter 修改屬性
c.radius = 10       # 呼叫 setter
c.color = "green"   # 修改顏色
c.label = "C1-updated"
print("\n修改後的圓形:", c)
print(f"面積: {c.area:.2f}")       # 314.159...

# 驗證機制：負數會被拒絕
try:
    c.radius = -1   # 觸發 ValueError
except ValueError as e:
    print(f"\n錯誤: {e}")        # 半徑不能為負數

# 唯讀屬性不能設定
try:
    c.area = 100    # 唯讀屬性不能設定
except AttributeError as e:
    print(f"錯誤: {e}")

# ── 用 property 做延遲計算 ────────────────────────────────
# @property 的另一個常見用途是「延遲計算」：
# 當需要某個計算結果時，才即時算出，而不是在 __init__ 時預先計算。

class Rectangle:
    # 初始化矩形的各項屬性
    def __init__(self, width, height, name="", color="white"):
        # 寬度與高度
        self.width = width
        self.height = height
        # 新增實例變數：名稱與顏色
        self._name = name
        self._color = color

    # ── name 屬性 ──
    @property
    def name(self):
        """回傳矩形的名稱"""
        return self._name

    @name.setter
    def name(self, value):
        """設定矩形的名稱"""
        self._name = value

    # ── color 屬性 ──
    @property
    def color(self):
        """回傳矩形的顏色"""
        return self._color

    @color.setter
    def color(self, value):
        """設定矩形的顏色"""
        self._color = value

    # ── area 屬性：延遲計算（每次存取時重新計算） ──
    @property
    def area(self):
        """計算矩形面積（寬 × 高）"""
        return self.width * self.height

    # ── perimeter 屬性：延遲計算 ──
    @property
    def perimeter(self):
        """計算矩形周長（2 × (寬 + 高)）"""
        return 2 * (self.width + self.height)

    # ── diagonal 屬性：延遲計算 ──
    @property
    def diagonal(self):
        """計算矩形對角線長度"""
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def __str__(self):
        """提供人性化的字串表示"""
        return f"[{self._name}] 矩形（寬 {self.width}，高 {self.height}，顏色 {self._color}）"


# 使用 Rectangle 類別
r = Rectangle(4, 6, name="R1", color="yellow")
print(f"\n矩形 1: {r}")
print(f"面積: {r.area}")       # 24
print(f"周長: {r.perimeter}")  # 20
print(f"對角線: {r.diagonal:.2f}")

# 修改寬度後，面積與周長會自動重新計算
r.width = 8         # 修改寬度
r.color = "cyan"    # 修改顏色
print(f"\n修改後的矩形: {r}")
print(f"新面積: {r.area}")       # 48
print(f"新周長: {r.perimeter}")  # 28

# ── 常見提醒 ─────────────────────────────────────────────
# - `@property` 裝飾器讓方法看起來像屬性（不加括號）。
# - `@name.setter` 可以在設定值時加入驗證邏輯，保護物件狀態。
# - 唯讀屬性只需要定義 `@property`，不定義 `@name.setter`。
# - 使用 `_name` 慣例表示內部屬性，讓使用者知道這些不該直接存取。
# - 透過 `@property` 可以實現「延遲計算」：只在需要時才算，更有效率。
# - 若定義了 setter，修改屬性值時，該 setter 會自動被呼叫。
