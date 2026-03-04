"""
Task 2: Student Ranking
給定多筆學生資料（name score age），依規則排序：
1. score 由高到低
2. 同分時 age 由小到大
3. 再同時 name 字母序由小到大
輸出排序後前 k 名。
"""


def parse_student(line):
    """
    解析學生資料行。
    
    Args:
        line: 格式為 "name score age" 的字串
    
    Returns:
        (name, score, age) 的元組，score 和 age 為整數
    """
    parts = line.split()
    name = parts[0]
    score = int(parts[1])
    age = int(parts[2])
    return (name, score, age)


def sort_students(students, k):
    """
    依規則排序學生並返回前 k 名。
    
    排序規則：
    1. score 由高到低（負值排序）
    2. 同分時 age 由小到大
    3. 再同時 name 字母序由小到大
    
    Args:
        students: 學生資料列表，每個元素為 (name, score, age) 元組
        k: 返回前 k 名
    
    Returns:
        排序後前 k 名的列表
    """
    # 使用 sorted 和 key 函式進行多鍵排序
    # score 為負值以實現高到低排序
    sorted_list = sorted(
        students,
        key=lambda x: (-x[1], x[2], x[0])
    )
    return sorted_list[:k]


def format_student(student):
    """
    格式化學生資料為輸出字串。
    
    Args:
        student: (name, score, age) 元組
    
    Returns:
        格式為 "name score age" 的字串
    """
    name, score, age = student
    return f"{name} {score} {age}"


def main():
    """主程式入口。"""
    # 第一行：n（學生數） k（前 k 名）
    first_line = input().strip()
    n, k = map(int, first_line.split())
    
    # 讀取 n 行學生資料
    students = []
    for _ in range(n):
        line = input().strip()
        student = parse_student(line)
        students.append(student)
    
    # 排序並獲得前 k 名
    top_k = sort_students(students, k)
    
    # 輸出結果
    for student in top_k:
        print(format_student(student))


if __name__ == '__main__':
    main()
