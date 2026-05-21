# R03. @property：屬性的守門員（詳解）
# 說明：
# 本檔展示如何使用 @property 把原本直接存取的屬性包成「有檢查邏輯」的屬性，
# 這樣可以在設定或讀取屬性時自動驗證或計算，兼顧 API 的簡潔與資料完整性。


# ---------- 範例：沒保護的屬性會出問題 ----------
# 若直接把屬性當公開欄位（public attribute）使用，任何人都能任意寫入，
# 可能導致不合理或錯誤的狀態（例如成績為負數）。
class BadStudent:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade   # 任何值都能被塞進去，沒有驗證


s = BadStudent("王小明", 85)
s.grade = -100   # 竟然允許，代表資料完整性無法保證
print(f"糟糕：{s.name} 的成績是 {s.grade}")  # -100


# ---------- 使用 @property：在存取屬性時加入檢查 ----------
# 實作步驟：
# 1) 在 class 中把實際資料藏在私有變數（慣例為 _grade）
# 2) 使用 @property 定義 getter，負責讀取屬性時回傳 _grade
# 3) 使用 @<prop>.setter 定義 setter，在設定時做驗證再賦值
class Student:
    """
    範例 Student，示範如何用 property 做屬性保護與驗證。

    設計要點：實際儲存位置使用底線開頭的名稱（例如 _grade），避免與 property 名稱衝突。
    """

    def __init__(self, name, grade):
        self.name = name
        # 直接設定 self.grade 會觸發下面定義的 setter，進而完成驗證
        self.grade = grade

    @property
    def grade(self):
        """getter：當讀取 student.grade 時被呼叫，回傳內部儲存的 _grade。"""
        return self._grade

    @grade.setter
    def grade(self, value):
        """setter：當執行 student.grade = value 時被呼叫，可在此處加入驗證邏輯。"""
        if not (0 <= value <= 100):
            # 提早拒絕不合理的輸入，維護物件的不變式（invariant）
            raise ValueError(f"成績必須在 0～100，你給了 {value}")
        self._grade = value


print("\n=== @property 守門員 ===")
s = Student("李大華", 90)
print(s.grade)    # 90

s.grade = 75      # 合法，通過檢查
print(s.grade)    # 75

try:
    s.grade = -10  # 觸發 ValueError（示範 setter 的保護效果）
except ValueError as e:
    print(f"錯誤：{e}")



# ---------- 唯讀屬性：計算出來的值不需要存放 ----------
# 如果某個屬性可以由其他資料即時計算出來（例如面積、直徑），
# 可以用 @property 只實作 getter 來暴露為「唯讀屬性」。這樣的屬性不會有 setter，
# 嘗試設定會得到 AttributeError，符合語意。
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        """面積是由 radius 計算而來，屬性為唯讀（不該被直接設定）。"""
        import math
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        # 直徑也是瞬時計算出來的屬性
        return self.radius * 2


print("\n=== 唯讀屬性（計算值）===")
c = Circle(5)
print(f"半徑 {c.radius}，直徑 {c.diameter:.1f}，面積 {c.area:.2f}")

c.radius = 10
print(f"半徑 {c.radius}，直徑 {c.diameter:.1f}，面積 {c.area:.2f}")

# 若嘗試設定唯讀屬性會得到 AttributeError（範例註解）：
# try:
#     c.area = 100
# except AttributeError as e:
#     print(e)



# ---------- 子類覆寫父類的 setter（延伸情境） ----------
# 有時子類需要修改父類屬性的驗證邏輯，例如研究生的成績允許超過 100。
# 示例中使用 @Student.grade.setter 的方式指定要覆寫哪個 property 的 setter。
class GradStudent(Student):

    @Student.grade.setter
    def grade(self, value):
        # 研究生允許的範圍更大
        if not (0 <= value <= 150):
            raise ValueError(f"研究生成績必須在 0～150，你給了 {value}")
        self._grade = value


print("\n=== 子類覆寫 setter（研究生） ===")
g = GradStudent("張教授", 120)
print(g.grade)   # 120（研究生可以超過 100）


# ---------- 記憶重點（快速參考） ----------
# - @property           → 定義 getter，讀取屬性時觸發
# - @屬性名.setter      → 定義 setter，設定屬性時觸發（可加入驗證）
# - 沒有 setter 的 property 為唯讀屬性（attempt to set -> AttributeError）
# - 慣例：實際儲存變數使用底線開頭（_grade）以避免命名衝突
