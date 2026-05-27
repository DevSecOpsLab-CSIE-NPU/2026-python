import math

while True:
    line = input().split()
    a, b = int(line[0]), int(line[1])
    
    if a == 0 and b == 0:
        break
    
    n1 = math.ceil(math.sqrt(a))
    n2 = math.floor(math.sqrt(b))
    
    if n1 <= n2:
        count = n2 - n1 + 1
    else:
        count = 0
    
    print(count)
