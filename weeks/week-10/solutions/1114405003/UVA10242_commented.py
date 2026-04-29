import sys

def same(a, b):
    return a[0] == b[0] and a[1] == b[1]

def solve():
    out = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        vals = list(map(float, line.split()))
        if len(vals) != 8:
            continue

        p = [(vals[i], vals[i+1]) for i in range(0, 8, 2)]

        if same(p[0], p[2]):
            d, a, b = p[0], p[1], p[3]
        elif same(p[0], p[3]):
            d, a, b = p[0], p[1], p[2]
        elif same(p[1], p[2]):
            d, a, b = p[1], p[0], p[3]
        else:
            d, a, b = p[1], p[0], p[2]

        out.append(f"{a[0] + b[0] - d[0]:.3f} {a[1] + b[1] - d[1]:.3f}")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()