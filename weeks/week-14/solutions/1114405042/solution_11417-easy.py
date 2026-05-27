import sys
import math
import itertools

def solve(input_text):
    """
    計算 UVA 11417 - GCD (簡單易記版)
    利用 itertools.combinations 與 generator expression 縮減程式碼
    """
    lines = input_text.strip().split('\n')
    output = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        N = int(line)
        if N == 0:
            break
            
        # 簡單判斷法 (Easy Way) 💡
        # 1. itertools.combinations(range(1, N + 1), 2): 
        #    會自動從 1 到 N 之中挑選所有長度為 2 的組合 (i, j)，且自動保證 i < j。
        #    這完美對應了題目的條件 1 <= i < j <= N，不用再自己寫雙層 for 迴圈。
        # 2. 將每組 (i, j) 透過 math.gcd(i, j) 算出最大公因數。
        # 3. 最外面包一個 sum()，一口氣把所有算出來的 gcd 加總起來。
        # 這樣的寫法極致簡化，不容易寫錯縮排或迴圈邊界！
        G = sum(math.gcd(i, j) for i, j in itertools.combinations(range(1, N + 1), 2))
                
        output.append(str(G))
        
    return '\n'.join(output) + '\n'

if __name__ == '__main__':
    sys.stdout.write(solve(sys.stdin.read()))
