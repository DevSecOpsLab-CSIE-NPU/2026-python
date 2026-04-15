import sys

def solve():
    input_data = sys.stdin.read().split()
    idx, field_num = 0, 1

    while idx < len(input_data):
        N, M = int(input_data[idx]), int(input_data[idx+1])
        idx += 2
        if N == 0 == M: break
        
        # 建立一個 (N+2) x (M+2) 的二維陣列（多出一圈邊框，避免邊界檢查）
        res = [[0] * (M + 2) for _ in range(N + 2)]
        mines = []

        for r in range(1, N + 1):
            row_str = input_data[idx]
            idx += 1
            for c, char in enumerate(row_str, 1):
                if char == '*':
                    mines.append((r, c))
                    res[r][c] = '*'

        # 只對地雷周圍的格子進行 +1
        for r, c in mines:
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if isinstance(res[r+dr][c+dc], int):
                        res[r+dr][c+dc] += 1

        # 輸出結果
        if field_num > 1: print()
        print(f"Field #{field_num}:")
        for r in range(1, N + 1):
            print("".join(map(str, res[r][1:M+1])))
        
        field_num += 1

solve()