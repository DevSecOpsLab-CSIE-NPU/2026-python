# ===================================================================
# R03. @property：屬性的守門員
# 學生：賴俋勳 1114405041
# 日期：2026-05-21
# 主題：@property getter/setter — 在屬性存取時加入驗證或計算邏輯
# ===================================================================
# 【學習心得】
#   @property 讓 class 的屬性「看起來像直接存取」，但背後可以有邏輯。
#   呼叫端不需要改寫（不用改成 .get_grade()），直接用 obj.grade 即可。
#   這符合封裝原則：外部不知道內部實作，只知道怎麼用。
#
#   常見模式：
#   - 實際資料存在 _屬性名（底線開頭表示「內部用」）
#   - @property 提供 getter（讀取）
#   - @屬性名.setter 提供 setter（設定，可加驗證）
#   - 沒有 setter 的就是唯讀屬性（設定時會 AttributeError）
# ===================================================================

# ── 沒有保護的屬性會怎樣？ ────────────────────────────────
# 沒有 @property 時，屬性可以被設為任何值，包含不合法的值。

class BadStudent:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade   # 任何值都能直接存進去，沒有任何驗證

s = BadStudent("王小明", 85)
s.grade = -100   # 成績不能是負數，但 Python 完全不阻止你！
print(f"糟糕：{s.name} 的成績是 {s.grade}")  # -100

# ── @property：在存取屬性時加上驗證 ──────────────────────

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade   # 這行會觸發下面的 setter，自動做驗證！

    @property
    def grade(self):
        """
        getter：讀取 self.grade 時呼叫。
        實際資料存在 self._grade（底線開頭慣例：內部用，外部不直接存取）。
        """
        return self._grade

    @grade.setter
    def grade(self, value):
        """
        setter：執行 self.grade = xxx 時呼叫。
        在這裡做驗證，不合法就拋出 ValueError。
        """
        if not (0 <= value <= 100):
            raise ValueError(f"成績必須在 0～100，你給了 {value}")
        self._grade = value   # 通過驗證才存入 _grade

print("\n=== @property 守門員 ===")
s = Student("李大華", 90)    # __init__ 裡的 self.grade = 90 → 呼叫 setter → _grade = 90
print(s.grade)               # 讀取 → 呼叫 getter → 回傳 _grade = 90

s.grade = 75                 # 合法，通過驗證
print(s.grade)               # 75

try:
    s.grade = -10            # 觸發 setter → 驗證失敗 → 拋出 ValueError
except ValueError as e:
    print(f"錯誤：{e}")

# ── 唯讀屬性：計算出來的值不需要存 ──────────────────────
# 有些屬性是「計算出來的」，不該被直接設定。
# 只定義 getter，不定義 setter，就是唯讀屬性。

class Circle:
    def __init__(self, radius):
        self.radius = radius   # 半徑是基本資料

    @property
    def area(self):
        """
        面積是從 radius 計算出來的，不需要單獨儲存。
        每次讀取 .area 都會重新計算，確保和 radius 同步。
        沒有 setter，所以 c.area = 100 會 AttributeError。
        """
        import math
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        """直徑 = 半徑 * 2，也是計算值"""
        return self.radius * 2

print("\n=== 唯讀屬性（計算值）===")
c = Circle(5)
print(f"半徑 {c.radius}，直徑 {c.diameter:.1f}，面積 {c.area:.2f}")

# 只修改 radius，area 和 diameter 自動更新
c.radius = 10
print(f"半徑 {c.radius}，直徑 {c.diameter:.1f}，面積 {c.area:.2f}")

# ── 子類覆寫 setter ────────────────────────────────────────
# 研究生有加分機制，成績可以超過 100。
# 覆寫父類的 setter，調整驗證範圍。

class GradStudent(Student):

    @Student.grade.setter         # 指定是要覆寫 Student.grade 的 setter
    def grade(self, value):
        """研究生允許 0～150 的成績（有加分機制）"""
        if not (0 <= value <= 150):
            raise ValueError(f"研究生成績必須在 0～150，你給了 {value}")
        self._grade = value

print("\n=== 子類覆寫 setter ===")
g = GradStudent("張教授", 120)   # 超過 100 也合法
print(g.grade)                   # 120

# ─── 記憶重點 ──────────────────────────────────────────────
# @property           → getter，讀取 obj.屬性 時觸發
# @屬性名.setter      → setter，執行 obj.屬性 = 值 時觸發（可加驗證）
# 沒有 setter 的就是「唯讀屬性」（設定時 AttributeError）
# 實際資料習慣存在 _屬性名（底線開頭）
