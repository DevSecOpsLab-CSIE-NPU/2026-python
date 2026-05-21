# R03. @property：屬性的守門員（Property Getter/Setter）
# 範例與說明（繁體中文）：
# @property 提供了在屬性讀取或設定時插入邏輯的途徑，常用於資料驗證、延遲計算（lazy evaluation）或把內部表示與使用者介面分離。
# 實作要點：實際資料通常存在以底線開頭的私有屬性（例如 _grade），以避免與 property 名稱衝突。

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
        # 指派給 self.grade 時會呼叫下方定義的 setter，進行驗證或轉換
        self.grade = grade   # 這裡會自動呼叫下面的 setter

        # R03. @property：屬性的守門員
        # 讓 class 的屬性在「讀取」或「設定」時可以加入驗證或計算邏輯
        # 註解使用繁體中文（詳細說明）以利教學與理解
        # 要點：
        # - `@property` 會將一個方法轉為「屬性存取的介面」，讀取時呼叫 getter。
        # - `@x.setter` 會將另一個方法註冊為該屬性的 setter，賦值時呼叫。
        # - 真正儲存資料時常用 `_name`（底線）避免與 property 名稱互相呼叫（遞迴）。
    @property
    def grade(self):
        """getter：在讀取 self.grade 時自動執行，可加入額外的轉換或延遲計算。"""
        # 實際資料儲存在 _grade，透過 property 隱藏內部實作
        return self._grade   # 實際資料存在 _grade（底線代表「內部用」）
                # 範例：沒有任何 guard（守門）機制的屬性
                # 直接把輸入值放進 public 屬性，會導致不合法的值被接受

    @grade.setter
    def grade(self, value):
        """setter：在設定 self.grade 時被呼叫，可做驗證、型別轉換或觸發其他副作用。"""
        # 範例驗證：成績必須在 0～100 之間
        if not (0 <= value <= 100):
            raise ValueError(f"成績必須在 0～100，你給了 {value}")
        # 驗證通過後將值存到內部屬性 _grade
        self._grade = value

print("\n=== @property 守門員 ===")
s = Student("李大華", 90)
                # 在建構子裡使用 self.grade = grade，會觸發下面定義的 setter
                # 這樣可以讓建構時也同樣受到驗證機制保護
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
        """area 是唯讀屬性，根據 radius 計算並回傳。

        若計算成本高且 radius 不常變動，可考慮用快取（lazy evaluation）策略儲存結果。
        """
        import math
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        # 直徑為 radius 的兩倍，示範簡單的唯讀屬性定義
        return self.radius * 2

print("\n=== 唯讀屬性（計算值）===")
c = Circle(5)
print(f"半徑 {c.radius}，直徑 {c.diameter:.1f}，面積 {c.area:.2f}")
                # radius 本身是可讀寫的公開屬性

c.radius = 10
print(f"半徑 {c.radius}，直徑 {c.diameter:.1f}，面積 {c.area:.2f}")

# try:
#     c.area = 100   # AttributeError：唯讀屬性不能設定

# ── 子類覆寫 setter ───────────────────────────────────────
# 研究生有加分機制，成績可以超過 100

class GradStudent(Student):

    @Student.grade.setter
    def grade(self, value):
        # 在子類覆寫 setter：示範如何放寬驗證邏輯（例如研究生允許較高分數）
        if not (0 <= value <= 150):
            raise ValueError(f"研究生成績必須在 0～150，你給了 {value}")
        self._grade = value

print("\n=== 子類覆寫 setter ===")
g = GradStudent("張教授", 120)
print(g.grade)   # 120（研究生可以超過 100）

# 記憶重點 ──────────────────────────────────────────────────
# - @property           → 定義 getter，讀取屬性時會自動呼叫
# - @屬性名.setter      → 定義 setter，設定屬性時會自動呼叫，可用於驗證或轉換
# - 若只定義 getter 而無 setter，該屬性為唯讀（attempting to set 會引發 AttributeError）
# - 實際資料習慣存在 _屬性名（例如 _grade），以避免與 property 名稱衝突
# - 子類可以透過 @BaseClass.attr.setter 來覆寫父類的 setter，以修改驗證邏輯
# - 設計建議：
#   - property 適合用於輕量的封裝與驗證；若有複雜狀態管理或副作用，考慮明確方法（如 set_radius()）
#   - 保持 getter/ setter 的副作用最小，避免在屬性讀取時做長時間或破壞性操作
