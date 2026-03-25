def solve(relatives):
    relatives.sort()
    median = relatives[(len(relatives) - 1) // 2]
    return sum(abs(r - median) for r in relatives)

print(solve([1, 2, 3]))
print(solve([1, 2, 3, 4]))
print(solve([10]))
print(solve([1, 5]))
