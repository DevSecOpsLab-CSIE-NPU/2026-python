import sys
for line in sys.stdin:
    s, d = map(int, line.split())
    while d > s:
        d -= s
        s += 1
    print(s)
