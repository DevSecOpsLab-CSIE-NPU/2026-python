import sys

def solve():
    first_line = sys.stdin.readline()
    if not first_line:
        return
    n = int(first_line)

    for _ in range(n):
        l_line = sys.stdin.readline()
        if not l_line:
            break
        length = int(l_line)
        
        cars = []
        while len(cars) < length:
            cars.extend(map(int, sys.stdin.readline().split()))
        
        swaps = 0
        for i in range(length):
            for j in range(0, length - i - 1):
                if cars[j] > cars[j+1]:
                    cars[j], cars[j+1] = cars[j+1], cars[j]
                    swaps += 1
        
        print(f"Optimal train swapping takes {swaps} swaps.")

if __name__ == "__main__":
    solve()