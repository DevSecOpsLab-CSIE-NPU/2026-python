import sys

# 逐行處理每組測資（直到 EOF）
for line in sys.stdin:
    parts = line.split()
    n = int(parts[0])
    # 只有一個數時，必定為 Jolly
    if n == 1:
        print("Jolly")
        continue
    
    # 計算所有相鄰元素差值的絕對值
    sequence = [int(parts[i]) for i in range(1, n + 1)]
    differences = set()
    
    for i in range(n - 1):
        diff = abs(sequence[i] - sequence[i + 1])
        differences.add(diff)
    
    # 差值集合若剛好是 1 到 n-1，則為 Jolly
    if differences == set(range(1, n)):
        print("Jolly")
    else:
        print("Not jolly")
