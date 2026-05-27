import math

while True:
    line = input().split()
    a, b = int(line[0]), int(line[1])
    
    if a == 0 and b == 0:
        break
    
    # Find the smallest integer n such that n^2 >= a
    n1 = math.ceil(math.sqrt(a))
    # Find the largest integer m such that m^2 <= b
    n2 = math.floor(math.sqrt(b))
    
    # Count the number of perfect squares
    if n1 <= n2:
        count = n2 - n1 + 1
    else:
        count = 0
    
    print(count)
