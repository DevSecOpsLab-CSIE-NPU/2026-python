# R01. 類別基礎（8.1）
# __init__ / 方法 / __repr__ / __str__

# ── 最簡單的 class ────────────────────────────────────────
# 定義一個Point類別，用於表示二維平面上的點
class Point:
    # __init__方法是建構函式，在建立物件時自動呼叫
    # self參數代表物件本身，x和y是座標值
    def __init__(self, x, y):
        self.x = x  # 將x座標儲存為實例變數
        self.y = y  # 將y座標儲存為實例變數

    # __repr__方法定義物件的「官方」字串表示
    # 主要給開發者使用，理想情況下應該能用eval()重建物件
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    # __str__方法定義物件的「非官方」字串表示
    # 主要給一般使用者看，print()函式會優先使用這個方法
    def __str__(self):
        return f"({self.x}, {self.y})"

    # 實例方法：計算與另一個點的距離
    def distance_to(self, other):
        # 使用歐幾里得距離公式：sqrt((x1-x2)^2 + (y1-y2)^2)
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


# 建立兩個Point物件實例
p1 = Point(0, 0)  # 原點
p2 = Point(3, 4)  # 點(3,4)

# 示範__repr__和__str__的差異
print(repr(p1))             # 呼叫__repr__：Point(0, 0)
print(str(p2))              # 呼叫__str__：(3, 4)
print(p1.distance_to(p2))  # 計算兩點距離：5.0

# ── 類別變數 vs 實例變數 ──────────────────────────────────
# 類別變數是所有實例共享的變數，而實例變數是每個物件獨有的
class Student:
    school = "國立澎湖科技大學"    # 類別變數：所有Student實例共享此變數

    # 建構函式：初始化實例變數
    def __init__(self, name, student_id):
        self.name = name            # 實例變數：每個學生有自己的名字
        self.student_id = student_id  # 實例變數：每個學生有自己的學號

    # __repr__方法：定義物件的字串表示
    def __repr__(self):
        return f"Student({self.student_id}, {self.name})"

    # 實例方法：使用類別變數和實例變數產生問候語
    def greeting(self):
        return f"我是 {self.school} 的 {self.name}"


# 建立兩個Student實例
s1 = Student("王小明", "11144050001")
s2 = Student("李小華", "11144050002")

# 示範實例方法呼叫
print(s1.greeting())  # 使用實例的greeting方法
print(s2.school)      # 透過實例存取類別變數
print(Student.school) # 透過類別名稱直接存取類別變數

# 修改類別變數會影響所有實例
Student.school = "NPU"  # 修改類別變數
print(s1.school)      # s1的school屬性也被改變
print(s2.school)      # s2的school屬性也被改變
