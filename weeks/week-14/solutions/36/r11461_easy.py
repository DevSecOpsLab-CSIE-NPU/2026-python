import math

while True:

    a, b = map(int, input().split())

    if a == 0 and b == 0:
        break

    min_i = math.ceil(math.sqrt(a))
    max_i = math.floor(math.sqrt(b))

    count = max_i - min_i + 1

    if min_i > max_i:
        count = 0
    
    print(count)
