# U04. heap 為何能高效拿 Top-N（1.4）
# 觀念：heapq 是最小堆(min-heap)；堆頂 h[0] 永遠是目前最小值。

import heapq


def section(title: str) -> None:
    print(f"\n=== {title} ===")


section("建立最小堆")
nums = [5, 1, 9, 2, 8, 3]
h = nums[:]
heapq.heapify(h)
print("原始 nums:", nums)
print("heapify 後內部陣列:", h)
print("最小值 h[0]:", h[0])

section("heappop 依序取最小")
while h:
    print("pop ->", heapq.heappop(h))

section("快速取最大/最小 N 筆")
portfolio = [12, 88, 3, 56, 42, 91, 7]
print("3 個最小值:", heapq.nsmallest(3, portfolio))
print("2 個最大值:", heapq.nlargest(2, portfolio))
