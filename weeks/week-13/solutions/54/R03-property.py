# R03. @property：屬性的守門員
# 讓 class 的屬性在「讀取」或「設定」時可以加入驗證邏輯
# 對應 Bloom's Taxonomy：記憶（Remember）— 背得出語法與使用時機

# ── 沒有保護的屬性會怎樣？ ───────────────────────────────

class BadStudent:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade   # 任何值都能塞進去

s = BadStudent("王小明", 85)
s.grade = -100   # 竟然可以！成績不能是負數
print(f"糟糕：{s.name} 的成績是 {s.grade}")  # -100

# ── @property：在存取屬性時加上檢查 ─────────────────────

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade   # 這裡會自動呼叫下面的 setter

    @property
    def grade(self):
        """getter：讀取 self.grade 時呼叫"""
        return self._grade   # 實際資料存在 _grade（底線代表「內部用」）

    @grade.setter
    def grade(self, value):
        """setter：執行 self.grade = xxx 時呼叫"""
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
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        """面積是計算出來的，不該被直接設定"""
        import math
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        return self.radius * 2

print("\n=== 唯讀屬性（計算值）===")
c = Circle(5)
print(f"半徑 {c.radius}，直徑 {c.diameter:.1f}，面積 {c.area:.2f}")

c.radius = 10
print(f"半徑 {c.radius}，直徑 {c.diameter:.1f}，面積 {c.area:.2f}")

# try:
#     c.area = 100   # AttributeError：唯讀屬性不能設定

# ── 子類覆寫 setter ───────────────────────────────────────
# 研究生有加分機制，成績可以超過 100

class GradStudent(Student):

    @Student.grade.setter
    def grade(self, value):
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
