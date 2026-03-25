"""
10057 - 中位數與最小距離【簡單版本 - AI教學版】

【核心概念】
找最優 A 使距離和最小：|X1-A| + |X2-A| + ... + |Xn-A|
答案是中位數

【輸出三個值】
1. A 值（最小的最優值）
2. 最小距離個數
3. 可能的 A 個數
"""

def solve(numbers):
    """找使距離和最小的 A"""
    if not numbers:
        return 0, 0, 0
    
    numbers.sort()
    n = len(numbers)
    
    # 找中位數
    if n % 2 == 1:
        median = numbers[n // 2]
        lower = upper = median
    else:
        lower = numbers[n // 2 - 1]
        upper = numbers[n // 2]
    
    # 最小的 A
    a = lower
    
    # 計算距離
    distances = [abs(x - a) for x in numbers]
    min_distance = min(distances)
    count_min = sum(1 for d in distances if d == min_distance)
    
    # 可能的 A 個數
    num_possible = upper - lower + 1
    
    return a, count_min, num_possible


if __name__ == "__main__":
    print(solve([5]))           # (5, 1, 1)
    print(solve([1, 3, 5]))     # (3, 1, 1)
    print(solve([1, 5]))        # (1, 1, 5)
    print(solve([5, 5, 5]))     # (5, 3, 1)
