while True:
    n = input().strip()
    if n == "0":
        break

    total = 0 

    for i, d in enumerate(reversed(n)):
        digit_value = int(d)
        if i % 2 == 0:
            total += digit_value
        else:
            total -= digit_value
    if total % 11 == 0:
        print(f"{n} is a multiple of 11.")
    else:
        print(f"{n} is not a multiple of 11.")
        