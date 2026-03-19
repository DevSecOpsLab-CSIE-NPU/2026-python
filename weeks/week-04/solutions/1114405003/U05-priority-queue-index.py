# U5. 優先佇列為何要加 index（1.5）
# 此示例演示在使用 heapq 實現優先隊列時為什麼必須添加 index
# 當兩個元素的優先級相同時，Python 會比較元組中的下一個元素
# 如果該元素不支持比較（如自定義對象），就會拋出 TypeError

# 導入 heapq 模組設計優先隊列
import heapq

# ===== 定義自定義對象 =====
# 建立一個簡單的 Item 類，代表優先隊列中的元素
class Item:
    def __init__(self, name):
        self.name = name

# ===== 建立優先隊列 =====
# Python 的優先隊列通常基於堆實現
pq = []

# ===== 問題演示：為什麼不能只用 (priority, item) =====
# 嘗試建立包含 (優先級, Item 對象) 的優先隊列
# 當優先級相同時，heapq 會嘗試比較 Item 對象以決定順序

# 注意：以下代碼會拋出 TypeError，因為 Item 類沒有定義 __lt__ 方法
# heapq.heappush(pq, (-1, Item('a')))  # 優先級 -1，項目 Item('a')
# heapq.heappush(pq, (-1, Item('b')))  # 優先級 -1，項目 Item('b')
# TypeError：'<' not supported between instances of 'Item' and 'Item'

# ===== 為什麼會出現 TypeError =====
# 1. heapq._siftup 或 heapq._siftdown 需要比較元素以維持堆的性質
# 2. 當兩個元組的第一個元素（優先級 -1）相等時
# 3. Python 會比較元組的第二個元素（Item 對象）
# 4. Item 對象沒有定義 __lt__（小於）方法，導致比較失敗
# 5. 拋出 TypeError："'<' not supported between instances of 'Item' and 'Item'"

# ===== 解決方案：添加 index =====
# 使用 (priority, index, item) 的三元組結構
# - priority：優先級（主要排序鍵）
# - index：遞增的唯一索引（打破優先級相同時的平局）
# - item：實際的數據對象

# 建立計數器用於生成唯一的索引
idx = 0

# 推入第一個項目，優先級 -1，索引 0
# 當使用 (priority, index, item) 時，即使優先級相同，
# index 也會用於比較，避免了比較 Item 對象
heapq.heappush(pq, (-1, idx, Item('a')))  # (-1, 0, Item('a'))
idx += 1  # 索引遞增

# 推入第二個項目，優先級 -1，索引 1
# 索引 0 和 1 都是整數，可以無問題地比較
heapq.heappush(pq, (-1, idx, Item('b')))  # (-1, 1, Item('b'))
idx += 1  # 索引遞增

# ===== 元組比較的順序 =====
# Python 比較元組時遵循字典序（lexicographic order）：
# 1. 首先比較第一個元素（優先級）
#    - 如果優先級不同，赢者就是優先級小/大（取決於 heap 是 min/max）
#    - 如果優先級相同，繼續
# 2. 然後比較第二個元素（index）
#    - 兩個索引都是整數，總是可以比較
#    - 索引較小的元素在堆中位置較高
# 3. 永遠不需要比較第三個元素（item），因為 index 已經決定了順序

# ===== 為什麼索引有效 =====
# - Index 是唯一的遞增值，確保相同優先級的元素有明確的順序
# - 整數總是可以比較的，不會拋出 TypeError
# - 實現 FIFO 行為：相同優先級的項目按插入順序處理
# - Index 沒有實際語義，只是用於打破平局

print(heapq)  # 查看 heapq 模組
