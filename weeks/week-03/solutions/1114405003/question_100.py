"""
題目 100：Collatz序列 手打版本
檔名：question_100.py

這是學生在CPE考試當場手打出來的版本
特點：
- 最小化且直接的實現
- 邏輯清晰但保持簡洁
- 適合快速編寫和測試
"""

cache = {}

def get_cycle_length(n):
    """計算n的cycle-length"""
    if n == 1:
        return 1
    
    if n in cache:
        return cache[n]
    
    if n % 2 == 0:
        result = get_cycle_length(n // 2) + 1
    else:
        result = get_cycle_length(3 * n + 1) + 1
    
    cache[n] = result
    return result

def find_max_cycle(i, j):
    """找出[i,j]之間的最大cycle-length"""
    start = min(i, j)
    end = max(i, j)
    
    max_value = 0
    for n in range(start, end + 1):
        length = get_cycle_length(n)
        if length > max_value:
            max_value = length
    
    return max_value

# 主程式
if __name__ == '__main__':
    try:
        while True:
            line = input()
            a, b = map(int, line.split())
            ans = find_max_cycle(a, b)
            print(a, b, ans)
    except EOFError:
        pass
