t = int(input())

for _ in range(t):
    n, p, i = input().split()
    n = int(n)
    p = float(p)
    i = int(i)

    if p == 0:
        print("0.0000")
    else:
        q = 1 - p
        ans = (q ** (i - 1) * p) / (1 - q ** n)
        print(f"{ans:.4f}")