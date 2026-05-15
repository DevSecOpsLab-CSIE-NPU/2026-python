import sys

# 10908 - Easy Version
# 更加精簡的寫法

def solve():
    data = sys.stdin.read().split()
    if not data: return
    it = iter(data)
    try:
        T_cases = int(next(it))
    except StopIteration:
        return
        
    for _ in range(T_cases):
        try:
            m, n, q = int(next(it)), int(next(it)), int(next(it))
        except StopIteration:
            break
        grid = [next(it) for _ in range(m)]
        print(m, n, q)
        for _ in range(q):
            r, c = int(next(it)), int(next(it))
            char = grid[r][c]
            k = 0
            while r-k >= 0 and r+k < m and c-k >= 0 and c+k < n:
                # 檢查擴張層的字元是否都相同
                is_same = True
                for i in range(r-k, r+k+1):
                    if grid[i][c-k] != char or grid[i][c+k] != char:
                        is_same = False; break
                if not is_same: break
                for j in range(c-k, c+k+1):
                    if grid[r-k][j] != char or grid[r+k][j] != char:
                        is_same = False; break
                if is_same:
                    k += 1
                else:
                    break
            print(2 * (k-1) + 1)

if __name__ == "__main__":
    solve()
