import sys

# 公式：P(i) = ((1-p)^(i-1) * p) / (1 - (1-p)^n)

tokens = sys.stdin.read().split()
if not tokens:
    raise SystemExit

s = int(tokens[0])
idx = 1
out = []

for _ in range(s):
    n = int(tokens[idx])
    p = float(tokens[idx + 1])
    i = int(tokens[idx + 2])
    idx += 3

    if p == 0.0:
        out.append("0.0000")
        continue

    q = 1.0 - p
    ans = (q ** (i - 1) * p) / (1.0 - q ** n)
    out.append(f"{ans:.4f}")

print("\n".join(out))
