# 100-easy.py
# UVA 100：3n+1 問題 (簡單版)

def get_cycle_length(n):
    count = 1
    while n != 1:
        if n % 2 == 1:
            n = 3 * n + 1
        else:
            n = n // 2
        count += 1
    return count

def solve():
    # 範例輸入模擬
    import sys
    for line in sys.stdin:
        parts = line.split()
        if not parts: continue
        i, j = map(int, parts)
        
        # 關鍵：i, j 可能反過來，但輸出要照原樣
        start, end = (i, j) if i <= j else (j, i)
        
        max_len = 0
        for n in range(start, end + 1):
            length = get_cycle_length(n)
            if length > max_len:
                max_len = length

        print(f"{i} {j} {max_len}")

if __name__ == "__main__":
    solve()
