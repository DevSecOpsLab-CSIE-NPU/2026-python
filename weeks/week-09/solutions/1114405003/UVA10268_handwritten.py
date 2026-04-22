import sys


def f(x, a):
    n = len(a) - 1
    if n <= 0:
        return 0

    ans = a[0] * n
    d = n - 1
    for i in range(1, n):
        ans = ans * x + a[i] * d
        d -= 1
    return ans


lines = [s.strip() for s in sys.stdin if s.strip()]
out = []
i = 0
while i + 1 < len(lines):
    x = int(lines[i])
    a = list(map(int, lines[i + 1].split()))
    out.append(str(f(x, a)))
    i += 2

sys.stdout.write("\n".join(out))
