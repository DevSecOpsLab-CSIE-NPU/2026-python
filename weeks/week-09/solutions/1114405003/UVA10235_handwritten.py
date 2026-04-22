import sys


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


out = []
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    n = int(line)
    if not is_prime(n):
        out.append(f"{n} is not prime.")
        continue

    r = int(str(n)[::-1])
    if r != n and is_prime(r):
        out.append(f"{n} is emirp.")
    else:
        out.append(f"{n} is prime.")

sys.stdout.write("\n".join(out))
