import sys

# 手打版本：中位數性質解決最小距離和
def solve():
    raw = sys.stdin.read().split()
    if not raw: return
    T = int(raw[0])
    idx = 1
    for _ in range(T):
        N = int(raw[idx]); idx += 1
        X, Y = [], []
        for i in range(N):
            X.append(int(raw[idx]))
            Y.append(int(raw[idx+1]))
            idx += 2
        X.sort(); Y.sort()
        m1, m2 = (N-1)//2, N//2
        # 最優解在 [X[m1], X[m2]] 和 [Y[m1], Y[m2]] 區間內
        min_d = 0
        bx, by = X[m1], Y[m1]
        for x in X: min_d += abs(x - bx)
        for y in Y: min_d += abs(y - by)
        ways = (X[m2]-X[m1]+1) * (Y[m2]-Y[m1]+1)
        print(f"{min_d} {ways}")

if __name__ == "__main__": solve()
