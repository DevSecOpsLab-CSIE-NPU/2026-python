import sys
from collections import Counter


def solve():
    data = sys.stdin.read()
    if not data:
        return
    lines = data.splitlines()

    t = int(lines[0].strip())
    i = 1
    if i < len(lines) and lines[i].strip() == "":
        i += 1

    out = []
    for case_id in range(t):
        cnt = Counter()
        total = 0
        while i < len(lines) and lines[i].strip() != "":
            cnt[lines[i]] += 1
            total += 1
            i += 1

        for name in sorted(cnt):
            out.append(f"{name} {cnt[name] * 100.0 / total:.4f}")

        if case_id != t - 1:
            out.append("")

        while i < len(lines) and lines[i].strip() == "":
            i += 1

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
