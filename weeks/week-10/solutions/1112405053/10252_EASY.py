import sys


def main():
    it = iter(sys.stdin.read().split())
    t = int(next(it, 0))
    out = []
    for _ in range(t):
        n = int(next(it))
        xs = [0]*n
        ys = [0]*n
        for i in range(n):
            xs[i] = int(next(it)); ys[i] = int(next(it))
        xs.sort(); ys.sort()
        if n & 1:
            xm = xs[n//2]; ym = ys[n//2]
            s = sum(abs(x - xm) for x in xs) + sum(abs(y - ym) for y in ys)
            cnt = 1
        else:
            xl = xs[n//2 - 1]; xh = xs[n//2]
            yl = ys[n//2 - 1]; yh = ys[n//2]
            s = sum(abs(x - xl) for x in xs) + sum(abs(y - yl) for y in ys)
            cnt = (xh - xl + 1) * (yh - yl + 1)
        out.append(f"{s} {cnt}")
    sys.stdout.write("\n".join(out))


if __name__ == '__main__':
    main()
