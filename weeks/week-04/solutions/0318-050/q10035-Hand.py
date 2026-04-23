import sys

for line in sys.stdin:
    parts = line.split()
    if len(parts) != 2:
        continue
        
    a, b = int(parts[0]), int(parts[1])
    
    if a == 0 and b == 0:
        break
        
    ans = 0
    c = 0
    
    while a > 0 or b > 0:
        total = (a % 10) + (b % 10) + c
        
        if total >= 10:
            ans += 1
            c = 1
        else:
            c = 0
            
        a //= 10
        b //= 10
        
    if ans == 0:
        print("No carry operation.")
    elif ans == 1:
        print("1 carry operation.")
    else:
        print(f"{ans} carry operations.")