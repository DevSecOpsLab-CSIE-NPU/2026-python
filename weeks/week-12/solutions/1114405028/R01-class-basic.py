# R01. 類別基礎示範
# 這個範例展示 Python 類別的基本用法：建構子、實例屬性、類別屬性，以及 __repr__ / __str__ 的差異。

# Point 類別示範一個簡單的 2D 點座標物件
class Point:
    def __init__(self, x, y):
        # 建構子會在物件建立時呼叫，設定實例屬性 x, y
        self.x = x
        self.y = y

    def __repr__(self):
        # __repr__ 主要給開發者使用，通常回傳可用於重建物件的字串
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        # __str__ 主要給終端使用者使用，例如 print() 時顯示的內容
        return f"({self.x}, {self.y})"

    def distance_to(self, other):
        # 計算當前點到另一個 Point 的歐式距離
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


p1 = Point(0, 0)
p2 = Point(3, 4)

print(repr(p1))            # 顯示開發者模式的表示法 Point(0, 0)
print(str(p2))             # 顯示使用者模式的表示法 (3, 4)
print(p1.distance_to(p2))  # 計算距離：5.0


# Student 類別示範類別屬性（class variable）與實例屬性（instance variable）的差異
class Student:
    school = "國立澎湖科技大學"  # 類別變數，所有實例共用

    def __init__(self, name, student_id):
        self.name = name            # 每個實例自己的屬性
        self.student_id = student_id

    def __repr__(self):
        return f"Student({self.student_id}, {self.name})"

    def greeting(self):
        # 使用類別變數 school 建構問候語
        return f"我是 {self.school} 的 {self.name}"


s1 = Student("王小明", "11144050001")
s2 = Student("李小華", "11144050002")

print(s1.greeting())        # 呼叫實例方法
print(s2.school)            # 實例也能讀取類別變數
print(Student.school)       # 直接透過類別名稱讀取類別變數

# 修改類別變數會影響所有實例
Student.school = "NPU"
print(s1.school)            # NPU
print(s2.school)            # NPU
