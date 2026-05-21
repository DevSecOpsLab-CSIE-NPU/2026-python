# R03. @property：屬性的守門員
# 讓 class 的屬性在「讀取」或「設定」時可以加入驗證邏輯
# 對應 Bloom's Taxonomy：記憶（Remember）— 背得出語法與使用時機
#
# 本題核心：
# @property 可以讓「方法」看起來像「屬性」一樣使用。
#
# 一般方法需要加括號呼叫：
# obj.method()
#
# 但 property 可以像屬性一樣讀取：
# obj.grade
#
# 更重要的是：
# @property 可以在「讀取屬性」或「設定屬性」時，
# 加入額外的檢查、計算或保護邏輯。
#
# 這份程式會示範：
# 1. 沒有保護的屬性可能被設定成不合理的值
# 2. 使用 @property getter 讀取屬性
# 3. 使用 @屬性名.setter 設定屬性並檢查資料是否合法
# 4. 使用沒有 setter 的唯讀屬性
# 5. 子類別覆寫父類別的 setter

# ── 沒有保護的屬性會怎樣？ ───────────────────────────────
#
# Python 預設的物件屬性通常可以直接讀取、直接修改。
#
# 例如：
# s.grade = -100
#
# 如果 class 沒有設計檢查機制，
# 那就算這個值明顯不合理，Python 也不會自動阻止。
#
# 這在小程式中可能還好，
# 但在正式程式或資料處理中會造成資料錯誤。
#
# 所以我們需要 property 來當「屬性的守門員」。

class BadStudent:
    # BadStudent 是一個沒有保護機制的學生類別。
    #
    # 它直接把 name 和 grade 存成公開屬性。
    # 任何人都可以從外部直接修改 grade，
    # 而且不會經過任何檢查。

    def __init__(self, name, grade):
        # 初始化學生姓名。
        self.name = name

        # 初始化成績。
        #
        # 這裡直接把 grade 存進 self.grade。
        # 因為沒有 setter 驗證，
        # 所以任何值都可以被放進 grade。
        self.grade = grade   # 任何值都能塞進去

# 建立一個 BadStudent 物件。
#
# 一開始成績是合理的 85。
s = BadStudent("王小明", 85)

# 直接從外部修改 s.grade。
#
# 這裡把成績改成 -100。
# 但成績理論上不應該是負數。
#
# 因為 BadStudent 沒有使用 @property 檢查，
# 所以 Python 仍然允許這個錯誤值被設定成功。
s.grade = -100   # 竟然可以！成績不能是負數

# 印出結果。
#
# 可以看到成績真的變成 -100，
# 這代表資料已經變成不合理狀態。
print(f"糟糕：{s.name} 的成績是 {s.grade}")  # -100

# ── @property：在存取屬性時加上檢查 ─────────────────────
#
# @property 可以把一個方法包裝成「屬性讀取」。
#
# 例如：
# def grade(self):
#     ...
#
# 加上 @property 後，
# 外部可以用：
# s.grade
#
# 而不是：
# s.grade()
#
# @grade.setter 則可以攔截設定屬性的動作。
#
# 例如：
# s.grade = 75
#
# 這行看起來像直接設定屬性，
# 但實際上會呼叫 setter 方法。
#
# 所以我們可以在 setter 裡面檢查：
# 成績是否介於 0 到 100。
#
# 如果合法，就存入真正的內部變數 self._grade。
# 如果不合法，就 raise ValueError 阻止錯誤資料進入物件。

class Student:
    # Student 是有保護機制的學生類別。
    #
    # 它使用 @property 控制 grade 的讀取與設定。
    #
    # 外部使用方式仍然很自然：
    # s.grade
    # s.grade = 90
    #
    # 但內部可以加上驗證邏輯。

    def __init__(self, name, grade):
        # 初始化學生姓名。
        self.name = name

        # 注意：
        # 這裡寫 self.grade = grade，
        # 看起來像是在直接設定屬性，
        # 但因為下面有定義 @grade.setter，
        # 所以這一行實際上會自動呼叫 setter。
        #
        # 也就是：
        # self.grade = grade
        #
        # 會觸發：
        # grade(self, value)
        #
        # 因此物件一建立時，初始成績也會被檢查是否合法。
        self.grade = grade   # 這裡會自動呼叫下面的 setter

    @property
    def grade(self):
        """getter：讀取 self.grade 時呼叫"""

        # 這是 getter。
        #
        # 當外部讀取：
        # s.grade
        #
        # Python 會自動呼叫這個方法。
        #
        # 真正的資料不是存在 self.grade，
        # 而是存在 self._grade。
        #
        # 原因：
        # 如果 getter 裡面 return self.grade，
        # 又會再次觸發 getter，
        # 造成無限遞迴。
        #
        # 所以實際資料通常會存在底線開頭的屬性，
        # 例如 self._grade。
        return self._grade   # 實際資料存在 _grade（底線代表「內部用」）

    @grade.setter
    def grade(self, value):
        """setter：執行 self.grade = xxx 時呼叫"""

        # 這是 setter。
        #
        # 當外部執行：
        # s.grade = value
        #
        # Python 會自動呼叫這個方法。
        #
        # value 就是等號右邊傳進來的新值。
        #
        # 例如：
        # s.grade = 75
        #
        # 則 value = 75。

        # 檢查 value 是否在 0 到 100 之間。
        #
        # 0 <= value <= 100 是 Python 的連續比較寫法。
        # 等同於：
        # value >= 0 and value <= 100
        #
        # not (...) 代表如果不符合這個範圍，
        # 就進入 if 區塊。
        if not (0 <= value <= 100):
            # raise ValueError 表示主動丟出一個錯誤。
            #
            # ValueError 通常用在：
            # 資料型態可能正確，
            # 但資料內容不合法的情況。
            #
            # 例如成績是數字，
            # 但成績範圍不合理。
            raise ValueError(f"成績必須在 0～100，你給了 {value}")

        # 如果通過檢查，
        # 就把 value 存進真正的內部屬性 self._grade。
        self._grade = value

# 印出區塊標題。
print("\n=== @property 守門員 ===")

# 建立 Student 物件。
#
# 這裡會呼叫 Student.__init__。
# __init__ 裡面的 self.grade = 90
# 會自動觸發 setter 檢查。
#
# 90 在 0 到 100 之間，所以合法。
s = Student("李大華", 90)

# 讀取 s.grade。
#
# 這會呼叫 getter，
# 回傳 self._grade。
print(s.grade)    # 90

# 設定 s.grade = 75。
#
# 這會呼叫 setter，
# 檢查 75 是否在 0 到 100 之間。
#
# 因為合法，所以成功更新 self._grade。
s.grade = 75      # 合法，通過檢查

# 再次讀取 s.grade。
#
# 這會呼叫 getter，
# 取得目前的 self._grade，也就是 75。
print(s.grade)    # 75

try:
    # 嘗試把成績設定成 -10。
    #
    # 這會呼叫 setter。
    # 因為 -10 不在 0 到 100 之間，
    # setter 會 raise ValueError。
    s.grade = -10  # 觸發 ValueError

except ValueError as e:
    # except 會接住 ValueError。
    #
    # as e 代表把錯誤物件存到變數 e。
    #
    # 這樣程式不會直接中斷，
    # 而是可以把錯誤訊息印出來。
    print(f"錯誤：{e}")

# ── 唯讀屬性：計算出來的值不需要存 ──────────────────────
#
# 有些屬性其實不需要真的存起來，
# 而是可以根據其他資料即時計算。
#
# 例如圓形：
# 半徑 radius 是真正需要儲存的資料。
#
# 直徑 diameter 可以由 radius * 2 算出來。
# 面積 area 可以由 math.pi * radius ** 2 算出來。
#
# 因此 diameter 和 area 不一定要另外存。
#
# 如果只定義 @property getter，
# 沒有定義 setter，
# 這個 property 就是「唯讀屬性」。
#
# 外部可以讀取：
# c.area
#
# 但不能設定：
# c.area = 100

class Circle:
    # Circle 類別用來表示圓形。
    #
    # 真正儲存的屬性是 radius。
    # area 和 diameter 則是根據 radius 計算出來的 property。

    def __init__(self, radius):
        # 儲存圓的半徑。
        self.radius = radius

    @property
    def area(self):
        """面積是計算出來的，不該被直接設定"""

        # area 是唯讀屬性。
        #
        # 每次讀取 c.area 時，
        # Python 都會執行這個方法重新計算面積。
        #
        # 因為面積依賴 radius，
        # 所以只要 radius 改變，
        # area 讀出來的結果也會跟著改變。
        import math

        # 圓面積公式：
        # π × 半徑平方
        #
        # math.pi 是 Python math 模組提供的圓周率。
        # self.radius ** 2 是半徑的平方。
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        # diameter 也是唯讀屬性。
        #
        # 每次讀取 c.diameter 時，
        # 都會根據目前的 radius 即時計算。
        #
        # 直徑公式：
        # 半徑 × 2
        return self.radius * 2

# 印出區塊標題。
print("\n=== 唯讀屬性（計算值）===")

# 建立一個半徑為 5 的圓。
c = Circle(5)

# 印出半徑、直徑、面積。
#
# c.radius 是一般屬性。
# c.diameter 是 property，會呼叫 diameter getter。
# c.area 是 property，會呼叫 area getter。
#
# :.1f 代表顯示到小數點後 1 位。
# :.2f 代表顯示到小數點後 2 位。
print(f"半徑 {c.radius}，直徑 {c.diameter:.1f}，面積 {c.area:.2f}")

# 修改半徑。
#
# radius 是一般屬性，
# 所以可以直接修改。
c.radius = 10

# 再次印出半徑、直徑、面積。
#
# 因為 diameter 和 area 都是根據 radius 即時計算，
# 所以 radius 改成 10 後，
# 直徑與面積也會自動反映新半徑。
print(f"半徑 {c.radius}，直徑 {c.diameter:.1f}，面積 {c.area:.2f}")

# try:
#     c.area = 100   # AttributeError：唯讀屬性不能設定
#
# 上面這段被註解掉，所以不會執行。
#
# 如果取消註解，會發生 AttributeError。
#
# 原因：
# Circle.area 只有 @property getter，
# 沒有 @area.setter。
#
# 所以 area 是唯讀屬性，不能直接設定。

# ── 子類覆寫 setter ───────────────────────────────────────
# 研究生有加分機制，成績可以超過 100
#
# 子類別可以繼承父類別的 property，
# 也可以覆寫父類別的 setter。
#
# 這裡 GradStudent 繼承 Student。
#
# Student 原本規定 grade 必須在 0 到 100。
# 但 GradStudent 希望允許成績到 150。
#
# 所以 GradStudent 重新定義 grade 的 setter，
# 讓它套用新的驗證範圍。

class GradStudent(Student):

    # @Student.grade.setter 的意思是：
    # 使用父類別 Student 裡面的 grade property，
    # 但重新指定它的 setter。
    #
    # 這樣 GradStudent 可以保留 grade 的 property 結構，
    # 但改寫設定 grade 時的檢查規則。
    @Student.grade.setter
    def grade(self, value):
        # 檢查研究生成績是否在 0 到 150 之間。
        #
        # 這裡和 Student 的 setter 類似，
        # 只是上限從 100 改成 150。
        if not (0 <= value <= 150):
            # 如果 value 不在合法範圍內，
            # 就丟出 ValueError。
            raise ValueError(f"研究生成績必須在 0～150，你給了 {value}")

        # 如果合法，就把成績存到內部屬性 self._grade。
        self._grade = value

# 印出區塊標題。
print("\n=== 子類覆寫 setter ===")

# 建立 GradStudent 物件。
#
# GradStudent 繼承 Student 的 __init__。
#
# Student.__init__ 裡會執行：
# self.grade = grade
#
# 但因為實際物件是 GradStudent，
# 所以會使用 GradStudent 覆寫後的 setter。
#
# 因此 120 是合法的，
# 因為 GradStudent 允許 0 到 150。
g = GradStudent("張教授", 120)

# 讀取 g.grade。
#
# getter 仍然使用繼承來的 grade getter，
# 回傳 self._grade。
print(g.grade)   # 120（研究生可以超過 100）

# 記憶重點 ──────────────────────────────────────────────────
# @property           → getter，讀取時觸發
# @屬性名.setter      → setter，設定時觸發（可加驗證）
# 沒有 setter 的就是「唯讀屬性」
# 實際資料習慣存在 _屬性名（底線開頭）
#
# 補充整理：
#
# 1. @property
#    可以讓方法像屬性一樣被讀取。
#
# 2. getter
#    負責讀取資料。
#    例如讀取 s.grade 時會觸發。
#
# 3. setter
#    負責設定資料。
#    例如執行 s.grade = 75 時會觸發。
#
# 4. setter 很適合用來做資料驗證。
#    例如檢查成績不能小於 0，也不能超過 100。
#
# 5. 內部真正存資料時，常用底線開頭的屬性。
#    例如 self._grade。
#
# 6. 如果只有 getter、沒有 setter，
#    那這個 property 就是唯讀屬性。
#
# 7. 子類別可以覆寫父類別的 setter，
#    讓同一個屬性在不同類別中有不同的驗證規則。