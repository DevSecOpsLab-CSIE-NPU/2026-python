# R03. @property：屬性的守門員
# =============================================================================
# 什麼是 @property？
#   @property 是 Python 的一個內建裝飾器（decorator），
#   讓你可以把「方法」偽裝成「屬性」來使用。
#
# 為什麼需要？
#   1. 資料驗證：設定屬性時可以檢查值是否合理
#   2. 唯讀屬性：有些值是由其他屬性計算出來的，不該被直接修改
#   3. 向後相容：原本直接存取屬性，後來想加邏輯時不必改 API
#
# 核心概念：
#   把 getter（讀取）和 setter（寫入）藏在屬性存取背後
#   使用者寫 obj.attr 就像在讀屬性，但實際上在執行方法
#
# 對應 Bloom's Taxonomy：記憶（Remember）— 背得出語法與使用時機
# =============================================================================


# ═════════════════════════════════════════════════════════════════════════════
# 沒有保護的屬性會怎樣？
# ═════════════════════════════════════════════════════════════════════════════
# 一般的 class 屬性可以直接存取，沒有任何檢查機制。
# 這意味著任何人都可以設定不合邏輯的值。

class BadStudent:
    """不好的設計：屬性完全沒有保護"""
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade   # 任何值都能塞進去，無法檢查

s = BadStudent("王小明", 85)
s.grade = -100   # 竟然可以！成績不可能是負數
print(f"糟糕：{s.name} 的成績是 {s.grade}")  # -100

# 解決方案有幾種：
#   1. 用 getter/setter 方法（Java 風格）：obj.get_grade() / obj.set_grade(v)
#      但 Python 程式碼通常不喜歡這種寫法
#   2. 用 @property：看起來像屬性，但有檢查邏輯
#      Python 慣用的作法


# ═════════════════════════════════════════════════════════════════════════════
# @property：在存取屬性時加上檢查
# ═════════════════════════════════════════════════════════════════════════════
# @property 的三個部分：
#
#   1. @property（getter）：
#       裝飾在方法上，讓 obj.grade 變成讀取方法
#       方法名稱就是「屬性名稱」
#
#   2. @屬性名.setter（setter）：
#       裝飾在方法上，讓 obj.grade = xxx 變成執行方法
#       可以在這裡加入驗證邏輯
#
#   3. 內部儲存變數：
#       習慣在屬性前加底線（_grade），表示「這是內部使用的」
#       避免 getter 和內部變數名稱衝突（否則會無窮遞迴）

class Student:
    """有 @property 保護的學生 class

    設計重點：
        - 外部使用 s.grade 來讀寫成績
        - 內部實際資料存在 s._grade
        - 設定時會檢查成績是否在 0~100 之間
    """
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade   # 這裡會自動呼叫下面的 setter

    @property
    def grade(self):
        """getter：讀取 self.grade 時自動呼叫

        注意：
            - 方法名稱是 grade，不是 get_grade
            - 回傳 self._grade（有底線，代表內部變數）
            - 如果這裡寫成 return self.grade，會無窮遞迴！
              因為 self.grade 又會呼叫這個 getter
        """
        return self._grade

    @grade.setter
    def grade(self, value):
        """setter：執行 self.grade = xxx 時自動呼叫

        可以在這裡加入各種驗證邏輯：
            - 型別檢查（必須是 int）
            - 範圍檢查（0~100）
            - 邏輯檢查（例如不能低於之前的分數）

        如果驗證失敗，拋出 ValueError 或 TypeError
        """
        if not (0 <= value <= 100):
            raise ValueError(f"成績必須在 0～100，你給了 {value}")
        self._grade = value

print("\n=== @property 守門員 ===")
s = Student("李大華", 90)
print(s.grade)    # 90（自動呼叫 getter）

s.grade = 75      # 合法，通過檢查（自動呼叫 setter）
print(s.grade)    # 75

try:
    s.grade = -10  # 觸發 ValueError，不會成功設定
except ValueError as e:
    print(f"錯誤：{e}")


# ═════════════════════════════════════════════════════════════════════════════
# 唯讀屬性：計算出來的值不需要存
# ═════════════════════════════════════════════════════════════════════════════
# 有些屬性是從其他屬性「計算」得來的，不該被直接設定。
# 作法：只定義 @property，不定義 @屬性名.setter。
# 這樣 obj.area = 100 會拋出 AttributeError。

class Circle:
    """圓形 class

    唯讀屬性：
        area（面積）：由 radius 計算，不可直接設定
        diameter（直徑）：由 radius * 2 計算，不可直接設定

    這樣設計的好處：
        radius 改變時，area 和 diameter 會自動更新
        不需要手動同步
    """
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        """面積 getter：由半徑計算

        注意：這裡沒有定義 setter
        所以 c.area = 100 會拋出 AttributeError
        """
        import math
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        """直徑 getter：半徑的兩倍

        也是唯讀屬性
        """
        return self.radius * 2

print("\n=== 唯讀屬性（計算值）===")
c = Circle(5)
print(f"半徑 {c.radius}，直徑 {c.diameter:.1f}，面積 {c.area:.2f}")

c.radius = 10
print(f"半徑 {c.radius}，直徑 {c.diameter:.1f}，面積 {c.area:.2f}")

# c.area = 100   # 這行會 AttributeError：唯讀屬性不能設定


# ═════════════════════════════════════════════════════════════════════════════
# 子類覆寫 setter
# ═════════════════════════════════════════════════════════════════════════════
# 有時候子類需要放寬或修改父類的驗證規則。
# 例如：一般學生成績最高 100 分，但研究生因為有加分機制，
# 可以到 150 分。這時可以在子類覆寫 setter。

class GradStudent(Student):
    """研究生：成績可以到 150（有加分機制）"""

    @Student.grade.setter
    def grade(self, value):
        """覆寫父類的 setter，放寬上限到 150

        注意語法：
            @Student.grade.setter
            意思是「我要覆寫 Student 類別的 grade 屬性的 setter」
        """
        if not (0 <= value <= 150):
            raise ValueError(f"研究生成績必須在 0～150，你給了 {value}")
        self._grade = value

print("\n=== 子類覆寫 setter ===")
g = GradStudent("張教授", 120)
print(g.grade)   # 120（研究生可以超過 100）


# ═════════════════════════════════════════════════════════════════════════════
# 記憶重點
# ═════════════════════════════════════════════════════════════════════════════
# 1. @property           → getter，讀取屬性時觸發
# 2. @屬性名.setter      → setter，設定屬性時觸發（可加驗證）
# 3. 沒有 setter 的屬性就是「唯讀屬性」
# 4. 內部資料習慣存在 _屬性名（前導底線代表「保護的、內部的」）
# 5. 常見應用：
#    - 數值範圍驗證（成績、年齡、分數）
#    - 型別驗證（確保是 int 不是 str）
#    - 計算屬性（面積、直徑、BMI）
#    - 快取（第一次計算後存起來）
# 6. 陷阱提醒：
#    getter 裡 return self.grade 會無窮遞迴！
#    一定要用 self._grade 這種內部變數
