import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    num_cases = int(input_data[0])
    curr = 1
    for _ in range(num_cases):
        L = int(input_data[curr])
        trains = list(map(int, input_data[curr+1 : curr+1+L]))
        curr += L + 1
        swaps = 0
        for i in range(len(trains)):
            for j in range(len(trains)-1-i):
                if trains[j] > trains[j+1]:
                    trains[j], trains[j+1] = trains[j+1], trains[j]
                    swaps += 1
        print(f"Optimal train swapping takes {swaps} swaps.")

if __name__ == "__main__":
    solve()