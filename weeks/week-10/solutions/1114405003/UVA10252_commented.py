import sys
from collections import Counter

def solve():
    data = sys.stdin.read().splitlines()
    out = []

    i = 0
    while i + 1 < len(data):
        a = data[i]
        b = data[i + 1]
        i += 2

        ca = Counter(a)
        cb = Counter(b)

        common = []
        for ch in range(ord('a'), ord('z') + 1):
            k = min(ca.get(chr(ch), 0), cb.get(chr(ch), 0))
            if k > 0:
                common.append(chr(ch) * k)

        out.append("".join(common))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()