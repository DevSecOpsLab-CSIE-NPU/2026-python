import sys

def solve():
    text = sys.stdin.read()
    if not text:
        return
        
    text = text.replace('N', ' ').replace('=', ' ')
    tokens = text.split()
    
    T = int(tokens[0])
    idx = 1
    for t in range(1, T + 1):
        n = int(tokens[idx])
        idx += 1
        length = n * n
        matrix = [int(x) for x in tokens[idx : idx + length]]
        idx += length
        
        if matrix == matrix[::-1] and all(x >= 0 for x in matrix):
            print(f"Test #{t}: Symmetric.")
        else:
            print(f"Test #{t}: Non-symmetric.")

if __name__ == '__main__':
    solve()