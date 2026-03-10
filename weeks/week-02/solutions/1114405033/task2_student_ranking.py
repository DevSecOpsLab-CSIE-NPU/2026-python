def rank_students(students, k):
    
    sorted_students = sorted(students, key=lambda x: (-x[1], x[2], x[0]))
    return sorted_students[:k]

if __name__ == "__main__":
    try:
        line1 = input().split()
        if not line1: exit()
        n, k = map(int, line1)
        data = []
        for _ in range(n):
            parts = input().split()
            data.append((parts[0], int(parts[1]), int(parts[2])))
        
        results = rank_students(data, k)
        for res in results:
            print(f"{res[0]} {res[1]} {res[2]}")
    except EOFError:
        pass