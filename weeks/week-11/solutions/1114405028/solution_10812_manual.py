n = int(input())
for _ in range(n):
    s, d = map(int, input().split())
    if (s + d) % 2 != 0:
        print("impossible")
    else:
        big = (s + d) // 2
        small = (s - d) // 2
        if small < 0:
            print("impossible")
        else:
            print(big, small)
