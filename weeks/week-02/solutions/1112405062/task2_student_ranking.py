"""
Task 2: Student Ranking
根據成績、年齡、姓名排序，輸出前 k 名
"""


def get_top_students(students_data, k):
    """
    取得排名最高的 k 名學生

    排序規則：
        1. score 由高到低
        2. 同分時 age 由小到大
        3. 再同時 name 字母序由小到大

    參數：
        students_data: 學生資料列表，每項為 (name, score, age)
        k: 要输出的前几名
    回傳：
        排序後的前 k 名學生
    """
    sorted_students = sorted(students_data, key=lambda s: (-s[1], s[2], s[0]))
    return sorted_students[:k]


def main():
    import sys

    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            lines = [line.strip() for line in f if line.strip()]
    else:
        lines = [line.strip() for line in sys.stdin if line.strip()]

    if not lines:
        return

    n, k = map(int, lines[0].split())
    students = []

    for i in range(1, n + 1):
        parts = lines[i].split()
        name = parts[0]
        score = int(parts[1])
        age = int(parts[2])
        students.append((name, score, age))

    result = get_top_students(students, k)

    for name, score, age in result:
        print(f"{name} {score} {age}")


if __name__ == "__main__":
    main()
