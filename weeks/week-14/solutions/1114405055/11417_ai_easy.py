import sys, math

# 讀取所有輸入並轉為整數
for n in map(int, sys.stdin.read().split()):
    if n == 0: break
    # 直接使用 Python 生成器與 sum 函數精簡算式
    print(sum(math.gcd(i, j) for i in range(1, n) for j in range(i + 1, n + 1)))
