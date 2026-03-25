def solve(n, hartal_params):
    loss = 0
    for day in range(1, n + 1):
        day_of_week = (day - 1) % 7
        if day_of_week not in [1, 2, 3, 4]:
            continue
        if any(day % h == 0 for h in hartal_params):
            loss += 1
    return loss

print(solve(7, [3]))
print(solve(10, [2, 3]))
