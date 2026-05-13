import sys

def solve():
    # Read all input at once and split by whitespace
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    try:
        n = int(input_data[0])
    except (ValueError, IndexError):
        return
        
    idx = 1
    for _ in range(n):
        if idx + 1 >= len(input_data):
            break
        try:
            s = int(input_data[idx])
            d = int(input_data[idx+1])
            idx += 2
            
            # a + b = s
            # a - b = d
            # 2a = s + d => a = (s + d) / 2
            # 2b = s - d => b = (s - d) / 2
            # a and b must be non-negative integers.
            if s >= d and (s + d) % 2 == 0:
                a = (s + d) // 2
                b = (s - d) // 2
                print(f"{a} {b}")
            else:
                print("impossible")
        except ValueError:
            idx += 1
            continue

if __name__ == "__main__":
    solve()
