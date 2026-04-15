# R12. Counter 統計 + most_common（1.12）

from collections import Counter

words = ['look', 'into', 'my', 'eyes', 'look']
# 快速統計每個單字出現次數
word_counts = Counter(words)
# 取出前 3 名高頻元素
word_counts.most_common(3)

# 可持續更新計數
word_counts.update(['eyes', 'eyes'])
