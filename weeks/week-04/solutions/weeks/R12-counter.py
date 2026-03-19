# R12. Counter 統計 + most_common（1.12）

from collections import Counter

# 一個簡單的字串列表
words = ['look', 'into', 'my', 'eyes', 'look']

# 建立 Counter 物件，會自動統計每個元素出現的次數
word_counts = Counter(words)
# word_counts = {'look': 2, 'into': 1, 'my': 1, 'eyes': 1}

# most_common(n) 回傳出現次數最多的前 n 個元素（依次數排序）
word_counts.most_common(3)
# → [('look', 2), ('into', 1), ('my', 1)]

# update() 可以用來增加計數（可傳入可迭代物件）
word_counts.update(['eyes', 'eyes'])
# 'eyes' 的計數會增加 2