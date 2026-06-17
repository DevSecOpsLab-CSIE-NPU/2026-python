# task2.py
# Task 2: Student Ranking

def rank_students(students, k):
    # 排序規則：
    # 1. score 由高到低 (-x[1])
    # 2. age 由小到大 (x[2])
    # 3. name 字母序由小到大 (x[0])
    sorted_students = sorted(students, key=lambda x: (-x[1], x[2], x[0]))
    return sorted_students[:k]

if __name__ == "__main__":
    import sys
    input_data = sys.stdin.read().split()
    if not input_data:
        sys.exit(0)
        
    n = int(input_data[0])
    k = int(input_data[1])
    
    students = []
    idx = 2
    for _ in range(n):
        name = input_data[idx]
        score = int(input_data[idx+1])
        age = int(input_data[idx+2])
        students.append((name, score, age))
        idx += 3
        
    results = rank_students(students, k)
    for name, score, age in results:
        print(f"{name} {score} {age}")
