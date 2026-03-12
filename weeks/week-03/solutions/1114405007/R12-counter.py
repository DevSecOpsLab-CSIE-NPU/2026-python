# R12: Counter 計數器
# 觀念：Counter 是 dict 子類別，專門計算元素出現次數。

from collections import Counter

words = ['look', 'into', 'my', 'eyes', 'look']
word_counts = Counter(words)

# most_common(3) 取出出現次數最高的前三名
word_counts.most_common(3)

# update 可累加新的元素計數
word_counts.update(['eyes', 'eyes'])
