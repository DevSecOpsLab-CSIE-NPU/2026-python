# task2-easy.py
# Task 2: Student Ranking (簡單版)

def solve():
    # 範例輸入
    students = [
        ("amy", 88, 20),
        ("bob", 88, 19),
        ("zoe", 92, 21),
        ("ian", 88, 19),
        ("leo", 75, 20),
        ("eva", 92, 20)
    ]
    k = 3
    
    # 排序：
    # 1. 分數 (-x[1] 降序)
    # 2. 年齡 (x[2] 升序)
    # 3. 名字 (x[0] 升序)
    res = sorted(students, key=lambda x: (-x[1], x[2], x[0]))
    
    for i in range(min(k, len(res))):
        print(f"{res[i][0]} {res[i][1]} {res[i][2]}")

if __name__ == "__main__":
    solve()
