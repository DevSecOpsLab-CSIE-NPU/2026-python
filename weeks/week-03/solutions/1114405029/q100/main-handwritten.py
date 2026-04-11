import sys

def solve():
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 2:
            continue
            
        num1 = int(parts[0])
        num2 = int(parts[1])
        
        start = min(num1, num2)
        end = max(num1, num2)
        
        max_length = 0
        
        for n in range(start, end + 1):
            current_n = n
            count = 1
            
            while current_n != 1:
                if current_n % 2 == 0:
                    current_n = current_n // 2
                else:
                    current_n = 3 * current_n + 1
                count += 1
            
            if count > max_length:
                max_length = count
        
        print(f"{num1} {num2} {max_length}")

if __name__ == "__main__":
    solve()