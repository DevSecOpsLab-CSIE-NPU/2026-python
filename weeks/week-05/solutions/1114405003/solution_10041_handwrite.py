def solve(relatives):
    relatives.sort()
    median = relatives[(len(relatives) - 1) // 2]
    return sum(abs(r - median) for r in relatives)

# 測試
print(solve([1, 2, 3]))      # 2
print(solve([1, 2, 3, 4]))   # 4
print(solve([10]))           # 0
