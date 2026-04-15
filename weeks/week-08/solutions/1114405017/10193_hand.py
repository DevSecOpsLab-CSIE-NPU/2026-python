import sys, math
for line in sys.stdin:
    a = int(line.strip())
    t = a * a + 1
    x = math.isqrt(t)
    while t % x: 
        x -= 1
    print(x + t // x + 2 * a)