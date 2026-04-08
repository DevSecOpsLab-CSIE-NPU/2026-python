"""
================================================================================
Task 2: Student Ranking
================================================================================

題目說明：
    給定多筆學生資料（name score age），請依規則排序：
    1. score 由高到低
    2. 同分時 age 由小到大
    3. 再同時 name 字母序由小到大
    輸出排序後前 k 名

================================================================================
"""

from typing import List


def student_ranking(input_lines: List[str]) -> List[str]:
    """
    學生排名排序

    參數：
        input_lines: 輸入行列表，第一行為 "n k"，接著 n 行學生資料

    回傳：
        排序後前 k 名的學生資料列表
    """
    if not input_lines:
        return []

    # 解析輸入
    first_line = input_lines[0].strip().split()
    if len(first_line) < 2:
        return []

    n = int(first_line[0])
    k = int(first_line[1])

    if n == 0:
        return []

    students = []
    for line in input_lines[1 : 1 + n]:
        parts = line.strip().split()
        if len(parts) == 3:
            name, score, age = parts[0], int(parts[1]), int(parts[2])
            students.append((name, score, age))

    # 排序：score 由高到低 -> age 由小到大 -> name 由小到大
    sorted_students = sorted(students, key=lambda x: (-x[1], x[2], x[0]))

    # 取前 k 名
    top_k = sorted_students[:k]

    # 轉換為輸出格式
    return [f"{name} {score} {age}" for name, score, age in top_k]


def main():
    """主函式：讀取輸入並輸出結果"""
    try:
        lines = []
        while True:
            line = input()
            if not line:
                break
            lines.append(line)
        result = student_ranking(lines)
        for line in result:
            print(line)
    except EOFError:
        pass


if __name__ == "__main__":
    main()
