import sys
for line in sys.stdin:
    I = int(line.strip())
    if I == 0:
        break
    B = bin(I)[2:]
    P = B.count('1')
    print(f"The parity of {B} is {P} (mod 2).")