"""benchmark.py - 使用 timeit 比較 linear_search vs binary_search"""

import random
from timing import timeit
from search import linear_search, binary_search


# 建立測試資料
random.seed(42)
n = 100000
data = list(range(n))
target = n // 2  # 存在於中間的元素

# 打亂資料給 linear_search 用（binary_search 需要排序後的資料）
shuffled_data = data.copy()
random.shuffle(shuffled_data)

# 定義被測試的函式
@timeit(repeat=5)
def test_linear_search():
    return linear_search(shuffled_data, target)

@timeit(repeat=5)
def test_binary_search():
    return binary_search(data, target)

# 執行測試
print("=== 效能比較 ===")
print(f"資料大小: n = {n}")
print(f"目標值: {target} (存在於中間)")
print()

# 線性搜尋
result_linear = test_linear_search()
print(f"linear_search 結果: index = {result_linear}")
print(f"  records: {[f'{t*1000:.3f}ms' for t in test_linear_search.records]}")
print(f"  last_elapsed (平均): {test_linear_search.last_elapsed*1000:.3f} ms")
print()

# 二分搜尋
result_binary = test_binary_search()
print(f"binary_search 結果: index = {result_binary}")
print(f"  records: {[f'{t*1000:.3f}ms' for t in test_binary_search.records]}")
print(f"  last_elapsed (平均): {test_binary_search.last_elapsed*1000:.3f} ms")
print()

# 比較
ratio = test_linear_search.last_elapsed / test_binary_search.last_elapsed
print(f"=== 比較 ===")
print(f"binary_search 比 linear_search 快 {ratio:.1f} 倍")
print(f"(linear: {test_linear_search.last_elapsed*1000:.3f}ms vs binary: {test_binary_search.last_elapsed*1000:.3f}ms)")