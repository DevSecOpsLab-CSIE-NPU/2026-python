"""
測試程式碼 - UVA 100 The 3n+1 Problem
ZeroJudge: c039
"""

memo = {1: 1}


def cycle_length(n):
    path = []
    current = n
    while current not in memo:
        path.append(current)
        if current % 2 == 0:
            current = current // 2
        else:
            current = 3 * current + 1
    base = memo[current]
    for i, val in enumerate(reversed(path)):
        memo[val] = base + i + 1
    return memo[n]


def max_cycle_in_range(i, j):
    lo, hi = min(i, j), max(i, j)
    return max(cycle_length(n) for n in range(lo, hi + 1))


def run_tests():
    test_cases = [
        (1, 10, 20),
        (100, 200, 125),
        (201, 210, 89),
        (900, 1000, 174),
        (10, 1, 20),
        (22, 22, 16),
        (1, 1, 1),
    ]

    passed = 0
    failed = 0
    print("=" * 50)
    print("UVA 100 測試結果")
    print("=" * 50)

    for i, j, expected in test_cases:
        result = max_cycle_in_range(i, j)
        status = "PASS" if result == expected else "FAIL"
        if result == expected:
            passed += 1
        else:
            failed += 1
        print(f"[{status}]  輸入: {i} {j}  →  輸出: {i} {j} {result}  (預期: {expected})")

    print("-" * 50)
    print(f"共 {passed + failed} 筆，通過 {passed} 筆，失敗 {failed} 筆")


if __name__ == "__main__":
    run_tests()