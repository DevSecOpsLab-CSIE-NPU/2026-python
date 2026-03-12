"""
Task 2: Student Ranking
回家作業：複合排序規則
"""


class Student:
    """學生資料類別"""
    
    def __init__(self, name, score, age):
        self.name = name
        self.score = int(score)
        self.age = int(age)
    
    def __repr__(self):
        return f"{self.name} {self.score} {self.age}"
    
    def __eq__(self, other):
        return (self.name == other.name and 
                self.score == other.score and 
                self.age == other.age)


def parse_students(lines):
    """
    將輸入行列表解析為 Student 物件列表
    
    Args:
        lines: list of strings in format "name score age"
        
    Returns:
        list: Student 物件列表
    """
    students = []
    for line in lines:
        parts = line.strip().split()
        if len(parts) != 3:
            raise ValueError(f"Invalid format: {line}")
        name, score, age = parts
        students.append(Student(name, score, age))
    return students


def rank_students(students, k):
    """
    排序學生並返回前 k 名
    
    排序規則：
    1. score 由高到低
    2. 同分時 age 由小到大
    3. 再同時 name 字母序由小到大
    
    Args:
        students: list of Student objects
        k: 要返回的學生數量
        
    Returns:
        list: 排序後前 k 名的 Student 列表
    """
    # 使用 sorted 配合 key 排序
    # 注意：score 是倒序（負值），age 和 name 是正序
    sorted_students = sorted(
        students,
        key=lambda s: (-s.score, s.age, s.name)
    )
    return sorted_students[:k]


def format_students(students):
    """
    格式化學生列表為輸出字串
    
    Args:
        students: list of Student objects
        
    Returns:
        str: 格式化的輸出字串
    """
    return '\n'.join(str(student) for student in students)


def process_ranking(n, k, student_lines):
    """
    主要處理函式
    
    Args:
        n: 學生數量
        k: 前 k 名
        student_lines: 學生資料行列表
        
    Returns:
        list: 排序後前 k 名的 Student 列表
    """
    if n != len(student_lines):
        raise ValueError(f"Expected {n} students, got {len(student_lines)}")
    
    students = parse_students(student_lines)
    return rank_students(students, k)


def main():
    """主程式"""
    print("=== Task 2: Student Ranking ===")
    print("輸入 n k（n=學生數量, k=前k名):")
    
    line = input().strip().split()
    n, k = int(line[0]), int(line[1])
    
    print(f"輸入 {n} 名學生資料（格式: name score age）:")
    student_lines = []
    for _ in range(n):
        student_lines.append(input().strip())
    
    try:
        ranked = process_ranking(n, k, student_lines)
        print("\n輸出:")
        print(format_students(ranked))
    except ValueError as e:
        print(f"錯誤：{e}")


if __name__ == "__main__":
    main()
