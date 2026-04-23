import sys

# --- 簡單版快取 ---
# 這裡我們「只記住一開始問的數字」，不記錄中間經過的每一站。
# 這樣的寫法最單純，不用準備 path 陣列，也不用思考反轉 (reversed) 的邏輯。
cache = {1: 1}

def get_cycle_length(n):
    orig = n     # 記住一開始的數字
    step = 0     # 記錄我們目前走了幾步
    
    # 只要 n 還沒被算過 (不在 cache 裡)，就繼續往下算
    while n not in cache:
        if n % 2 == 1:
            n = 3 * n + 1
        else:
            n = n // 2
        step += 1
        
    # 迴圈結束時，代表我們撞到以前算過的數字了！
    # 總步數 = 剛剛自己走的步數 (step) + 該已知數字原本的步數 (cache[n])
    cache[orig] = step + cache[n]
    
    return cache[orig]

def solve(i, j):
    # 處理 UVA 100 陷阱：i 可能大於 j，所以先找出真正的起點和終點
    start = min(i, j)
    end = max(i, j)
    
    max_len = 0
    # 用最基本的 for 迴圈逐一檢查，找出最大值
    for n in range(start, end + 1):
        length = get_cycle_length(n)
        if length > max_len:
            max_len = length
            
    return i, j, max_len

if __name__ == '__main__':
    # 最標準、好記的輸入讀取寫法
    for line in sys.stdin:
        parts = line.split()
        if not parts:         # 如果這行是空的，就跳過
            continue
            
        i = int(parts[0])
        j = int(parts[1])
        
        res_i, res_j, max_len = solve(i, j)
        print(f"{res_i} {res_j} {max_len}")