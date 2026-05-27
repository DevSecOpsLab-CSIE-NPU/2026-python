T = int(input())

for test_num in range(1, T + 1):
    n = int(input())
    matrix = []
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    
    # Check if matrix is symmetric
    is_symmetric = True
    
    # Check 1: All elements must be non-negative
    for i in range(n):
        for j in range(n):
            if matrix[i][j] < 0:
                is_symmetric = False
                break
        if not is_symmetric:
            break
    
    # Check 2: Matrix must be centrally symmetric (180-degree rotational symmetry)
    # M[i][j] = M[n-1-i][n-1-j]
    if is_symmetric:
        for i in range(n):
            for j in range(n):
                if matrix[i][j] != matrix[n-1-i][n-1-j]:
                    is_symmetric = False
                    break
            if not is_symmetric:
                break
    
    if is_symmetric:
        print(f"Test #{test_num}: Symmetric")
    else:
        print(f"Test #{test_num}: Non-symmetric")

