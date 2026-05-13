n= int(input())

for _ in range(n):
    S, D = map(int, input().split())
    
    if (S + D) % 2 != 0:
        print("impossible")
        continue
    
    high = (S + D) // 2
    low = (S - D) // 2
    
    if low < 0:
        print("impossible")
    else:
        print(f"{high} {low}")
        