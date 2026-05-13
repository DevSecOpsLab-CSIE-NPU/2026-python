import sys
def solve():
    for line in sys.stdin:
        n = line.strip()
        if not n or n == "0": break
        b = f"{int(n):b}"
        print(f"The parity of {b} is {b.count('1')} (mod 2).")
if __name__ == "__main__": solve()
