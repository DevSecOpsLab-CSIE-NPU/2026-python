while True:
    x = input()
    if x == "0":
        break
    s = x
    d = 0
    while len(s) > 1:
        t = sum(int(c) for c in s)
        s = str(t)
        d += 1
    if s == "9":
        print(f"{x} is a multiple of 9.")
    else:
        print(f"{x} is not a multiple of 9.")
