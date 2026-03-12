# R12 counter
# 目標：示範 Counter 計數與 most_common。

from collections import Counter

words = ["look", "into", "my", "eyes", "look"]
word_counts = Counter(words)

# 取出出現次數前 3 名
top3 = word_counts.most_common(3)

# 批次更新計數
word_counts.update(["eyes", "eyes"])
