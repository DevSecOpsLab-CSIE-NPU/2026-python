"""
Task 2: Student Ranking
根據分數 (desc)、年齡 (asc)、姓名 (asc) 進行多重條件排序。
"""

def sort_students(students, k):
    """
    排序規則：
    1. score: 由高到低 (加負號處理, 索引為 1)
    2. age: 由小到大 (索引為 2)
    3. name: 字母序由小到大 (索引為 0)
    """
    # x 的結構是 (name, score, age)
    # 所以索引分別是: name=0, score=1, age=2
    sorted_list = sorted(
        students, 
        key=lambda x: (-x[1], x[2], x[0])
    )
    return sorted_list[:k]

def main():
    import sys
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    try:
        n = int(input_data[0])
        k = int(input_data[1])
        
        students = []
        current = 2
        for _ in range(n):
            if current + 2 < len(input_data):
                name = input_data[current]
                score = int(input_data[current + 1])
                age = int(input_data[current + 2])
                students.append((name, score, age))
                current += 3
            
        # 執行排序
        results = sort_students(students, k)
        
        # 格式化輸出
        for res in results:
            print(f"{res[0]} {res[1]} {res[2]}")
            
    except (ValueError, IndexError):
        return

if __name__ == "__main__":
    main()