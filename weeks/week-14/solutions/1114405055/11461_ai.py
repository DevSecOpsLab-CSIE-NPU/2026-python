# UVA 11461 - Square Numbers (AI 版本)
import sys
import math

def solve():
    # 處理所有輸入字串
    data = sys.stdin.read().split()
    idx = 0
    while idx < len(data):
        a = int(data[idx])
        b = int(data[idx+1])
        idx += 2
        
        # 結束條件為 a = 0, b = 0
        if a == 0 and b == 0:
            break
            
        # 計算區間內的完全平方數個數
        # 使用開根號後分別取 ceiling 和 floor 來計算
        start = math.ceil(math.sqrt(a))
        end = math.floor(math.sqrt(b))
        
        # 輸出範圍內的值數量
        if start <= end:
            print(end - start + 1)
        else:
            print(0)

if __name__ == '__main__':
    solve()
