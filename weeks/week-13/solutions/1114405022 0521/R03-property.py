# R03. @property：屬性的守門員
# 讓 class 的屬性在「讀取」或「設定」時可以加入驗證邏輯
# 對應 Bloom's Taxonomy：記憶（Remember）— 背得出語法與使用時機

# ── 沒有保護的屬性會怎樣？ ───────────────────────────────

class BadStudent:
    """不好的設計：屬性沒有任何保護機制"""

    def __init__(self, name, grade):
        self.name = name    # 直接將參數指派給屬性
        self.grade = grade   # 任何值都能塞進去，完全沒檢查

s = BadStudent("王小明", 85)   # 建立物件，成績設為 85
s.grade = -100   # 竟然可以！成績不能是負數，但沒有任何防護
print(f"糟糕：{s.name} 的成績是 {s.grade}")  # 輸出 -100（不合理！）

# ── @property：在存取屬性時加上檢查 ─────────────────────

class Student:
    """使用 @property 保護成績屬性的學生類別"""

    def __init__(self, name, grade):
        self.name = name      # 姓名不需要檢查
        self.grade = grade    # 這裡會自動呼叫下面的 setter（@grade.setter）

    @property
    def grade(self):
        """
        getter：讀取 self.grade 時自動呼叫
        注意：方法名稱叫 grade，但實際資料存在 self._grade
        使用者在外部寫 s.grade 時，自動觸發此方法
        """
        return self._grade   # 實際資料存在 _grade（底線代表「內部用」）

    @grade.setter
    def grade(self, value):
        """
        setter：執行 self.grade = xxx 時自動呼叫
        可以在這裡加入驗證邏輯，確保資料合法性
        """
        if not (0 <= value <= 100):   # 檢查成績是否在 0~100 範圍內
            raise ValueError(f"成績必須在 0～100，你給了 {value}")  # 不合法就拋出例外
        self._grade = value   # 合法才存入內部變數

print("\n=== @property 守門員 ===")
s = Student("李大華", 90)   # 呼叫 __init__，觸發 setter 檢查 90 合法
print(s.grade)    # 90（讀取時觸發 getter，回傳 self._grade）

s.grade = 75      # 75 合法，通過 setter 檢查
print(s.grade)    # 75（再次讀取確認）

try:
    s.grade = -10  # -10 不合法，觸發 ValueError
except ValueError as e:
    print(f"錯誤：{e}")  # 印出錯誤訊息

# ── 唯讀屬性：計算出來的值不需要存 ──────────────────────

import math  # 匯入 math 模組，用於圓周率

class Circle:
    """圓形類別，示範唯讀的計算屬性"""

    def __init__(self, radius):
        self.radius = radius  # 半徑是可讀寫的

    @property
    def area(self):
        """
        面積是唯讀的計算屬性
        只定義了 getter（@property），沒有定義 setter，
        所以外部無法對 area 賦值
        """
        return math.pi * self.radius ** 2  # 圓面積公式：π × r²

    @property
    def diameter(self):
        """直徑也是唯讀的計算屬性"""
        return self.radius * 2  # 直徑 = 半徑 × 2

print("\n=== 唯讀屬性（計算值）===")
c = Circle(5)                     # 建立半徑為 5 的圓
print(f"半徑 {c.radius}，直徑 {c.diameter:.1f}，面積 {c.area:.2f}")

c.radius = 10                     # 修改半徑為 10
print(f"半徑 {c.radius}，直徑 {c.diameter:.1f}，面積 {c.area:.2f}")  # 面積和直徑自動重新計算

# try:
#     c.area = 100   # AttributeError：唯讀屬性不能設定（因為沒有定義 setter）

# ── 子類覆寫 setter ───────────────────────────────────────
# 研究生有加分機制，成績可以超過 100

class GradStudent(Student):
    """
    研究生類別，繼承 Student 但放寬成績上限到 150
    使用 @Student.grade.setter 來覆寫父類別的 setter
    """

    @Student.grade.setter  # 覆寫父類 Student 的 grade setter
    def grade(self, value):
        """研究生 setter：成績範圍放寬到 0～150"""
        if not (0 <= value <= 150):   # 研究生可以到 150 分
            raise ValueError(f"研究生成績必須在 0～150，你給了 {value}")
        self._grade = value   # 合法成績存入內部變數

print("\n=== 子類覆寫 setter ===")
g = GradStudent("張教授", 120)  # 120 在 0~150 範圍內，合法
print(g.grade)   # 120（研究生可以超過 100）

# 記憶重點 ──────────────────────────────────────────────────
# @property           → getter，讀取時觸發
# @屬性名.setter      → setter，設定時觸發（可加驗證）
# 沒有 setter 的就是「唯讀屬性」
# 實際資料習慣存在 _屬性名（底線開頭）
