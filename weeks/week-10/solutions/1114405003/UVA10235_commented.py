import sys

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    limit = int(n ** 0.5)
    i = 5
    while i <= limit:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def solve():
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

if __name__ == "__main__":
    solve()