"""
UVA 10038: Jolly Jumper

判斷序列相鄰元素差的絕對值是否為 1 到 n-1 的排列。
"""

try:
    while True:
        line = input().strip()
        if not line:
            continue
        
        parts = list(map(int, line.split()))
        n = parts[0]
        sequence = parts[1:n+1]
        
        if n == 1:
            print("Jolly")
            continue
        
        # 計算相鄰元素差的絕對值
        differences = set()
        for i in range(len(sequence) - 1):
            diff = abs(sequence[i] - sequence[i+1])
            differences.add(diff)
        
        # 檢查是否為 1 到 n-1 的排列
        expected = set(range(1, n))
        
        if differences == expected:
            print("Jolly")
        else:
            print("Not jolly")
except EOFError:
    pass
