import sys, math

# 讀取標準輸入中的所有數字並逐一處理
for line in sys.stdin:
    a = int(line.strip())
    t = a * a + 1
    
    # 從根號向下找第一個能整除的因數 x
    # t // x 即為對應的另一個大因數 y
    x = math.isqrt(t)
    while t % x: 
        x -= 1
        
    # 直接輸出 x + y + 2a (即 b + c)
    print(x + t // x + 2 * a)