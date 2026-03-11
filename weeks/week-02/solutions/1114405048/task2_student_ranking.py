"""
Task 2: Student Ranking
給定多筆學生資料（name score age），請依規則排序：
1. score 由高到低
2. 同分時 age 由小到大
3. 再同時 name 字母序由小到大
輸出排序後前 k 名
"""


def parse_student_data(n, k, lines):
    """
    解析學生資料
    
    Args:
        n: 學生數量
        k: 要輸出的前 k 名數量
        lines: 學生資料行的列表
    
    Returns:
        學生列表和 k 值
    """
    students = []
    for line in lines:
        parts = line.split()
        name = parts[0]
        score = int(parts[1])
        age = int(parts[2])
        students.append((name, score, age))
    return students, k


def rank_students(students, k):
    """
    依排序規則排名並返回前 k 名
    
    規則：
    1. score 由高到低 (負號表示降序)
    2. 同分時 age 由小到大
    3. 再同時 name 字母序由小到大
    
    Args:
        students: (name, score, age) 元組列表
        k: 返回前 k 名
    
    Returns:
        排序後的前 k 名學生
    """
    # 使用多條件排序：先按 score 降序，再按 age 升序，最後按 name 升序
    sorted_students = sorted(
        students,
        key=lambda x: (-x[1], x[2], x[0])
    )
    return sorted_students[:k]


def format_output(students):
    """
    格式化學生資料為輸出字符串
    
    Args:
        students: 排序後的學生列表
    
    Returns:
        格式化後的字符串列表
    """
    output = []
    for name, score, age in students:
        output.append(f"{name} {score} {age}")
    return output


def process_ranking(n, k, lines):
    """
    主要處理函式
    
    Args:
        n: 學生數量
        k: 要輸出的前 k 名
        lines: 學生資料行的列表
    
    Returns:
        前 k 名學生的格式化輸出
    """
    students, k = parse_student_data(n, k, lines)
    ranked = rank_students(students, k)
    return format_output(ranked)


def main():
    """主程式入口"""
    try:
        first_line = input().strip()
        n, k = map(int, first_line.split())
        
        lines = []
        for _ in range(n):
            lines.append(input().strip())
        
        results = process_ranking(n, k, lines)
        for line in results:
            print(line)
    except EOFError:
        pass


if __name__ == "__main__":
    main()
