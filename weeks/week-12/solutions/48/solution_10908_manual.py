t = int(input())
for _ in range(t):
    m, n, q = map(int, input().split())
    g = []
    for _ in range(m):
        g.append(input())
    print(m, n, q)
    for _ in range(q):
        r, c = map(int, input().split())
        ch = g[r][c]
        k = 0
        while r-k-1>=0 and r+k+1<m and c-k-1>=0 and c+k+1<n:
            ok = True
            for i in range(c-k, c+k+1):
                if g[r-k-1][i] != ch or g[r+k+1][i] != ch:
                    ok = False
            for i in range(r-k, r+k+1):
                if g[i][c-k-1] != ch or g[i][c+k+1] != ch:
                    ok = False
            if ok:
                k += 1
            else:
                break
        print(2*k+1)
