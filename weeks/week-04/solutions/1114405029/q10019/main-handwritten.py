import sys
for line in sys.stdin:
    parts = line.split()
    if not parts: continue
    n1 = int(parts[0])
    n2 = int(parts[1])
    res = n1 - n2
    if res < 0: res *= -1
    print(res)