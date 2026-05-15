# =================================================================
# R01. 類別基礎（Python 3 標準函式庫 8.1 節）
# =================================================================
# 本範例展示如何定義類別 (Class)、初始化物件 (Object) 以及使用特殊方法。
# 物件導向 (OOP) 能幫助我們將資料與處理資料的方法封裝在一起。

# ── 1. 定義基本的類別：以「點 (Point)」為例 ────────────────────────
class Point:
    """
    這是一個代表平面座標系統中「點」的類別。
    """
    def __init__(self, x, y):
        """
        __init__ 是建構子 (Constructor)：
        當你執行 p = Point(0, 0) 時，Python 會自動呼叫這個方法。
        self 代表物件實例本身，用來綁定屬性 (Attribute)。
        """
        self.x = x
        self.y = y

    def __repr__(self):
        """
        __repr__ (Representation)：
        回傳物件的「官方」字串表達形式。主要給開發者看（例如在互動式介面直接打變數名）。
        理想情況下，repr 的內容應該可以直接拿來重新建立該物件。
        """
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        """
        __str__ (String)：
        回傳物件的「非正式」或「漂亮」的字串表達形式。主要給一般使用者看（例如 print(p) 時）。
        """
        return f"({self.x}, {self.y})"

    def distance_to(self, other):
        """
        這是一個自定義方法，用來計算當前點與另一個點之間的歐幾里得距離。
        """
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


# 測試 Point 類別
p1 = Point(0, 0)
p2 = Point(3, 4)

print(f"開發者模式輸出 (repr): {repr(p1)}")   # 呼叫 __repr__
print(f"使用者模式輸出 (str): {str(p2)}")     # 呼叫 __str__
print(f"兩點間的距離: {p1.distance_to(p2)}")  # 預期輸出 5.0


# ── 2. 類別變數 (Class Variable) vs 實例變數 (Instance Variable) ────────
class Student:
    # 類別變數：定義在所有方法之外，為所有建立出來的學生物件所共用。
    school = "國立澎湖科技大學"

    def __init__(self, name, student_id):
        # 實例變數：定義在 __init__ 內，每個學生物件都有自己獨立的姓名與學號。
        self.name = name
        self.student_id = student_id

    def __repr__(self):
        return f"Student({self.student_id}, {self.name})"

    def greeting(self):
        # 透過 self 可以存取實例變數與類別變數
        return f"我是 {self.school} 的 {self.name}"


# 建立兩個學生實例
s1 = Student("王小明", "1114405001")
s2 = Student("李小華", "1114405002")

print(s1.greeting())
print(f"透過實例存取學校: {s2.school}")
print(f"透過類別存取學校: {Student.school}")

# [重要] 修改類別變數會影響到「所有」實例
print("\n--- 修改類別變數後 ---")
Student.school = "NPU (National Penghu University)"
print(f"學生 1 的學校變成了: {s1.school}")
print(f"學生 2 的學校變成了: {s2.school}")
