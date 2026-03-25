def solve(numbers):
    if not numbers:
        return 0, 0, 0
    
    numbers.sort()
    n = len(numbers)
    
    if n % 2 == 1:
        median = numbers[n // 2]
        lower = upper = median
    else:
        lower = numbers[n // 2 - 1]
        upper = numbers[n // 2]
    
    a = lower
    distances = [abs(x - a) for x in numbers]
    min_distance = min(distances)
    count_min = sum(1 for d in distances if d == min_distance)
    num_possible = upper - lower + 1
    
    return a, count_min, num_possible

print(solve([5]))
print(solve([1, 3, 5]))
print(solve([1, 5]))
print(solve([5, 5, 5]))
