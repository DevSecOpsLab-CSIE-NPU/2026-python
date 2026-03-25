while True:
    line = input().split()
    a, b = int(line[0]), int(line[1])
    if a == 0 and b == 0:
        break
    
    carry = 0
    count = 0
    while a > 0 or b > 0 or carry > 0:
        digit_a = a % 10
        digit_b = b % 10
        total = digit_a + digit_b + carry
        if total >= 10:
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
