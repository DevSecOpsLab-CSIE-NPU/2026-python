import sys
data = sys.stdin.read().split()
S = int(data[0])
for k in range(S):
    N = int(data[1 + k*3])
    p = float(data[2 + k*3])
    i = int(data[3 + k*3])
    if p == 0:
        print("0.0000")
    else:
        q = 1 - p
        ans = (p * q**(i-1)) / (1 - q**N)
        print(f"{ans:.4f}")