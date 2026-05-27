import sys
import math

def solve(input_text):
    """
    計算 UVA 11461 - Square Numbers 的主邏輯（標準版）
    給定區間 [a, b]，計算裡面有多少個完全平方數。
    """
    lines = input_text.strip().split('\n')
    output = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # 解析每一行的 a 與 b
        parts = line.split()
        a = int(parts[0])
        b = int(parts[1])
        
        # 遇到 0 0 代表輸入結束
        if a == 0 and b == 0:
            break
            
        # 標準解法：利用 math 模組的 ceil 和 floor 取得區間的平方根整數範圍
        # 1. 尋找大於等於 a 的最小完全平方數的根（無條件進位）
        lower_bound = math.ceil(math.sqrt(a))
        # 2. 尋找小於等於 b 的最大完全平方數的根（無條件捨去）
        upper_bound = math.floor(math.sqrt(b))
        
        # 3. 計算這兩個根之間包含了多少個整數
        if lower_bound <= upper_bound:
            count = upper_bound - lower_bound + 1
        else:
            count = 0
            
        output.append(str(count))
        
    return '\n'.join(output) + '\n'

if __name__ == '__main__':
    # 從標準輸入讀取所有資料並輸出結果
    sys.stdout.write(solve(sys.stdin.read()))
