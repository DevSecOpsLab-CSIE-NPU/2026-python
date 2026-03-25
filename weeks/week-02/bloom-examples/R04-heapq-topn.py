# ============================================================================
# R4. 堆 (Heap) - 高效取 Top-N（1.4）
# ============================================================================
# 本題展示 heapq 模組如何高效地取得最大/最小的 N 個元素。
# 核心優勢：O(k log n)，當 k << n 時遠快於排序。
# ============================================================================

import heapq

print("【heapq 基本用法】")
print("=" * 50)
print()

print("場景：從 11 個數字中找出最大 / 最小的 3 個\n")

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(f"原始列表：{nums}")
print(f"列表長度：{len(nums)}\n")

print("【方法 1】heapq.nlargest() - 取最大的 N 個")
largest_3 = heapq.nlargest(3, nums)
print(f"heapq.nlargest(3, nums) = {largest_3}\n")

print("【方法 2】heapq.nsmallest() - 取最小的 N 個")
smallest_3 = heapq.nsmallest(3, nums)
print(f"heapq.nsmallest(3, nums) = {smallest_3}\n")

print("=" * 50)
print("【複雜資料結構的 Top-N】")
print("=" * 50)
print()

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
]

print("股票投資組合：")
for stock in portfolio:
    print(f"  {stock}")
print()

print("【需求】找出最便宜的 1 支股票")
print("執行：heapq.nsmallest(1, portfolio, key=lambda s: s['price'])\n")

cheapest = heapq.nsmallest(1, portfolio, key=lambda s: s['price'])
print(f"結果：{cheapest[0]}")
print(f"說明：使用 key 參數提取比較用的值\n")

print("=" * 50)
print("【heapify - 構建堆】")
print("=" * 50)
print()

print("當需要多次取值時，直接 heapify 更高效\n")

heap = list(nums)  # 複製列表
print(f"原始列表：{heap}")

heapq.heapify(heap)
print(f"heapify(heap) 後：{heap}")
print(f"說明：現在 heap[0] 永遠是最小值")
print()

min_val = heapq.heappop(heap)
print(f"heappop(heap) = {min_val}")
print(f"堆此時：{heap}\n")

min_val = heapq.heappop(heap)
print(f"heappop(heap) = {min_val}  （再取一個）")
print(f"堆此時：{heap}\n")

print("=" * 50)
print("【nlargest/nsmallest vs heapify")
print("=" * 50)
print("""
                 nlargest/      heapify      heappop
                 nsmallest      (一次)        (重複)
────────────────────────────────────────────────────
時間複雜度      O(k log n)     O(n)         O(k log n)
場景            k << n         一次性取      多次取值
                k 很小         多個最值

推薦用法：
  ✓ 簡單場景：直接 nlargest() / nsmallest()
  ✓ 複雜場景：先 heapify()，再多次 heappop()
  ✓ key 參數：用於比較複雜物件
""")

print("\n" + "=" * 50)
print("【性能比較】")
print("=" * 50)
print("""
從 1000 個元素中取 Top-10：

方法                           時間複雜度        實際耗時
─────────────────────────────────────────────────────
sorted(nums, reverse=True)[:10]   O(n log n)     約 1000×log1000 ≈ 10000
heapq.nlargest(10, nums)          O(n + k log n) 約 1000 + 10×log1000 ≈ 1130
                                  ✓ 快 8-9 倍！
""")
