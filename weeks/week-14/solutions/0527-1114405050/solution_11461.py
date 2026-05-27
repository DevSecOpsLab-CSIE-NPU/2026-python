import sys
import math

def solve():
    """
    UVA 11461 - Square Numbers
    讀取標準輸入，針對每組區間 [a, b]，計算當中的完全平方數個數。
    """
    # 讀取全部輸入，並以空白或換行分割為一個個的 token (字串)
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    # 由於每筆測資有 a, b 兩個數字，因此用迴圈一次取兩個 (step=2)
    for i in range(0, len(input_data), 2):
        if i + 1 >= len(input_data):
            break
            
        a = int(input_data[i])
        b = int(input_data[i+1])
        
        # 遇到 a=0 且 b=0 代表測資結束
        if a == 0 and b == 0:
            break
            
        # 核心數學邏輯：
        # 在區間 [1, N] 之間的完全平方數個數，剛好等於 floor(sqrt(N))，即 math.isqrt(N)。
        # 因此，區間 [a, b] 內的個數 = ([1, b] 的個數) - ([1, a-1] 的個數)。
        ans = math.isqrt(b) - math.isqrt(a - 1)
        
        # 輸出結果
        print(ans)

if __name__ == '__main__':
    solve()