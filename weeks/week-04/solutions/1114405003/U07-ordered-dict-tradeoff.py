# U7. OrderedDict 的取捨：保序但更吃記憶體（1.7）
# 此示例演示 OrderedDict 的特性和權衡
# OrderedDict 能保證元素按插入順序排列，但需要額外的內存開銷來維持這個順序

# 導入 OrderedDict 從 collections 模組
from collections import OrderedDict

# ===== 建立 OrderedDict =====
# OrderedDict 是 dict 的子類，主要區別是保證元素的插入順序
# 普通 dict 在 Python 3.7+ 後也保序，但 OrderedDict 提供了額外的功能
d = OrderedDict()

# ===== 插入元素 =====
# 插入第一個鍵值對
d['foo'] = 1

# 插入第二個鍵值對
d['bar'] = 2

# ===== 保序特性 =====
# 遍歷 OrderedDict 時，元素總是按照插入順序出現
# for k, v in d.items():
#     print(k, v)  # 結果：foo 1，然後 bar 2

# ===== 為什麼 OrderedDict 需要額外記憶體 =====
# 背景：普通字典（Python 3.6 之前）使用哈希表存儲，順序不保證
# OrderedDict 實現方式：
# 1. 內部使用一個雙向鏈表（doubly-linked list）
#    - 每個節點記錄前一個和後一個元素的位置
#    - 用於維持插入順序
# 2. 加上普通哈希表進行快速查找
#    - O(1) 時間複雜度查找值
#    - 同時保持元素順序

# 額外的記憶體開銷來自：
# 1. 每個元素增加兩個指針（前驅和後繼）
# 2. 鏈表頭尾指針
# 3. 額外的節點對象
# => 大約增加 2-3 倍的記憶體使用量

# ===== OrderedDict 相比普通 dict 的額外功能 =====
# 即使 Python 3.7+ 的 dict 也保序了，OrderedDict 還有其他優勢：
# 1. move_to_end(key)：將指定鍵移到末尾或開頭
d_example = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# d_example.move_to_end('a')  # 將 'a' 移到末尾
# d_example.move_to_end('b', last=False)  # 將 'b' 移到開頭

# 2. popitem()：彈出最後一個項（或 FIFO if last=False）
# d_example.popitem()  # 返回並移除 ('c', 3)
# d_example.popitem(last=False)  # 返回並移除 ('b', 2)

# ===== 何時使用 OrderedDict =====
# 1. 需要 move_to_end() 或 popitem() 的 FIFO 功能
# 2. 需要與預期 dict 是有序的舊代碼兼容（Python 3.7+ 時大部分不需要）
# 3. 實現 LRU 緩存（結合 move_to_end()）
# 4. 需要明確表達「順序很重要」的代碼意圖

# ===== 何時不需要使用 OrderedDict =====
# Python 3.7+ 時：
# 1. 如果只需要保序，普通 dict 就足夠
# 2. 普通 dict 內存更省，性能略好
# 3. 無需額外的 move_to_end() 功能

# ===== OrderedDict 的實現成本（幾乎總是保序，只有在需要額外功能時才用）=====
# 時間複雜度：
# - 插入、查找、刪除：O(1)（與普通 dict 相同）
# - move_to_end()：O(1)（額外功能）

# 空間複雜度：
# - OrderedDict：O(n)，但常數因子更大（額外的鏈表指針）
# - 普通 dict（Python 3.7+）：O(n)，常數因子更小

# ===== 使用建議 =====
# 優先用普通 dict，除非你需要：
# 1. move_to_end() 或 popitem(last=False) 功能
# 2. 與舊代碼的兼容性（Python < 3.7）
# 3. 明確表達「順序關鍵」的設計意圖
