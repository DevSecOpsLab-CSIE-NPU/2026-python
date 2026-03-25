def solve(n, hartal_params):
    loss = 0
    for day in range(1, n + 1):
        if (day - 1) % 7 not in [1, 2, 3, 4]:
            continue
        for h in hartal_params:
            if day % h == 0:
                loss += 1
                break
    return loss

# 測試
print(solve(7, [3]))      # 1
print(solve(10, [2, 3]))  # 5
