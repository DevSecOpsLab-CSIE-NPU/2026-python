def get_student_data():
    """獲取學生資料"""
    try:
        n = int(input("請輸入學生數量: "))
        k = int(input("請輸入顯示名次: "))
        students = []
        for i in range(n):
            data = input(f"請輸入第{i+1}位學生姓名、分數、年齡（以空格分隔）: ").split()
            if len(data) != 3:
                raise ValueError("輸入格式錯誤，請輸入姓名 分數 年齡")
            name, score, age = data
            students.append((name, int(score), int(age)))
        return students, k
    except ValueError as e:
        print(f"輸入錯誤: {e}")
        return [], 0

def sort_students(students):
    """按分數降序、年齡升序、姓名升序排序學生"""
    return sorted(students, key=lambda x: (-x[1], x[2], x[0]))

def display_top_students(sorted_students, k):
    """顯示前k名學生"""
    print("學生排序結果:")
    for student in sorted_students[:k]:
        print(f"{student[0]} {student[1]} {student[2]}")

def main():
    students, k = get_student_data()
    if not students:
        return
    sorted_students = sort_students(students)
    display_top_students(sorted_students, k)

if __name__ == "__main__":
    main()
