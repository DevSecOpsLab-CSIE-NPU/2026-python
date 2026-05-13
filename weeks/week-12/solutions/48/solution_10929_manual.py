while True:
    x = input()
    if x == "0":
        break
    odd = 0
    even = 0
    for i, c in enumerate(reversed(x)):
        if i % 2 == 0:
            odd += int(c)
        else:
            even += int(c)
    if (odd - even) % 11 == 0:
        print(f"{x} is a multiple of 11.")
    else:
        print(f"{x} is not a multiple of 11.")
