while True:

    i = int(input())
    if i == 0:
        break
    binary = bin(i)[2:] 
    parity = binary.count('1')

    print(f"The parity of {binary} is {parity} (mod 2).")
    