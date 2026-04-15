# 快速檢查程式邏輯
from bisect import bisect_left, insort

def solve_cow_order(n, smaller_counts):
    result = []
    sorted_result = []
    used = set()
    
    result.append(1)
    sorted_result.append(1)
    used.add(1)
    
    for i in range(1, n):
        c = smaller_counts[i - 1]
        found = False
        for num in range(1, n + 1):
            if num not in used:
                count_smaller = bisect_left(sorted_result, num)
                if count_smaller == c:
                    result.append(num)
                    insort(sorted_result, num)
                    used.add(num)
                    found = True
                    break
        if not found:
            raise ValueError(f"位置 {i+1} 無法找到合適編號")
    
    return result

# 測試
print("測試1: N=2, [0]")
r1 = solve_cow_order(2, [0])
print(f"結果: {r1}, 驗證: {set(r1) == {1, 2}}")

print("\n測試2: N=2, [1]")
r2 = solve_cow_order(2, [1])
print(f"結果: {r2}, 驗證: {set(r2) == {1, 2}}")

print("\n測試3: N=4, [0, 1, 2]")
r3 = solve_cow_order(4, [0, 1, 2])
print(f"結果: {r3}, 驗證: {set(r3) == {1, 2, 3, 4}}")

print("\nAll Done!")
