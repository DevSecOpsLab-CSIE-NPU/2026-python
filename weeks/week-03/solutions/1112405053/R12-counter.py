# R12. Counter 統計 + most_common（1.12）

from collections import Counter

words = ['look', 'into', 'my', 'eyes', 'look']
# 建立詞頻統計
word_counts = Counter(words)
# 取出最常見的前 3 名
word_counts.most_common(3)

# 可再用 update 累加新的資料
word_counts.update(['eyes', 'eyes'])
