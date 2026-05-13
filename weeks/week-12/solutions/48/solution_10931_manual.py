while True:
    n = int(input())
    if n == 0:
        break
    b = bin(n)[2:]
    c = b.count('1')
    print(f"The parity of {b} is {c} (mod 2).")
