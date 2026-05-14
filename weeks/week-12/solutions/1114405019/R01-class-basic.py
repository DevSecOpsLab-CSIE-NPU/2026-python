# R01-class-basic.py
# 示範基礎類別、__init__、實例/類別變數及 __repr__/__str__

class Student:
    # 類別變數 (Class Variable): 所有實例共享
    school_name = "Python Academy"
    student_count = 0

    def __init__(self, name: str, age: int):
        # 實例變數 (Instance Variable): 每個實例獨立
        self.name = name
        self.age = age
        Student.student_count += 1
        self.id = Student.student_count

    def __repr__(self):
        # 供開發者閱讀的字串表示，通常可用於重建該物件
        return f"Student(name='{self.name}', age={self.age})"

    def __str__(self):
        # 供使用者閱讀的字串表示，print() 時會呼叫
        return f"[學號 {self.id}] 姓名: {self.name}, 年齡: {self.age} ({self.school_name})"

if __name__ == "__main__":
    print("=== 基礎類別示範 ===")
    s1 = Student("Alice", 20)
    s2 = Student("Bob", 22)

    print(s1)  # 呼叫 __str__
    print(repr(s2))  # 呼叫 __repr__
    
    print(f"目前學生總數: {Student.student_count}")
    print(f"S1 的學校: {s1.school_name}")
