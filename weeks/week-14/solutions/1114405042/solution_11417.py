import sys
import math

def solve(input_text):
    """
    計算 UVA 11417 - GCD
    題意：給定 N，求所有 1 <= i < j <= N 的 gcd(i, j) 加總。
    此為標準雙重迴圈解法。
    """
    lines = input_text.strip().split('\n')
    output = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        N = int(line)
        # 遇到 0 代表輸入結束
        if N == 0:
            break
            
        # G 用來儲存所有的最大公因數總和
        G = 0
        
        # 雙重迴圈枚舉所有的 i 和 j (1 <= i < j <= N)
        for i in range(1, N):
            for j in range(i + 1, N + 1):
                # 利用 math.gcd() 計算 i 和 j 的最大公因數
                G += math.gcd(i, j)
                
        # 將結果存入輸出陣列
        output.append(str(G))
        
    # 用換行符號組合所有結果
    return '\n'.join(output) + '\n'

if __name__ == '__main__':
    # 讀取標準輸入並輸出結果
    sys.stdout.write(solve(sys.stdin.read()))
