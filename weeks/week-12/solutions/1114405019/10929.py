import sys

def solve():
    for line in sys.stdin:
        n_str = line.strip()
        if n_str == "0":
            break
        
        # N can be up to 1000 digits, so we use the property of 11.
        # (Sum of odd-position digits) - (Sum of even-position digits)
        odd_sum = 0
        even_sum = 0
        for i, digit in enumerate(n_str):
            if i % 2 == 0:
                odd_sum += int(digit)
            else:
                even_sum += int(digit)
        
        if abs(odd_sum - even_sum) % 11 == 0:
            print(f"{n_str} is a multiple of 11.")
        else:
            print(f"{n_str} is not a multiple of 11.")

if __name__ == "__main__":
    solve()
