import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    it = iter(input_data)
    m = int(next(it))  # 測試資料組數
    
    for case_idx in range(m):
        n = int(next(it))  # 硬幣數量
        k = int(next(it))  # 秤重次數
        
        # 初始所有硬幣都有可能是假的 (1-indexed)
        candidates = set(range(1, n + 1))
        
        for _ in range(k):
            p = int(next(it))
            left = [int(next(it)) for _ in range(p)]
            right = [int(next(it)) for _ in range(p)]
            res = next(it)
            
            on_scale = set(left + right)
            
            if res == '=':
                # 秤上的全是真幣，移除可能
                candidates -= on_scale
            else:
                # 秤以外的全是真幣，交集保留秤上的硬幣
                candidates &= on_scale
        
        # 輸出處理
        if len(candidates) == 1:
            print(list(candidates)[0])
        else:
            print(0)
            
        # 題目要求各組測試資料間輸出一空白列
        if case_idx < m - 1:
            print()

if __name__ == "__main__":
    solve()