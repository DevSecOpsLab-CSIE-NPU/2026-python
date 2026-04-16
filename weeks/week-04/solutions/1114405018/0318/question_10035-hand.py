import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    a, b = map(int, line.split())
    if a == 0 and b == 0:
        break

    carry = 0
    count = 0
    while a > 0 or b > 0:
        s = (a % 10) + (b % 10) + carry
        if s >= 10:
            count += 1
            carry = 1
        else:
            carry = 0
        a //= 10
        b //= 10

    if count == 0:
        print("No carry operation.")
    elif count == 1:
        print("1 carry operation.")
    else:
        print(f"{count} carry operations.")