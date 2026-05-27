import sys
import math

def solve():
    # 讀取全部的輸入資料，轉換為整數後，建立成一個「迭代器(Iterator)」
    nums = iter(map(int, sys.stdin.read().split()))
    
    # 神奇小技巧：zip(nums, nums) 會自動從 nums 中一次抓取兩個元素配對給 a 和 b
    # 完全不需要自己處理索引值 (index) 的問題！
    for a, b in zip(nums, nums):
        # 遇到 a=0 且 b=0 代表程式結束
        if a == 0 and b == 0:
            break
            
        # 核心數學邏輯：區間內完全平方數的數量 = floor(sqrt(b)) - floor(sqrt(a-1))
        # math.isqrt 會直接回傳平方根的整數部分 (即無條件捨去)
        print(math.isqrt(b) - math.isqrt(a - 1))

if __name__ == '__main__':
    solve()