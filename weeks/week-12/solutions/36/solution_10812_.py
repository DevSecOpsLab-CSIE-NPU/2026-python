n = int(input())
for _ in range(n):
    s, d = map(int, input().split())
    
    if (s + d) % 2 != 0 or (s - d) % 2 != 0:
        print("impossible")
        continue
    
    high = (s + d) // 2
    low = (s - d) // 2

    if low < 0:
        print("impossible")
    else:
        print(high, low)