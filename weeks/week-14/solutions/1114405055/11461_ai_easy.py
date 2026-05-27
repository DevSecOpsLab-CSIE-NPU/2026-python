import sys, math

data = list(map(int, sys.stdin.read().split()))
# 每兩個為一組 (a, b) 讀取
for i in range(0, len(data)-1, 2):
    a, b = data[i], data[i+1]
    if a == 0 and b == 0: break
    # 計算範圍內的完全平方數個數
    count = math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1
    print(max(0, count))
