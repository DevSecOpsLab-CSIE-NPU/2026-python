import sys

def solve():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
            
        parts = line.split()
        if len(parts) != 2:
            continue
            
        try:
            a = int(parts[0])
            b = int(parts[1])
        except ValueError:
            continue
        if a == 0 and b == 0:
            break
            
        carry = 0
        carry_count = 0
        while a > 0 or b > 0:
            digit_a = a % 10
            digit_b = b % 10
            current_sum = digit_a + digit_b + carry
            
            if current_sum >= 10:
                carry = 1
                carry_count += 1
            else:
                carry = 0
            a //= 10
            b //= 10
        if carry_count == 0:
            print("No carry operation.")
        elif carry_count == 1: 
            print("1 carry operation.")
        else:
            print(f"{carry_count} carry operations.")

if __name__ == '__main__':
    solve()