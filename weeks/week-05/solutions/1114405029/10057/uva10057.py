try:
    while True:
        n = int(input())
        numbers = [int(input()) for _ in range(n)]
        numbers.sort()

        if n % 2 == 1:
            median = numbers[n // 2]
            count = sum(1 for value in numbers if value == median)
            print(median, count, 1)
        else:
            low = numbers[n // 2 - 1]
            high = numbers[n // 2]
            count = sum(1 for value in numbers if low <= value <= high)
            print(low, count, high - low + 1)

except EOFError:
    pass