import sys

def solve():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            n = int(line)
        except ValueError:
            continue
            
        if n == 0:
            break
            
        binary_str = bin(n)[2:] # Remove '0b' prefix
        parity = binary_str.count('1')
        
        print(f"The parity of {binary_str} is {parity} (mod 2).")

if __name__ == "__main__":
    solve()
