# R03. @property：屬性的守門員
#
# `@property` 提供一個乾淨的屬性存取界面（像讀取屬性一樣），但實際上可以在
# 背後執行 getter / setter 邏輯（例如驗證、延遲計算、轉換等）。這讓使用者在介面
# 上不需改變（仍寫 a.x、a.x = v），而內部可以安全地加入檢查或計算。
#
# 學習重點：
#  - 使用 `@property` 將欄位封裝為受控存取（getter / setter）
#  - 無 setter 的 property 為唯讀屬性（computed property）
#  - 子類別可以覆寫父類的 property 或其 setter，以擴充或放寬檢查規則

# ── 沒有保護的屬性會怎樣？ ───────────────────────────────

class BadStudent:
    """一個沒有任何保護的學生類別，用來示範直接存取屬性的風險。"""

    def __init__(self, name, grade):
        self.name = name
        # 直接把 grade 當成公開屬性存放，外部可任意改寫
        self.grade = grade


s = BadStudent("王小明", 85)
# 直接設定為負值，程式不會阻止（不合理的狀態）
s.grade = -100
print(f"糟糕：{s.name} 的成績是 {s.grade}")  # -100

# ── @property：在存取屬性時加上檢查 ─────────────────────

class Student:
    """受保護的學生類別，示範如何用 property 在設定時加入驗證。

    實作細節：
      - 把實際儲存的屬性命名為 `_grade`（底線表示內部使用），
      - 對外提供 `grade` 屬性，讀取時回傳 `_grade`，設定時先做範圍檢查再寫入。
    """

    def __init__(self, name, grade):
        self.name = name
        # 指派到 property 的 setter（會觸發檢查）
        self.grade = grade

    @property
    def grade(self):
        """getter：讀取 `self.grade` 時會呼叫此方法，回傳內部儲存 `_grade`。"""
        return self._grade

    @grade.setter
    def grade(self, value):
        """setter：在設定 `self.grade = value` 時執行檢查，若不合法則丟出 ValueError。"""
        if not (0 <= value <= 100):
            raise ValueError(f"成績必須在 0～100，你給了 {value}")
        self._grade = value

print("\n=== @property 守門員 ===")
s = Student("李大華", 90)
print(s.grade)    # 90

s.grade = 75      # 合法，通過檢查
print(s.grade)    # 75

try:
    s.grade = -10  # 觸發 ValueError
except ValueError as e:
    print(f"錯誤：{e}")

# ── 唯讀屬性：計算出來的值不需要存 ──────────────────────

class Circle:
    """示範唯讀（computed）屬性：面積與直徑由 radius 計算而來。

    這類屬性不會有 setter，因此外部不能直接指派（會得到 AttributeError）。
    """

    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        """計算並回傳圓面積：π * r^2。這是唯讀屬性（沒有 setter）。"""
        import math
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        """直徑由 radius 計算而來，示範多個唯讀屬性間的相依關係。"""
        return self.radius * 2


print("\n=== 唯讀屬性（計算值）===")
c = Circle(5)
print(f"半徑 {c.radius}，直徑 {c.diameter:.1f}，面積 {c.area:.2f}")

c.radius = 10
print(f"半徑 {c.radius}，直徑 {c.diameter:.1f}，面積 {c.area:.2f}")

# 若嘗試直接設定 c.area，會得到 AttributeError，因為 area 沒有對應的 setter。
# try:
#     c.area = 100

# ── 子類覆寫 setter ───────────────────────────────────────
# 研究生有加分機制，成績可以超過 100

class GradStudent(Student):
    """研究生類別：示範子類如何覆寫父類的 property setter（放寬或改變驗證規則）。"""

    @Student.grade.setter
    def grade(self, value):
        # 研究生成績允許到 150（例如加分制度），其他行為保留父類的命名與內部儲存方式
        if not (0 <= value <= 150):
            raise ValueError(f"研究生成績必須在 0～150，你給了 {value}")
        self._grade = value

print("\n=== 子類覆寫 setter ===")
g = GradStudent("張教授", 120)
print(g.grade)   # 120（研究生可以超過 100）

# 記憶重點 ──────────────────────────────────────────────────
# @property           → getter，讀取時觸發
# @屬性名.setter      → setter，設定時觸發（可加驗證）
# 沒有 setter 的就是「唯讀屬性」
# 實際資料習慣存在 _屬性名（底線開頭）
