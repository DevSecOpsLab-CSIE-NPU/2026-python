n = int(input())

for _ in range(n):
    length = int(input())
    cars = list(map(int, input().split())) if length > 0 else []

    swaps = 0
    for i in range(len(cars)):
        for j in range(i + 1, len(cars)):
            if cars[i] > cars[j]:
                swaps += 1

    print(f"Optimal train swapping takes {swaps} swaps.")