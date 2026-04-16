"""
Task 2: Student Ranking

輸入多筆學生資料（name score age），依下列規則排序並輸出前 k 名：
1. score 由高到低
2. 同分時 age 由小到大
3. 再同時 name 字母序由小到大

輸入格式：
第一行：n k
接著 n 行：name score age
"""
import sys


def parse_students(lines: list[str]) -> list[tuple]:
    """將字串列表解析為 (name, score, age) 的 tuple 列表。"""
    students = []
    for line in lines:
        parts = line.split()
        name, score, age = parts[0], int(parts[1]), int(parts[2])
        students.append((name, score, age))
    return students


def rank_students(students: list[tuple], k: int) -> list[tuple]:
    """依 score↓, age↑, name↑ 排序後取前 k 名。"""
    sorted_students = sorted(students, key=lambda s: (-s[1], s[2], s[0]))
    return sorted_students[:k]


def student_ranking(input_lines: list[str]) -> None:
    """解析輸入並印出排名前 k 的學生。"""
    first = input_lines[0].split()
    n, k = int(first[0]), int(first[1])
    students = parse_students(input_lines[1: n + 1])
    ranked = rank_students(students, k)
    for name, score, age in ranked:
        print(f"{name} {score} {age}")


if __name__ == "__main__":
    lines = sys.stdin.read().strip().splitlines()
    student_ranking(lines)
