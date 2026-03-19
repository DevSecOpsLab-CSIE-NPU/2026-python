# U4. heap 為何能高效拿 Top-N（1.4）
#
# heapq 提供的 heap 是一種「二元堆」（binary heap）實作，
# 它維持的是「最小堆」性質：任何節點的值不大於其子節點的值。
# 這代表最小值一定存在於索引 0（h[0]），因此取最小值的操作非常快速。
#
# heap 的核心特性：
# - 建堆 (heapify) 是 O(n)
# - 取最小值 (heappop) 是 O(log n)，但只需遍歷堆高度
# - 插入 (heappush) 也是 O(log n)
#
# 因此若要取 Top-N（最小或最大 N 筆）資料，比起排序整個序列更有效率。

import heapq

nums = [5, 1, 9, 2]
# 拷貝一份，避免修改原始列表
h = nums[:]

# heapify 會把列表原地轉成 heap 結構
heapq.heapify(h)

# 依照 heap 性質，h[0] 永遠是目前的最小值
# 即使堆內元素順序不是完全排序（只是部分有序），最小值仍然在最前面
m = heapq.heappop(h)  # 每次 pop 都拿到目前最小值

print("原始 nums:", nums)
print("heapify 後的 h:", h)
print("pop 出來的最小值:", m)
print("pop 之後剩下的 heap:", h)
