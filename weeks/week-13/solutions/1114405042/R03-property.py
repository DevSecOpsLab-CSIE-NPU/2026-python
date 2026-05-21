"""
R03. @property：屬性的守門員（Property 範例）

說明：示範未保護屬性可能導致錯誤賦值，以及如何使用 `@property`
為屬性加入讀取與設定時的驗證邏輯。包含唯讀屬性與子類覆寫 setter 的範例。
"""

# ── 範例：沒有保護的屬性（壞範例）────────────────────────
class BadStudent:
    """示範：直接把屬性暴露給外部，任何值都能直接設定，可能造成不合法狀態。"""

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade   # 任何值都能塞進去（沒有驗證）

s = BadStudent("王小明", 85)
s.grade = -100   # 錯誤示範：竟然可以設定成負數
print(f"糟糕：{s.name} 的成績是 {s.grade}")  # -100（不合理）


# ── 正確做法：使用 @property 在存取時加上檢查（getter / setter）─────
class Student:
    """範例學生類別：使用 `@property` 封裝 grade，並在設定時檢查範圍。

    實作細節：實際儲存資料在 `_grade`（底線前綴表示內部欄位），
    透過 `grade` 屬性提供受控的存取介面。
    """

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade   # 會觸發下面定義的 setter，進行驗證

    @property
    def grade(self):
        """getter：當讀取 `instance.grade` 時會執行此方法。

        回傳實際儲存在 `_grade` 的值。
        """
        return self._grade

    @grade.setter
    def grade(self, value):
        """setter：當執行 `instance.grade = value` 時觸發，負責驗證與設定。

        若 value 不在 0..100 範圍內，會拋出 ValueError。
        """
        if not (0 <= value <= 100):
            raise ValueError(f"成績必須在 0～100，你給了 {value}")
        self._grade = value

print("\n=== @property 守門員 ===")
s = Student("李大華", 90)
print(s.grade)    # 90

s.grade = 75      # 合法，通過檢查
print(s.grade)    # 75

try:
    s.grade = -10  # 觸發 ValueError（輸入不合法）
except ValueError as e:
    print(f"錯誤：{e}")


# ── 唯讀屬性：計算而來，不應該被外部直接設定 ───────────────
class Circle:
    """圓形範例：示範 `@property` 作為唯讀屬性（如面積）。"""

    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        """面積為計算結果，不應直接設定，因此只提供 getter（唯讀）。"""
        import math
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        """直徑為半徑的兩倍，也以唯讀屬性方式提供。"""
        return self.radius * 2

print("\n=== 唯讀屬性（計算值）===")
c = Circle(5)
print(f"半徑 {c.radius}，直徑 {c.diameter:.1f}，面積 {c.area:.2f}")

c.radius = 10
print(f"半徑 {c.radius}，直徑 {c.diameter:.1f}，面積 {c.area:.2f}")

# 若嘗試設定唯讀屬性會得到 AttributeError：
# c.area = 100  # AttributeError：唯讀屬性不能設定


# ── 子類覆寫 setter：擴充或放寬限制（例如研究生可有較高上限）─────
class GradStudent(Student):

    @Student.grade.setter
    def grade(self, value):
        """子類覆寫 setter，放寬成績上限至 150（例如研究生加分機制）。"""
        if not (0 <= value <= 150):
            raise ValueError(f"研究生成績必須在 0～150，你給了 {value}")
        self._grade = value

print("\n=== 子類覆寫 setter ===")
g = GradStudent("張教授", 120)
print(g.grade)   # 120（研究生可以超過 100）


# 記憶重點 ──────────────────────────────────────────────────
# - `@property`           → 定義 getter，讀取屬性時觸發
# - `@屬性名.setter`      → 定義 setter，設定屬性時觸發，可加入驗證
# - 若沒有定義 setter，該屬性為唯讀
# - 實際儲存的欄位習慣使用 `_` 前綴（例如 `_grade`）表明為內部使用
