import sys

def solve(input_text):
    """
    計算 UVA 11461 - Square Numbers (簡單易記版)
    利用前綴和 (Prefix Sum) 的概念，將區間問題轉換為相減問題。
    """
    lines = input_text.strip().split('\n')
    output = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        a, b = map(int, line.split())
        
        if a == 0 and b == 0:
            break
            
        # 簡單判斷法 (Easy Way) 💡
        # 1. 數學概念：在 1 到 X 之間，共有「整數(根號X)」個完全平方數。
        # 2. Python 語法：X ** 0.5 就是開根號，再套用 int() 就會自動無條件捨去。
        # 3. 區間解法：因此求 [a, b] 之間的完全平方數數量，就等於：
        #    「1 到 b 的數量」減掉「1 到 (a - 1) 的數量」
        # 這樣寫完全不需要 import math，也不需要去想 ceil(進位) 或 floor(捨去) 的邊界細節！
        count = int(b ** 0.5) - int((a - 1) ** 0.5)
        
        output.append(str(count))
        
    return '\n'.join(output) + '\n'

if __name__ == '__main__':
    # 從標準輸入讀取所有資料並輸出結果
    sys.stdout.write(solve(sys.stdin.read()))
