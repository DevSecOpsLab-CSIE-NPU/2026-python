def win_prob(n, p, i):
    if p == 1.0:
        return 1.0 if i == 1 else 0.0
    fail = 1 - p
    return (fail ** (i - 1)) * p / (1 - (fail ** n))

print(f"{win_prob(1, 0.5, 1):.4f}")
print(f"{win_prob(2, 0.5, 1):.4f}")
print(f"{win_prob(2, 0.5, 2):.4f}")
print(f"{win_prob(3, 1/6, 1):.4f}")
