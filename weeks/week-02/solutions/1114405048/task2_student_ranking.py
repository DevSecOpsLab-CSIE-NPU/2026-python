"""
Task 2: Student Ranking
實現學生排名排序功能，支援複合排序鍵
"""

from typing import List, Tuple


class Student:
    """學生類別"""
    
    def __init__(self, name: str, score: int, age: int):
        self.name = name
        self.score = score
        self.age = age
    
    def __repr__(self):
        return f"{self.name} {self.score} {self.age}"


def parse_students(data: List[str]) -> List[Student]:
    """
    解析學生資料
    輸入格式：["name score age", ...]
    """
    students = []
    for line in data:
        parts = line.split()
        name = parts[0]
        score = int(parts[1])
        age = int(parts[2])
        students.append(Student(name, score, age))
    return students


def rank_students(students: List[Student]) -> List[Student]:
    """
    排序學生
    規則：
    1. score由高到低
    2. 同分時age由小到大
    3. 再同時name字母序由小到大
    """
    return sorted(
        students,
        key=lambda s: (-s.score, s.age, s.name)
    )


def process_ranking(lines: List[str]) -> str:
    """
    主流程：輸入為行列表，回傳排序結果
    第一行：n k
    接著n行：name score age
    輸出：前k名學生
    """
    first_line = lines[0].split()
    n = int(first_line[0])
    k = int(first_line[1])
    
    student_data = lines[1:n+1]
    students = parse_students(student_data)
    ranked = rank_students(students)
    
    # 取前k名
    top_k = ranked[:k]
    
    # 格式化輸出
    result = []
    for student in top_k:
        result.append(str(student))
    
    return '\n'.join(result)


if __name__ == '__main__':
    # 測試預設例子
    test_input = """6 3
amy 88 20
bob 88 19
zoe 92 21
ian 88 19
leo 75 20
eva 92 20""".split('\n')
    
    print(process_ranking(test_input))
