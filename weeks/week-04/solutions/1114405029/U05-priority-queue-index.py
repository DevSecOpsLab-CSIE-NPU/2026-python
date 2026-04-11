# U5. 優先佇列為何要加 index（1.5）

import heapq

# ── 定義自定義類別 ────────────────────────────────────
class Item:
    def __init__(self, name):
        self.name = name
    
    # 注意：此類別沒有實作 __lt__ (小於) 等比較方法

pq = []

# ── 錯誤情境分析 ─────────────────────────────────────
# 在 Python 的元組比較中，若第一個元素 (priority) 相同，它會自動比較第二個元素。
# 下面這兩行若執行，當推入第二個 Item 時：
# 1. 優先權都是 -1，相同。
# 2. Python 嘗試比較 Item('a') < Item('b')。
# 3. 由於 Item 類別不支援小於運算，會拋出 TypeError。

# heapq.heappush(pq, (-1, Item('a')))
# heapq.heappush(pq, (-1, Item('b')))  # 這行會炸掉：TypeError

# ── 正確解法：引入序列號 (Index) ──────────────────────
# 在優先權與物件之間插入一個永遠不會重複且支援比較的數字（如遞增索引）。
idx = 0

# 運作邏輯：
# 1. 先比較優先權 (-1 vs -1) -> 相同。
# 2. 再比較索引值 (0 vs 1) -> 不同！
# 3. 既然索引值已經分出勝負，Python 就不會再去比較後方的 Item 物件。
heapq.heappush(pq, (-1, idx, Item('a'))); idx += 1
heapq.heappush(pq, (-1, idx, Item('b'))); idx += 1

# 結果：順利運作且保證了「先進先出」(FIFO) 的公平性（相同優先權時，先加進去的先出來）。