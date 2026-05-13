import sys

def get_degree(s, degree):
    digit_sum = sum(int(d) for d in s)
    if digit_sum == 9:
        return degree + 1
    if digit_sum < 9:
        return 0
    return get_degree(str(digit_sum), degree + 1)

def solve():
    for line in sys.stdin:
        n_str = line.strip()
        if n_str == "0":
            break
        
        # Calculate initial digit sum
        initial_sum = sum(int(d) for d in n_str)
        
        if initial_sum % 9 != 0:
            print(f"{n_str} is not a multiple of 9.")
        else:
            # If initial_sum is 9, degree is 1. 
            # Otherwise we need to recurse.
            if initial_sum == 9:
                degree = 1
            else:
                degree = get_degree(str(initial_sum), 1)
            print(f"{n_str} is a 9-degree of {degree}.")

if __name__ == "__main__":
    solve()
