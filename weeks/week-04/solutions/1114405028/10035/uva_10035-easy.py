# Easy version
for line in sys.stdin:
    a, b = line.split()
    if a == '0' and b == '0':
        break
    carry = 0
    count = 0
    for x, y in zip(reversed(a), reversed(b)):
        if int(x) + int(y) + carry >= 10:
            count += 1
            carry = 1
        else:
            carry = 0
    # Handle remaining digits
    if len(a) > len(b):
        for x in reversed(a[len(b):]):
            if int(x) + carry >= 10:
                count += 1
                carry = 1
            else:
                carry = 0
    elif len(b) > len(a):
        for y in reversed(b[len(a):]):
            if int(y) + carry >= 10:
                count += 1
                carry = 1
            else:
                carry = 0
    if count == 0:
        print("No carry operation.")
    elif count == 1:
        print("1 carry operation.")
    else:
        print(f"{count} carry operations.")