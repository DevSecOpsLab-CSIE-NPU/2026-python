# U7. OrderedDict 的取捨：保序但更吃記憶體（1.7）

from collections import OrderedDict

# ── 建立具備順序特性的字典 ───────────────────────────
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2

# ── 為什麼它能維持順序？（背後的取捨） ────────────────
# 在 Python 早期版本中，標準 dict 是無序的。
# OrderedDict 為了精確維持「插入順序」，在底層除了哈希表 (Hash Table) 外，
# 還額外維護了一個「雙向鏈結串列」(Doubly Linked List)。

# 1. 記憶體開銷：
# 由於多了鏈結串列來記錄元素的順序，OrderedDict 消耗的記憶體大約是
# 標準字典的兩倍以上。在處理數百萬筆小型資料時，這點需要特別考量。

# 2. 核心優勢：
# 雖然 Python 3.7+ 的標準 dict 也會保序，但 OrderedDict 提供了更多功能：
# - move_to_end()：能將現有鍵移動到字典的開頭或結尾，方便實現 LRU 快取。
# - 比較行為：兩個 OrderedDict 比較時，連「順序」不同都會被視為不相等。

# 3. 輸出保證：
# 當你需要將資料序列化（如轉成 JSON）並嚴格確保欄位順序與輸入完全一致時，
# OrderedDict 是最保險的選擇。