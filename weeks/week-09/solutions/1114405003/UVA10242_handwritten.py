import sys


def same(a, b):
    return a[0] == b[0] and a[1] == b[1]


out = []
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    v = list(map(float, line.split()))
    if len(v) != 8:
        continue

    p1 = (v[0], v[1])
    p2 = (v[2], v[3])
    p3 = (v[4], v[5])
    p4 = (v[6], v[7])

    if same(p1, p3):
        d, a, b = p1, p2, p4
    elif same(p1, p4):
        d, a, b = p1, p2, p3
    elif same(p2, p3):
        d, a, b = p2, p1, p4
    else:
        d, a, b = p2, p1, p3

    x = a[0] + b[0] - d[0]
    y = a[1] + b[1] - d[1]
    out.append(f"{x:.3f} {y:.3f}")

sys.stdout.write("\n".join(out))
