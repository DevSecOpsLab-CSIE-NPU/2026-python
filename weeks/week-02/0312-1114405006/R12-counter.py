# R12. Counter 統計 + most_common（1.12）
#
# Counter 是用來計數的工具：
# 1. 直接把可迭代物件丟進去，就會自動統計每個元素出現次數。
# 2. most_common(n) 可以取出出現次數最多的前 n 名。
# 3. update() 可以把新的資料加進統計結果中。

from collections import Counter

words = ['look', 'into', 'my', 'eyes', 'look']
word_counts = Counter(words)
word_counts.most_common(3)

word_counts.update(['eyes', 'eyes'])
