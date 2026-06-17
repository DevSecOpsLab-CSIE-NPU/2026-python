def rank_students(n, k, student_data):
    """
    Task 2: Student Ranking
    規則：
    1. score 由高到低 (降序)
    2. age 由小到大 (升序)
    3. name 字母序 (升序)
    """
    students = []
    for line in student_data:
        parts = line.split()
        if len(parts) == 3:
            name, score, age = parts[0], int(parts[1]), int(parts[2])
            students.append({'name': name, 'score': score, 'age': age})

    # 實作多條件排序：score 負號代表降序，其餘為預設升序
    # 這是符合 August 老師「不准用巢狀迴圈」的要求
    sorted_students = sorted(students, key=lambda x: (-x['score'], x['age'], x['name']))

    # 輸出前 k 名
    result = []
    for i in range(min(k, len(sorted_students))):
        s = sorted_students[i]
        result.append(f"{s['name']} {s['score']} {s['age']}")

    return result

if __name__ == "__main__":
    # 測試範例
    data = [
        "amy 88 20",
        "bob 88 19",
        "zoe 92 21",
        "ian 88 19",
        "leo 75 20",
        "eva 92 20"
    ]
    rankings = rank_students(6, 3, data)
    for r in rankings:
        print(r)
