import sys
from collections import Counter

def solve():
    data = sys.stdin.read().splitlines()
    if not data:
        return

    t = int(data[0].strip())
    idx = 1
    if idx < len(data) and data[idx].strip() == "":
        idx += 1

    out = []
    for _ in range(t):
        cnt = Counter()
        total = 0
        while idx < len(data) and data[idx].strip() != "":
            cnt[data[idx]] += 1
            total += 1
            idx += 1

        for name, count in sorted(cnt.items()):
            out.append(f"{name} {count * 100.0 / total:.4f}")

        if _ != t - 1:
            out.append("")

        while idx < len(data) and data[idx].strip() == "":
            idx += 1

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()