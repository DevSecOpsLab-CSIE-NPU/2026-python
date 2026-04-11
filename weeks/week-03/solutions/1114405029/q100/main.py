import sys

# 進階實作版：使用字典進行記憶化快取 (Memoization)
# 核心邏輯：透過快取避免重複計算已知的循環長度，大幅提升區間搜尋效率
def solve():
    # 快取字典，初始記錄 1 的循環長度為 1
    memo = {1: 1}

    def get_cycle_length(n):
        # 如果已經計算過，直接回傳快取的值
        if n in memo:
            return memo[n]
        
        # 依照題目規則計算下一個數字
        if n % 2 == 0:
            next_n = n // 2
        else:
            next_n = 3 * n + 1
            
        # 遞迴計算並存入快取
        memo[n] = 1 + get_cycle_length(next_n)
        return memo[n]

    # 處理標準輸入，直到 EOF
    for line in sys.stdin:
        parts = line.split()
        if not parts:
            continue
            
        i = int(parts[0])
        j = int(parts[1])
        
        # 題目陷阱：i 可能大於 j，需取出正確的左右界
        start = min(i, j)
        end = max(i, j)
        
        max_len = 0
        # 遍歷區間內的所有數字
        for n in range(start, end + 1):
            current_len = get_cycle_length(n)
            if current_len > max_len:
                max_len = current_len
                
        # 輸出原始的 i, j 以及最大循環長度
        print(f"{i} {j} {max_len}")

if __name__ == "__main__":
    solve()