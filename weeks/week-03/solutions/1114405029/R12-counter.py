# R12. Counter 統計 + most_common（1.12）

from collections import Counter

# ── 1. 初始化計數器 ──────────────────────────────────
words = ['look', 'into', 'my', 'eyes', 'look']

# Counter 會自動走訪列表，計算每個元素出現的次數
# 建立後 word_counts 內容約為：{'look': 2, 'into': 1, 'my': 1, 'eyes': 1}
word_counts = Counter(words)

# ── 2. 獲取出現頻率最高的元素 ────────────────────────
# most_common(n) 方法會回傳一個列表，包含前 n 個最常出現的元素及其計數
# 結果：[('look', 2), ('into', 1), ('my', 1)]
word_counts.most_common(3)

# ── 3. 更新計數器內容 ────────────────────────────────
# update() 方法不會取代原有的資料，而是將新的元素「累加」進去
# 這裡手動加入兩個 'eyes'
word_counts.update(['eyes', 'eyes'])

# 更新後，'eyes' 的計數從 1 變成 3
# 此時 word_counts['eyes'] == 3