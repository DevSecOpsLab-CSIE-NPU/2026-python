import sys
from collections import Counter


lines = sys.stdin.read().splitlines()
out = []
i = 0
while i + 1 < len(lines):
    a = lines[i]
    b = lines[i + 1]
    i += 2

    ca = Counter(a)
    cb = Counter(b)

    s = []
    for c in map(chr, range(256)):
        k = min(ca.get(c, 0), cb.get(c, 0))
        if k > 0:
            s.append(c * k)
    out.append("".join(s))

sys.stdout.write("\n".join(out))
