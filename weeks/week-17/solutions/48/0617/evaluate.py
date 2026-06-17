"""效能評估：linear_search vs binary_search"""

import random
from timing import timeit
from search import linear_search, binary_search

linear_search = timeit(linear_search, repeat=100)
binary_search = timeit(binary_search, repeat=100)

sizes = [1000, 5000, 10000, 50000]

print(f"{'n':>8} {'linear (s)':>12} {'binary (s)':>12} {'ratio':>10}")
print("-" * 44)

for n in sizes:
    data = sorted(random.sample(range(n * 10), n))
    target = random.choice(data)

    linear_search(data, target)
    linear_time = linear_search.last_elapsed

    binary_search(data, target)
    binary_time = binary_search.last_elapsed

    ratio = linear_time / binary_time if binary_time > 0 else float("inf")
    print(f"{n:>8} {linear_time:>12.8f} {binary_time:>12.8f} {ratio:>10.2f}x")

print()
print("結論：")
print("- linear_search: O(n), 資料量越大時間線性增長")
print("- binary_search: O(log n), 即使 n 大幅增加耗時變化很小")
print("- 排序成本 vs 搜尋次數：若只搜尋一次且資料未排序，linear 可能更划算")
