"""benchmark_sort.py - 比較 sort+binary vs linear"""

import random
from timing import timeit
from search import linear_search, binary_search


random.seed(42)
n = 100000
shuffled_data = list(range(n))
random.shuffle(shuffled_data)
target = n // 2

# linear_search（不需排序）
@timeit(repeat=5)
def test_linear():
    return linear_search(shuffled_data, target)

# sort + binary_search
@timeit(repeat=5)
def test_sort_then_binary():
    sorted_data = sorted(shuffled_data)  # 排序會修改資料，所以用 sorted()
    return binary_search(sorted_data, target)

# 只有 binary_search（資料已排序）
@timeit(repeat=5)
def test_binary_only():
    sorted_data = sorted(shuffled_data)
    return binary_search(sorted_data, target)

print("=== sort + binary vs linear ===")
print(f"資料大小: n = {n}")
print()

# 線性搜尋
result_linear = test_linear()
print(f"linear_search: {result_linear}")
print(f"  平均: {test_linear.last_elapsed*1000:.3f} ms")
print()

# sort + binary
result_sort_binary = test_sort_then_binary()
print(f"sort + binary_search: {result_sort_binary}")
print(f"  平均: {test_sort_then_binary.last_elapsed*1000:.3f} ms")
print()

# 只有 binary（已排序）
result_binary = test_binary_only()
print(f"binary_search (已排序): {result_binary}")
print(f"  平均: {test_binary_only.last_elapsed*1000:.3f} ms")
print()

print("=== 結論 ===")
print(f"sort+binary 總耗時: {test_sort_then_binary.last_elapsed*1000:.3f} ms")
print(f"linear 總耗時: {test_linear.last_elapsed*1000:.3f} ms")
print(f"sort+binary 比 linear {'快' if test_sort_then_binary.last_elapsed < test_linear.last_elapsed else '慢'} "
      f"{abs(test_sort_then_binary.last_elapsed - test_linear.last_elapsed)*1000:.3f} ms")