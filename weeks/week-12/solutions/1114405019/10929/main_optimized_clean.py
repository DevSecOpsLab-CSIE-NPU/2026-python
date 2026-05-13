import sys
def solve():
    for line in sys.stdin:
        n = line.strip()
        if n == "0": break
        if not n: continue
        if int(n) % 11 == 0: print(f"{n} is a multiple of 11.")
        else: print(f"{n} is not a multiple of 11.")
if __name__ == "__main__": solve()
