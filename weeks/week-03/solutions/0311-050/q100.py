import sys

# --- 核心概念：記憶化 (Memoization) ---
# 建立一個全域的快取字典 (Cache)，初始狀態已知 1 的 cycle-length 為 1。
# 因為 UVA 100 的多筆測資中可能會重複查詢相同的數字，將 cache 設為全域變數，
# 就可以跨測資保留已計算過的結果，大幅減少重複運算，避免 Time Limit Exceeded (TLE)。
cache = {1: 1}

def get_cycle_length(n):
    """
    計算單一整數 n 的 cycle-length (循環長度)
    依據 3n+1 演算法 (Collatz conjecture)：
    - 若 n 為奇數，則 n = 3n + 1
    - 若 n 為偶數，則 n = n / 2
    直到 n 等於 1 為止，所經過的數字個數即為 cycle-length。
    """
    original_n = n  # 保留原始輸入的 n，以便最後從 cache 中取值回傳
    path = []       # 用來記錄在尚未碰到 cache 內的數字前，沿途經過的所有數字
    
    # 當目前的數字 n 還沒被計算過 (不在 cache 字典中) 時，持續推進
    while n not in cache:
        path.append(n)  # 將當前的數字加入路徑清單
        
        # 判斷 n 是奇數還是偶數，根據題目規則進行運算
        if n % 2 == 1:
            n = 3 * n + 1  # 奇數：乘以 3 加 1
        else:
            n = n // 2     # 偶數：除以 2 (使用整數除法，確保結果為整數)
            
    # 迴圈結束代表目前的 n 已經是我們計算過、且存在 cache 裡面的數字了。
    # 接下來進行「反向回推 (Backtracking)」，把剛剛走過但還沒記錄的路徑都算出來並存入 cache。
    step = cache[n] # 取得這個已知數字的剩餘步數
    
    # 為什麼要反轉？因為越晚加入 path 的數字，離終點 (已知 n) 越近。
    for p in reversed(path):
        step += 1        # 往回退一步，步數 +1
        cache[p] = step  # 將路徑上的數字對應的 cycle-length 存入字典
        
    # 回傳最初詢問的 original_n 的 cycle-length
    return cache[original_n]

def solve(i, j):
    """
    計算 i 到 j 區間內 (包含 i, j) 的最大 cycle-length
    回傳格式為 Tuple: (原始 i, 原始 j, 最大 cycle-length)
    """
    # UVA 100 經典陷阱：測資給定的 i 有可能大於 j (例如輸入 10 1)。
    # 但迴圈計算區間時必須由小到大，因此先用 min() 和 max() 重新排序為 start 和 end。
    start, end = min(i, j), max(i, j)
    
    # 使用生成器表達式 (Generator Expression) 結合 max() 函式，
    # 簡潔地走訪 start 到 end 之間的所有數字，並找出最大的 cycle-length。
    max_len = max(get_cycle_length(n) for n in range(start, end + 1))
            
    # 題目要求輸出的前兩個數字必須維持「原始輸入的順序」，因此回傳 i, j 而非 start, end
    return (i, j, max_len)

if __name__ == '__main__':
    # --- 系統標準輸入處理 (Standard Input) ---
    # UVA 解題常用技巧：使用 sys.stdin 讀取測資直到檔案結束 (EOF)。
    for line in sys.stdin:
        # 使用海象運算子 (Walrus Operator, :=) 同時進行賦值與條件判斷。
        # 若 line.split() 有內容 (非空陣列)，則指派給 parts 並進入 if 區塊。
        if parts := line.split():
            i, j = int(parts[0]), int(parts[1])
            # 呼叫 solve 函式取得結果
            res_i, res_j, max_len = solve(i, j)
            # 依據題目要求的格式印出結果：i j max_cycle_length
            print(f"{res_i} {res_j} {max_len}")