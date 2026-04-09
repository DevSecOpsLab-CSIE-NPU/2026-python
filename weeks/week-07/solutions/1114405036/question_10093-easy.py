# 題目 10093: 炮兵部署問題 - 簡單版本
# 使用遞歸來枚舉每行的狀態，適合小 N。

def max_artillery_easy(N, M, grid):
    # 簡單版本：遞歸枚舉每行狀態
    masks = []
    for row in grid:
        mask = 0
        for j in range(M):
            if row[j] == 'P':
                mask |= (1 << j)
        masks.append(mask)

    def is_valid_state(s, mask):
        if (s & mask) != s:
            return False
        prev = -10
        for j in range(M):
            if (s & (1 << j)):
                if j - prev <= 2:
                    return False
                prev = j
        return True

    def compatible(s1, s2):
        for j in range(M):
            if (s2 & (1 << j)):
                for dj in range(max(0, j-2), min(M, j+3)):
                    if (s1 & (1 << dj)):
                        return False
        return True

    # 遞歸函數
    def dfs(row, prev_s):
        if row == N:
            return 0
        max_cnt = 0
        for s in range(1 << M):
            if is_valid_state(s, masks[row]) and compatible(prev_s, s):
                cnt = bin(s).count('1') + dfs(row + 1, s)
                max_cnt = max(max_cnt, cnt)
        return max_cnt

    return dfs(0, 0)  # prev_s = 0 for row 0

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    M = int(data[1])
    grid = []
    idx = 2
    for i in range(N):
        row = data[idx]
        grid.append(row)
        idx += 1
    result = max_artillery_easy(N, M, grid)
    print(result)