"""R01 類別基礎：Point 與 Student 範例。

這一版把 week-11 的課堂示範整理成可直接匯入的模組，
避免在載入時就輸出內容，方便單元測試反覆驗證。
"""


class Point:
    # Point 代表平面上的一個座標點，負責保存 x、y 兩個座標。
    def __init__(self, x, y):
        # 建立物件時，把傳入的座標存進實例屬性。
        self.x = x
        self.y = y

    # __repr__ 偏向給開發者看，通常要盡量長得像可直接重建物件的表示法。
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    # __str__ 偏向給使用者看，印出來要簡潔、直觀、容易閱讀。
    def __str__(self):
        return f"({self.x}, {self.y})"

    # 計算兩點之間的歐式距離，也就是平面座標中的直線距離。
    def distance_to(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


class Student:
    # 類別變數：所有 Student 物件都共用同一個 school 值。
    school = "國立澎湖科技大學"

    def __init__(self, name, student_id):
        # 實例變數：每個學生物件各自保存自己的姓名與學號。
        self.name = name
        self.student_id = student_id

    def __repr__(self):
        return f"Student({self.student_id}, {self.name})"

    def greeting(self):
        # 透過 self.school 讀取類別變數，方便之後統一修改學校名稱。
        return f"我是 {self.school} 的 {self.name}"


if __name__ == "__main__":
    # 只有直接執行這個檔案時才輸出示範結果，避免干擾單元測試。
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    print(repr(p1))
    print(str(p2))
    print(p1.distance_to(p2))

    s1 = Student("王小明", "11144050001")
    s2 = Student("李小華", "11144050002")
    print(s1.greeting())
    print(s2.school)
    print(Student.school)

    # 修改類別變數後，所有實例都會一起看到新的值。
    Student.school = "NPU"
    print(s1.school)
    print(s2.school)
