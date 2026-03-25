t = int(input())

for _ in range(t):
    data = list(map(int, input().split()))
    r = data[0]
    arr = data[1:]

    arr.sort()
    median = arr[r // 2]

    total = 0
    for x in arr:
        total += abs(x - median)

    print(total)