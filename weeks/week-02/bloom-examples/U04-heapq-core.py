# ============================================================================
# U4. Heap 資料結構：高效取得最小值（1.4）
# ============================================================================
# 本題展示 heap（堆）的核心性質：h[0] 永遠是最小值。
# 
# 關鍵特性：
# 1. heap 是部分排序的二叉樹（不是完全排序）
# 2. 樹根（h[0]）永遠是最小值
# 3. 插入/刪除 — O(log n)，比排序更快
# ============================================================================

import heapq


print("【Heap 基礎概念】")
print("=" * 50)
print("""
Heap 的性質：
  - 完全二叉樹 (complete binary tree)
  - 最小堆：每個父節點 ≤ 子節點
  - 最大堆：每個父節點 ≥ 子節點
  
Python heapq 模組提供：
  - 最小堆實現
  - h[0] 永遠是最小值
  - 不提供「排序」列表，而是「部分排序」
""")

print("\n" + "=" * 50)
print("【建立 Heap】")
print("=" * 50)
print()

nums = [5, 1, 9, 2]
print(f"原始列表：{nums}")
print(f"說明：無序的數字\n")

print("【方法 1】使用 heapify() 原地建立")
print()

h = nums[:]
print(f"複製列表：h = nums[:]  # {h}")

heapq.heapify(h)
print(f"heapify(h)")
print(f"結果：h = {h}")
print()

print(f"內部結構（二叉樹）：")
print(f"""
        1        ← h[0] 是最小值
       / \\
      2   5     ← 子節點都 ≥ 父節點
     /
    9             ← 葉節點
""")
print()

print(f"【重要】h 不是排序的！")
print(f"  排序結果應該是：[1, 2, 5, 9]")
print(f"  但 h 只是部分排序：{h}")
print(f"  唯一保證：h[0] = {h[0]} 是最小值")
print()

print("【方法 2】使用 heappush() 逐個插入")
print()

h2 = []
for num in nums:
    heapq.heappush(h2, num)
    print(f"  heappush(h2, {num}) → h2 = {h2}")

print()
print(f"結果與 heapify() 相同：{h2}")
print()

# ──────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 50)
print("【提取最小值】")
print("=" * 50)
print()

print(f"初始 heap：{h}\n")

print("【heappop() 操作】每次返回最小值\n")

min_vals = []
while h:
    m = heapq.heappop(h)
    min_vals.append(m)
    print(f"heappop(h) = {m:2d} → 剩餘 h = {h}")

print()
print(f"提取順序：{min_vals}")
print(f"說明：完全排序！這是 heappop 的性質")
print()

# ──────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 50)
print("【應用 1】Top-N 問題（為何 Heap 高效？）")
print("=" * 50)
print()

print("問題：從 100 萬個數字中找到工作 10 大")
print()

data = [15, 23, 8, 42, 5, 99, 1, 50, 30, 12, 88, 7]  # 簡化範例
k = 3  # 找前 3 個最小值

print(f"資料（12 個數字）：{data}")
print(f"需求：找到最小的 {k} 個\n")

print("【方法 A】排序（低效，尤其是 k << n）")
print()
print(f"代碼：sorted(data)[:k]")
sorted_result = sorted(data)[:k]
print(f"結果：{sorted_result}")
print(f"時間複雜度：O(n log n)")
print()

print("【方法 B】Heap（高效）")
print()
print(f"代碼：heapq.nsmallest(k, data)")
heap_result = heapq.nsmallest(k, data)
print(f"結果：{heap_result}")
print(f"時間複雜度：O(k log n)  ← 當 k << n 時，明顯更快")
print()

print(f"【比較】")
print(f"  排序：O(n log n) = O(12 log 12) ≈ 40 操作")
print(f"  Heap：O(k log n) = O(3 log 12) ≈ 10 操作")
print()

# ──────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 50)
print("【應用 2】Dijkstra 最短路徑演算法")
print("=" * 50)
print()

print("場景：在圖中找到某節點到其他節點的最短路徑")
print()
print("演算法步驟：")
print("  1. 初始化距離 heap")
print("  2. 不斷提取最小距離的節點")
print("  3. 更新相鄰節點的距離")
print("  4. 重複直到完成")
print()
print("為什麼用 Heap？")
print("  ✓ 每次 O(log n) 時間找到最短距離")
print("  ✓ 大圖上性能顯著優於掃描所有節點")
print()

# ──────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 50)
print("【常用 heapq 函式】")
print("=" * 50)
print()

data = [5, 1, 9, 2]

print(f"資料：{data}\n")

print("1. heapq.nsmallest(k, iterable)  # 找前 k 小")
result = heapq.nsmallest(3, data)
print(f"   nsmallest(3, data) = {result}")
print()

print("2. heapq.nlargest(k, iterable)  # 找前 k 大")
result = heapq.nlargest(3, data)
print(f"   nlargest(3, data) = {result}")
print()

print("3. heapq.heappushpop(heap, item)  # 插入後彈出")
h = [1, 2, 5, 9]
result = heapq.heappushpop(h, 3)
print(f"   初始 heap = {h}")
print(f"   heappushpop(h, 3) 返回 {result}，heap 變成 {h}")
print()

print("4. heapq.heapreplace(heap, item)  # 彈出後插入")
h = [1, 2, 5, 9]
result = heapq.heapreplace(h, 3)
print(f"   初始 heap = {h}")
print(f"   heapreplace(h, 3) 返回 {result}，heap 變成 {h}")
print()

print("\n" + "=" * 50)
print("【總結】")
print("=" * 50)
print("""
Heap 的優勢：
✓ 快速找到極值（最小/最大）：O(1) 查看，O(log n) 移除
✓ 高效的 Top-N 問題：O(k log n) 代替 O(n log n)
✓ 優先級隊列實現
✓ 圖演算法（Dijkstra、Prim）

何時使用 Heap：
✓ 反覆需要找最小/最大值
✓ Top-N 問題
✓ 優先級隊列
✗ 需要完全排序（用 sorted() 或 sort()）
""")
