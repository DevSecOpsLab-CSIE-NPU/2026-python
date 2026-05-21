# R03. @property：屬性的守門員
# 讓類別 (class) 的屬性在「讀取」或「設定」時可以加入驗證或自訂邏輯。
# 對應 Bloom's Taxonomy：記憶 (Remember) — 能背得出語法並理解其適用的使用時機。

# ── 沒有保護的屬性會怎樣？ ───────────────────────────────

class BadStudent:
    """不好的範例：屬性完全暴露，容易被填入錯誤數據"""
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade   # 任何值都能塞進來，沒有檢查

s = BadStudent("王小明", 85)
s.grade = -100   # ❌ 邏輯錯誤：成績不能是負數，但程式卻允許了
print(f"糟糕：{s.name} 的成績被設成了 {s.grade}")

# ── @property：在存取屬性時加上檢查 ─────────────────────

class Student:
    def __init__(self, name, grade):
        self.name = name
        # 注意：這裡賦值也會自動觸發下方的 setter 進行檢查
        self.grade = grade

    @property
    def grade(self):
        """getter：當執行 print(s.grade) 時會呼叫此方法"""
        # 實際資料通常儲存在底線開頭的變數中（慣例上代表內部使用）
        return self._grade

    @grade.setter
    def grade(self, value):
        """setter：當執行 s.grade = xxx 時會呼叫此方法"""
        # 加入驗證邏輯：成績必須在合理範圍內
        if not (0 <= value <= 100):
            raise ValueError(f"成績必須在 0～100 之間，但你給了 {value}")
        self._grade = value

print("\n=== @property 守門員運作中 ===")
s = Student("李大華", 90)
print(f"初始成績：{s.grade}")

s.grade = 75      # ✅ 合法設定
print(f"修改後成績：{s.grade}")

try:
    s.grade = -10  # ❌ 觸發錯誤檢查
except ValueError as e:
    print(f"攔截到錯誤：{e}")

# ── 唯讀屬性：由其他資料計算出來的結果 ──────────────────

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        """面積是根據半徑算出來的，不應該讓使用者手動設定"""
        import math
        return math.pi * (self.radius ** 2)

    @property
    def diameter(self):
        """直徑也是連動的"""
        return self.radius * 2

print("\n=== 唯讀屬性（計算值）示範 ===")
c = Circle(5)
print(f"半徑 {c.radius} -> 直徑 {c.diameter:.1f}, 面積 {c.area:.2f}")

# 修改半徑，相關屬性會自動隨之改變
c.radius = 10
print(f"修改半徑為 {c.radius} -> 直徑 {c.diameter:.1f}, 面積 {c.area:.2f}")

# 若嘗試執行 c.area = 100 會噴出 AttributeError，因為我們沒有定義 setter

# ── 子類覆寫 setter ───────────────────────────────────────
# 情境：研究生有特殊加分機制，成績上限較高

class GradStudent(Student):

    # 繼承父類的屬性，但自訂設定邏輯
    @Student.grade.setter
    def grade(self, value):
        if not (0 <= value <= 150):
            raise ValueError(f"研究生成績必須在 0～150 之間，但你給了 {value}")
        self._grade = value

print("\n=== 子類覆寫屬性邏輯 ===")
g = GradStudent("張研究生", 120)
print(f"{g.name} 的成績：{g.grade} (超過了大學部的 100 分限制)")

# 記憶重點 ──────────────────────────────────────────────────
# 1. @property           → 讀取器 (getter)，像存取屬性一樣呼叫方法。
# 2. @屬性名.setter      → 設定器 (setter)，負責賦值時的檢查與處理。
# 3. 封裝 (Encapsulation) → 將實體資料 (_name) 與存取介面 (name) 分離。
# 4. 唯讀 (Read-only)    → 只定義 @property 而不定義 .setter 即可達成。
